import threading

from elevator_system import ElevatorSystem, Direction


if __name__ == "__main__":
    elevator_system = ElevatorSystem(1)

    def user_input():
        while True:
            my_floor = input("What floor are you?\n")
            if my_floor.lower() == 'quit':
                break

            if my_floor == '':
                continue

            my_floor = int(my_floor.strip())
            direction = Direction[input("Going up or down?\n").strip().upper()]

            elevator_system.request_elevator(my_floor, direction)

    user_input_thread = threading.Thread(target=user_input)

    # Set the thread to be a "daemon" thread, which means it will automatically exit when the main program finishes
    user_input_thread.daemon = True
    user_input_thread.start()
