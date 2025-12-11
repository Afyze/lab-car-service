import unittest
from app.components import ListQueue, GasStation, StatsCollector
from app.models import Car


class TestCarService(unittest.TestCase):

    def setUp(self):
        StatsCollector.reset()

    def test_queue_operations(self):
        q = ListQueue()
        self.assertTrue(q.is_empty())

        q.enqueue(1)
        q.enqueue(2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)

    def test_gas_station_stats(self):
        station = GasStation()
        car = Car(1, "GAS", "PEOPLE", False, 30)

        station.refuel(car)

        self.assertEqual(StatsCollector.stats["GAS"], 1)
        self.assertEqual(StatsCollector.stats["CONSUMPTION"]["GAS"], 30)

    def test_wrong_fuel_type(self):
        station = GasStation()
        electric_car = Car(2, "ELECTRIC", "ROBOTS", False, 20)

        with self.assertRaises(ValueError):
            station.refuel(electric_car)


if __name__ == '__main__':
    unittest.main()