import threading
from elevator import Elevator, Direction


class ElevatorSystem:
    def __init__(self, num_elevators: int = 2):
        self.elevators: list[Elevator] = [Elevator(i) for i in range(num_elevators)]
        self.system_lock = threading.Lock()  # Create lock for the system

    def request_elevator(self, requested_floor: int, direction: Direction):
        best_elevator = self.find_best_elevator(requested_floor, direction)
        if best_elevator:
            with self.system_lock:
                best_elevator.request_elevator(requested_floor, direction)

    def find_best_elevator(self, requested_floor: int, direction: Direction):
        # Choose the best elevator based on several criteria:
        # 1. An elevator already moving towards the requested floor is priotity
        # 2. An idle elevator is also a good choice
        # 3. Otherwise, just pick the elevator with the smallest workload (fewest requests).
        best_elevator = None

        for elevator in self.elevators:
            with elevator.lock:
                if (elevator.direction == direction
                    and ((direction == Direction.UP and elevator.current_floor <= requested_floor)
                         or (direction == Direction.DOWN and elevator.current_floor >= requested_floor))):
                    best_elevator = elevator
                    break
                elif elevator.direction == Direction.IDLE:
                    best_elevator = elevator
                    break

        if not best_elevator:
            with self.system_lock:
                best_elevator = min(self.elevators, key=lambda e: e.requests.qsize())
                print(f"Choosing elevator {best_elevator.id} which has the least number of requests")

        return best_elevator
