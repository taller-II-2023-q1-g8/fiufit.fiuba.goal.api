"""Goal repository interface."""
from abc import abstractmethod


class IRepository:
    @abstractmethod
    def load_by_id(self, object_id: str) -> list[dict]:
        """Returns an object by id."""
        raise NotImplementedError

    @abstractmethod
    def load_all(self) -> list[dict]:
        """Returns all objects."""
        raise NotImplementedError

    @abstractmethod
    def create(self, goal_dict: dict) -> str:
        """Creates an object and returns its id."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, object_id: str):
        """Deletes an object."""
        raise NotImplementedError
