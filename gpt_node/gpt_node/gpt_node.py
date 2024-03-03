import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from interfaces.srv import Gptsrv
import openai
import re
import argparse
import math
import numpy as np
import os
import json
import time
import subprocess

class gpt(Node):
  def __init__(self):
    super().__init__('gpt_node')
    self.srv = self.create_client(Gptsrv, '/gpt_service')
    self.req = Gptsrv.Request()
    parser = argparse.ArgumentParser()

    current_file_path=os.path.dirname(os.path.abspath("gpt_node.py"))
    print(current_file_path)
    parser.add_argument("--prompt", type=str, default=current_file_path+"/src/gpt_node/gpt_node/prompts/assistant.txt")
    parser.add_argument("--sysprompt", type=str, default=current_file_path+"/src/gpt_node/gpt_node/system_prompts/system.txt")
    args = parser.parse_args()
    with open(args.sysprompt, "r") as f:
      self.sysprompt = f.read()
    with open(args.prompt, "r") as f:
      self.prompt = f.read()
    with open(current_file_path+"/build/gpt_node/gpt_node/config.json","r") as f:
      config = json.load(f)
    openai.api_key = config["OPENAI_API_KEY"]
    self.operate()

  def operate(self) :
    while(True) :
      inst=input("명령을 입력하세요 : ")
      if inst=='setting' :
        setting()
      else :
        quanswer=self.ask(inst)
        code=self.separate_code(quanswer)
        self.write_code(code)
  def write_code(self,code) :
    str(code)
    try:
        with open("src/gpt_node/gpt_node/gpt_code.py", 'w') as file:
          file.truncate(0)
          file.write(str(code))
        print(f"데이터를 성공적으로 썼습니다.")
    except Exception as e:
        print(f"파일 쓰기 오류: {e}")

  def sand_func(self,func) :
    print(func+"를 실행")
    self.req.a = str(func)
    self.future = self.srv.call_async(self.req)
    rclpy.spin_until_future_complete(self, self.future)
    if self.future.result() == 1:
     return
    else :
      print("오류발생")
      return

  def ask(self,prompt) :
    chat_history = [
    {
        "role": "system",
        "content": self.sysprompt
    },
    {
        "role": "user",
        "content": prompt
    },
    {
        "role": "assistant",
        "content": self.prompt
    }]


    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=0
    )
    print("-----실행할 main 함수-----")
    print(completion.choices[0].message.content)
    print("--------------------------")
    return completion.choices[0].message.content

  def separate_code(self,input_string):
    match = re.search(r"python(.+?)```", input_string, re.DOTALL)
    if match:
      print(match.group(1))
      return match.group(1)
    else:
      return input_string

def setting() :
  print("지도작성 및 환경 데이터 수집 시작")



def main(args=None):
  rclpy.init(args=args)
  gpt_service = gpt()
  rclpy.spin(gpt_service)
  gpt_service.destroy_node()
if __name__ == '__main__':
    main()
