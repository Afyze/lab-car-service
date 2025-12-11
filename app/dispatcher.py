import json
from app.models import Car
from app.components import (
    ListQueue, GasStation, ElectricStation,
    PeopleDinner, RobotDinner, StatsCollector
)
from app.station import CarStation


class Dispatcher:
    def __init__(self):
        # We need 4 variations of stations to cover all combinations
        # 1. Gas + People
        self.station_gp = CarStation(GasStation(), PeopleDinner(), ListQueue())
        # 2. Gas + Robots
        self.station_gr = CarStation(GasStation(), RobotDinner(), ListQueue())
        # 3. Electric + People
        self.station_ep = CarStation(ElectricStation(), PeopleDinner(), ListQueue())
        # 4. Electric + Robots
        self.station_er = CarStation(ElectricStation(), RobotDinner(), ListQueue())

    def load_cars(self, filename: str):
        with open(filename, 'r') as f:
            data = json.load(f)

        for item in data:
            car = Car(
                id=item['id'],
                type=item['type'],
                passengers=item['passengers'],
                is_dining=item['isDining'],
                consumption=item['consumption']
            )
            self.route_car(car)

    def route_car(self, car: Car):
        # Logic to route car to specific station (Task 4)
        if car.type == "GAS":
            if car.passengers == "PEOPLE":
                self.station_gp.add_car(car)
            else:
                self.station_gr.add_car(car)
        else:  # ELECTRIC
            if car.passengers == "PEOPLE":
                self.station_ep.add_car(car)
            else:
                self.station_er.add_car(car)

    def process_all(self):
        self.station_gp.serve_cars()
        self.station_gr.serve_cars()
        self.station_ep.serve_cars()
        self.station_er.serve_cars()

    def get_stats(self):
        return StatsCollector.stats