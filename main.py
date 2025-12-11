import json
import os
from app.dispatcher import Dispatcher
from app.components import StatsCollector

INPUT_FILE = "cars.json"


def main():
    StatsCollector.reset()

    dispatcher = Dispatcher()

    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found. Please run generator.py first.")
        return

    dispatcher.load_cars(INPUT_FILE)
    dispatcher.process_all()

    print(json.dumps(dispatcher.get_stats(), indent=4))


if __name__ == "__main__":
    main()