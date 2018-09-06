import typing as t

from abc import ABC, abstractmethod

from sevenwonders.resources import resource
from sevenwonders.utilities.containers import HashableMultiset



class CostAtom(ABC):

	@abstractmethod
	def requirement(self) -> t.Optional[resource.Resource]:
		pass

	@abstractmethod
	def pay(self) -> None:
		pass

	@abstractmethod
	def __hash__(self):
		pass

	@abstractmethod
	def __eq__(self, other):
		pass


class ResourceCostAtom(CostAtom):

	def __init__(self, price: resource.Resource):
		self._resource = price

	def requirement(self) -> t.Optional[resource.Resource]:
		return self._resource

	def pay(self) -> None:
		return None

	def __hash__(self):
		return hash(self._resource)

	def __eq__(self, other):
		return (
			isinstance(other, self.__class__)
			and self._resource == other._resource
		)


class CoinCostAtom(CostAtom):

	def requirement(self) -> t.Optional[resource.Resource]:
		return None

	def pay(self) -> None:
		return None

	def __hash__(self):
		return hash(self.__class__)

	def __eq__(self, other):
		return (
			isinstance(other, self.__class__)
		)


class Cost(object):

	def __init__(self, atoms: t.Iterable[CostAtom]):
		self._atoms = HashableMultiset(atoms)

	def __hash__(self):
		return hash(self._atoms)

	def __eq__(self, other):
		return (
			isinstance(other, self.__class__)
			and self._atoms == other._atoms
		)