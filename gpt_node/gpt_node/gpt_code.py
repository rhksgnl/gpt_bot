import gpt_api

def main():
    coffee_coordinates = gpt_api.find("coffee")
    if coffee_coordinates is None:
        print("No coffee found")
        return

    global_coffee_coordinates = gpt_api.local_to_global(coffee_coordinates)
    if gpt_api.move_to_coordinates(global_coffee_coordinates) != 1:
        print("Failed to move to coffee")
        return

    if gpt_api.pick_up(coffee_coordinates) != 1:
        print("Failed to pick up coffee")
        return

    print("Coffee picked up successfully!")

if __name__ == "__main__":
    main()