from rclpy.node import Node

def find(object) :
  print("find 실행")
  return 1
def local_to_global(local_coordinates) :
  print("local_to_global실행")
  return 1
def pick_up(local_cpprdomates) :
  print("pick_up 실행")
  return 1
def move_to_coordinates(coordinates) :
  print("move_to_coordinates 실행")
  return 1
def get_object_coordinates(object_name) :
  print("get_object_coordinates 실행")
  return 1
def coordinates_3D(local_coordinates) :
  print("coordinates_3D 실행")
  return 1

def put_it_down(object) :
  print("put_it_down 실행")
  return 1

class coordinate_3D:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
