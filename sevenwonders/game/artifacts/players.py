import typing as t

from sevenwonders.game.artifacts.artifact import GameArtifact
from sevenwonders.game.artifacts.wonders import Wonder
from sevenwonders.game.artifacts.cards import Card
from sevenwonders.game.artifacts.tokens import Token


class Player(GameArtifact):
	
	def __init__(self, wonder: Wonder):
		self._wonder = wonder
		
		self._cards = [] #type: t.List[Card]
		self._tokens = [] #type: t.List[Token]
		self._leaders = set() #type: t.Set[Card]

		self._coins = 0 #type: int

	@property
	def wonder(self) -> Wonder:
		return self._wonder

	@property
	def cards(self) -> t.List[Card]:
		return self._cards

	@property
	def tokens(self) -> t.List[Token]:
		return self._tokens