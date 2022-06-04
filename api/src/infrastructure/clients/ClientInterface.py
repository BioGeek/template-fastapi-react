from abc import abstractmethod
from typing import Dict, Generic, List, TypeVar

# Type definition for Model
M = TypeVar("M")

# Type definition for Unique Id
K = TypeVar("K")


class ClientInterface(Generic[M, K]):

    # Create a new instance of the Model
    @abstractmethod
    def create(self, instance: M) -> M:
        pass

    # Delete an existing instance of the Model
    @abstractmethod
    def delete(self, id: K) -> None:
        pass

    # Fetch an existing instance of the Model by it's unique Id
    @abstractmethod
    def find_by_id(self, id: K) -> M:
        pass

    @abstractmethod
    def find_by_filter(self, filter, projection) -> M:
        pass

    # Lists all existing instance of the Model
    @abstractmethod
    def list(self, limit: int, start: int) -> List[M]:
        pass

    # Updates an existing instance of the Model
    @abstractmethod
    def update(self, id: K, instance: M) -> M:
        pass

    @abstractmethod
    def get_all(self) -> List[M]:
        pass
