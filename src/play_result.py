from dataclasses import dataclass, field
from src.game_status import GameStatus
from src.match import Match

@dataclass
class PlayResult:
    status: GameStatus = GameStatus.IN_PROGRESS
    message: str = ""
    attempts: int = 0
    tally_response: list[Match] = field(default_factory=list)
