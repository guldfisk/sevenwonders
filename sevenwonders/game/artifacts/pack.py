import typing as t

from sevenwonders.game.artifacts.artifact import GameArtifact
from sevenwonders.game.artifacts.cards import Card


class Pack(GameArtifact):

	def __init__(self, cards: t.Iterable[Card]):
		self._cards = set(cards)

	@property
	def cards(self) -> t.Set[Card]:
		return self._cards