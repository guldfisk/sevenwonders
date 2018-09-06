from abc import ABC
from functools import total_ordering


@total_ordering
class Resource(ABC):

	def __init__(self, value: int, name: str):
		self._value = value
		self._name = name

	def __hash__(self) -> int:
		return hash(self._value)

	def __eq__(self, other) -> bool:
		return (
			isinstance(other, self.__class__)
			and self._value == other._value
		)

	def __lt__(self, other) -> bool:
		return self._value < other._value

	def __str__(self) -> str:
		return self._name


class NaturalResource(Resource):
	pass


class ProcessedResource(Resource):
	pass


LUMBER = NaturalResource(0, 'Lumber')
STONE = NaturalResource(1, 'Stone')
CLAY = NaturalResource(2, 'Clay')
ORE = NaturalResource(3, 'Ore')

CLOTH = ProcessedResource(4, 'Cloth')
GLASS = ProcessedResource(5, 'Glass')
PAPER = ProcessedResource(6, 'Paper')