from abc import ABC, abstractmethod

class ServiceAble(ABC):
    @abstractmethod
    def needs_service(self):
        pass