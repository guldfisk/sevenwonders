import typing as t

from enum import Enum

from sevenwonders.game.artifacts.artifact import GameArtifact


class CardColor(Enum):

	BROWN = 'Brown'
	GREY = 'Grey'
	BLUE = 'Blue'
	YELLOW = 'Yellow'
	GREEN = 'Green'
	RED = 'Red'
	PURPLE = 'Purple'

	WHITE = 'White'

	BLACK = 'Black'


class CardAge(Enum):
	I = 0
	II = 1
	III = 2


class Card(GameArtifact):

	def __init__(self, name: str, age: CardAge, color: CardColor):
		self._name = name
		self._age = age
		self._color = color

	@property
	def name(self) -> str:
		return self._name

	@property
	def age(self) -> CardAge:
		return self._age

	@property
	def color(self) -> CardColor:
		return self._color