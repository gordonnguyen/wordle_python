from src.match import Match
from src.game_status import GameStatus
from src.play_result import PlayResult


def tally_for_position(target, guess, position):
    def count_occurrences_until_position(word, letter, position):
        return word[:position].count(letter)
    
    def count_positional_matches(target, guess, letter):
        return len(
            list(
                filter(
                    lambda index: target[index] == letter and target[index] == guess[index],
                    range(0, len(target))
                )
            )
        )

    if target[position] == guess[position]:
        return Match.EXACT

    letter = guess[position]

    positional_matches = count_positional_matches(target, guess, letter)

    non_positional_occurrences_in_target = (
        count_occurrences_until_position(target, letter, len(target))
        - positional_matches
    )

    number_of_occurrences_in_guess_until_position = count_occurrences_until_position(
        guess, letter, position
    )

    if non_positional_occurrences_in_target > number_of_occurrences_in_guess_until_position:
        return Match.PARTIAL

    return Match.NO


def tally(target, guess):
    return list(
        map(
            lambda position: tally_for_position(target, guess, position),
            range(len(target))
        )
    )

def play(number_of_attempts, target, guess):
    win_msg_list = ["Amazing", "Splendid"]

    play_result = PlayResult(
        attempts = number_of_attempts + 1, tally_response = tally(target, guess)
    )

    if target == guess:
        play_result.status = GameStatus.WON
        play_result.message = win_msg_list[number_of_attempts-1]
    
    else:
        play_result.status = GameStatus.IN_PROGRESS

    return play_result
