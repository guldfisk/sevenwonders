import typing as t

from abc import ABC

from sevenwonders.game.costs.costs import Cost
from sevenwonders.game.artifacts.artifact import GameArtifact


class WonderStage(ABC):

	def __init__(self, cost: Cost):
		self._cost = cost

	@property
	def cost(self) -> Cost:
		return self._cost


class Wonder(GameArtifact):

	def __init__(self, name: str, stages: t.Iterable[WonderStage]):
		self._name = name
		self._stages = tuple(stages)

	@property
	def name(self) -> str:
		return self._name
