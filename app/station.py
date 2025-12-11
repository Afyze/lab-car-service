from app.interfaces import Queue, Refuelable, Dineable
from app.models import Car
from app.components import StatsCollector


class CarStation:
    def __init__(self, refueling_service: Refuelable, dining_service: Dineable, queue: Queue[Car]):
        self.refueling_service = refueling_service
        self.dining_service = dining_service
        self.queue = queue

    def add_car(self, car: Car) -> None:
        self.queue.enqueue(car)

    def serve_cars(self) -> None:
        while not self.queue.is_empty():
            car = self.queue.dequeue()

            self.refueling_service.refuel(car)

            if car.is_dining:
                self.dining_service.serve_dinner(car)
            else:
                StatsCollector.stats["NOT_DINING"] += 1
                StatsCollector.stats[car.passengers] += 1