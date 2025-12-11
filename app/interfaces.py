from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any

T = TypeVar('T')

class Queue(ABC, Generic[T]):
    @abstractmethod
    def enqueue(self, item: T) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

class Refuelable(ABC):
    @abstractmethod
    def refuel(self, car: Any) -> None:
        pass

class Dineable(ABC):
    @abstractmethod
    def serve_dinner(self, car: Any) -> None:
        pass