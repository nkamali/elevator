import threading
import time
from enum import Enum
from queue import PriorityQueue


class Direction(Enum):
    UP = 1
    DOWN = 2
    IDLE = 3


class Elevator:
    def __init__(self, id: int):
        self.id: int = id
        self.current_floor: int = 0
        self.target_floor: int = 0
        self.direction: Direction = Direction.IDLE
        self.travel_speed_seconds_per_floor: int = 1  # used to simulate time it takes to move between floors
        self.requests = PriorityQueue()
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self.move)
        self.thread.start()

    def _calculate_score(self, request_floor: int, current_floor: int, direction: Direction):
        distance = abs(current_floor - request_floor)
        if ((direction == Direction.UP and request_floor < current_floor) or
           (direction == Direction.DOWN and request_floor > current_floor)):
            distance += 1000  # add large number to give low priority
        return distance

    def request_elevator(self, requested_floor: int, direction: str):
        with self.lock:
            score = self._calculate_score(requested_floor, self.current_floor, self.direction)
            self.requests.put((score, requested_floor, direction))

    def _remove_item(self, q, item_to_remove):
        new_q = PriorityQueue()
        while not q.empty():
            item = q.get()
            if item != item_to_remove:
                new_q.put(item)
        return new_q

    def _set_direction(self):
        with self.lock:
            self.target_floor = self.requests.queue[0][1]
            print(f'in {threading.current_thread().name} target floor is {self.target_floor}')
            if self.target_floor > self.current_floor:
                self.direction = Direction.UP
            elif self.target_floor < self.current_floor:
                self.direction = Direction.DOWN
            else:
                self.direction = Direction.IDLE

    def _next_floor(self):
        if self.direction == Direction.UP:
            return self.current_floor + 1
        elif self.direction == Direction.DOWN:
            return self.current_floor - 1
        else:
            return self.current_floor

    def _serve_requests_on_the_way(self):
        print("what's in the queue: ", list(self.requests.queue))
        for request in list(self.requests.queue):
            if request[1] == self.current_floor:
                print(f"Elevator {self.id} is serving request at floor {request[1]}")
                self.requests = self._remove_item(self.requests, request)

    def move(self):
        while True:
            if not self.requests.empty():
                self._set_direction()

                current_floor = self.current_floor
                target_floor = self.target_floor

                while current_floor != target_floor and not self.requests.empty():
                    time.sleep(self.travel_speed_seconds_per_floor)  # simulate time taken to move between floors
                    self.current_floor = self._next_floor()
                    self._serve_requests_on_the_way()

                    print(f"Elevator {self.id} is at floor {self.current_floor}")

                print(f"Elevator {self.id} has arrived at floor {self.current_floor}")
                print("what's in the queue: ", list(self.requests.queue))
                self.requests.get()
                self.direction = Direction.IDLE  # reset direction after serving a request
            else:
                time.sleep(1)
