from abc import ABC, abstractmethod

from lineapy.data.graph import Graph
from lineapy.db.asset_manager.base import DataAssetManager


class GraphReader(ABC):
    """
    Base class for anything that only involves reading the graph
    without writing anything back to the DB.

    TODO
    """

    @abstractmethod
    def walk(self, graph: Graph) -> None:
        pass

    @abstractmethod
    def validate(self, graph: Graph) -> None:
        """
        TODO
        Things to check for:
        - Loops are first entered and then exit.
        """
        pass

    @property
    def data_asset_manager(self) -> DataAssetManager:
        pass