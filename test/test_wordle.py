import unittest
from parameterized import parameterized

from src.wordle import tally, play
from src.match import Match
from src.game_status import GameStatus
from src.play_result import PlayResult

[NO, EXACT, PARTIAL] = Match


class WordleTests(unittest.TestCase):

    def test_canary(self):
        self.assertTrue(True)

    @parameterized.expand(
        [
            ("FAVOR", "FAVOR", [EXACT] * 5),
            ("FAVOR", "TESTS", [NO, NO, NO, NO, NO]),
            ("FAVOR", "RAPID", [PARTIAL, EXACT, NO, NO, NO]),
            ("FAVOR", "MAYOR", [NO, EXACT, NO, EXACT, EXACT]),
            ("FAVOR", "RIVER", [NO, NO, EXACT, NO, EXACT]),
            ("FAVOR", "AMAST", [PARTIAL, NO, NO, NO, NO]),
            ("SKILL", "SKILL", [EXACT] * 5),
            ("SKILL", "SWIRL", [EXACT, NO, EXACT, NO, EXACT]),
            ("SKILL", "CIVIL", [NO, PARTIAL, NO, NO, EXACT]),
            ("SKILL", "SHIMS", [EXACT, NO, EXACT, NO, NO]),
            ("SKILL", "SILLY", [EXACT, PARTIAL, PARTIAL, EXACT, NO]),
            ("SKILL", "SLICE", [EXACT, PARTIAL, EXACT, NO, NO]),
        ]
    )
    def test_tally_for_target_and_guess(self, target, guess, expected_result):
        result = tally(target, guess)

        self.assertEqual(result, expected_result)

    def test_play_first_attempt_with_winning_guess(self):
        expected_play_result = PlayResult(
            status = GameStatus.WON,
            message = "Amazing",
            attempts = 2,
            tally_response = [EXACT] * 5,
        )

        play_result = play(1, "FAVOR", "FAVOR")
        
        self.assertEqual(play_result, expected_play_result)


    def test_play_first_attempt_with_non_winning_guess(self):
        expected_play_result = PlayResult(
            status = GameStatus.IN_PROGRESS,
            message = "",
            attempts = 2,
            tally_response = [NO, NO, EXACT, NO, EXACT],
        )

        play_result = play(1, "FAVOR", "RIVER")

        self.assertEqual(play_result, expected_play_result)
    
    def test_play_second_attempt_with_winning_guess(self):
        expected_play_result = PlayResult(
            status = GameStatus.WON,
            message = "Splendid",
            attempts = 3,
            tally_response = [EXACT] * 5,
        )

        play_result = play(2, "FAVOR", "FAVOR")

        self.assertEqual(play_result, expected_play_result)

    
    def test_play_second_attempt_with_non_winning_guess(self):
        expected_play_result = PlayResult(
            status = GameStatus.IN_PROGRESS,
            message = "",
            attempts = 3,
            tally_response = [NO, NO, EXACT, NO, EXACT],
        )

        play_result = play(2, "FAVOR", "RIVER")

        self.assertEqual(play_result, expected_play_result)
    

if __name__ == "__main__":
    unittest.main()
