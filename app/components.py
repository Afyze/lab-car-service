from typing import List
from app.interfaces import Queue, Refuelable, Dineable
from app.models import Car


class StatsCollector:
    stats = {
        "ELECTRIC": 0,
        "GAS": 0,
        "PEOPLE": 0,
        "ROBOTS": 0,
        "DINING": 0,
        "NOT_DINING": 0,
        "CONSUMPTION": {"ELECTRIC": 0, "GAS": 0}
    }

    @classmethod
    def reset(cls):
        cls.stats = {
            "ELECTRIC": 0,
            "GAS": 0,
            "PEOPLE": 0,
            "ROBOTS": 0,
            "DINING": 0,
            "NOT_DINING": 0,
            "CONSUMPTION": {"ELECTRIC": 0, "GAS": 0}
        }


class ListQueue(Queue[Car]):
    def __init__(self):
        self._items: List[Car] = []

    def enqueue(self, item: Car) -> None:
        self._items.append(item)

    def dequeue(self) -> Car:
        if not self.is_empty():
            return self._items.pop(0)
        return None

    def is_empty(self) -> bool:
        return len(self._items) == 0


class GasStation(Refuelable):
    def refuel(self, car: Car) -> None:
        if car.type != "GAS":
            raise ValueError(f"GasStation cannot refuel {car.type}")

        print(f"Refueling gas car {car.id}.")
        StatsCollector.stats["GAS"] += 1
        StatsCollector.stats["CONSUMPTION"]["GAS"] += car.consumption


class ElectricStation(Refuelable):
    def refuel(self, car: Car) -> None:
        if car.type != "ELECTRIC":
            raise ValueError(f"ElectricStation cannot charge {car.type}")

        print(f"Charging electric car {car.id}.")
        StatsCollector.stats["ELECTRIC"] += 1
        StatsCollector.stats["CONSUMPTION"]["ELECTRIC"] += car.consumption


class PeopleDinner(Dineable):
    def serve_dinner(self, car: Car) -> None:
        if car.passengers != "PEOPLE":
            raise ValueError("PeopleDinner cannot serve Robots")

        print(f"Serving dinner to people in car {car.id}.")
        StatsCollector.stats["PEOPLE"] += 1
        StatsCollector.stats["DINING"] += 1


class RobotDinner(Dineable):
    def serve_dinner(self, car: Car) -> None:
        if car.passengers != "ROBOTS":
            raise ValueError("RobotDinner cannot serve People")

        print(f"Serving energy to robots in car {car.id}.")
        StatsCollector.stats["ROBOTS"] += 1
        StatsCollector.stats["DINING"] += 1