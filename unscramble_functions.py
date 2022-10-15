"""CSC108/A08: Fall 2021 -- Assignment 1: unscramble

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michelle Craig, Anya Tafliovich.

"""

# Valid moves in the game.
SHIFT = 'S'
SWAP = 'W'
CHECK = 'C'


# We provide a full solution to this function as an example.
def is_valid_move(move: str) -> bool:
    """Return True if and only if move is a valid move. Valid moves are
    SHIFT, SWAP, and CHECK.

    >>> is_valid_move('C')
    True
    >>> is_valid_move('S')
    True
    >>> is_valid_move('W')
    True
    >>> is_valid_move('R')
    False
    >>> is_valid_move('')
    False
    >>> is_valid_move('NOT')
    False

    """

    return move == CHECK or move == SHIFT or move == SWAP

def get_section_start(section_number: int, section_length: int) -> int:
    """Return the index number of the first character of the specified section
    section_number given its section length section_length.

    precondition: section_number and section_length >= 1

    >>> get_section_start(2, 4)
    4
    >>> get_section_start(3, 3)
    6
    >>> get_section_start(10, 2)
    18
    >>> get_section_start(1, 4)
    0
    """
    return (section_number - 1) * section_length

def get_section(game_state: str, section_number: int,
                section_length: int) -> str:
    """Return the section of the state game_state that corresponds to the given
    section section_number with its length section_length.

    preconditions: section_number and section_length are valid for
    the given game_state

    >>> get_section('apples', 2, 2)
    'pl'
    >>> get_section('lives2laugh4', 2, 3)
    'es2'
    >>> get_section('I luv candy!', 1, 3)
    'I l'
    >>> get_section('Carpool?', 2, 4)
    'ool?'
    """

    index_number = (section_number - 1) * section_length
    return game_state[index_number:index_number + section_length]

def is_valid_section(game_state: str, section_number: int,
                     section_length: int) -> bool:
    """Return whether or not the the length of the section section_length and
    number of the section section_number are valid for the state string
    game_state.

    precondition: section_number >= 1 and section_length > 1

    >>> is_valid_section('cats4Ever', 3, 3)
    True
    >>> is_valid_section('cardioLOVER', 7, 2)
    False
    >>> is_valid_section('Happy Day!', 5, 3)
    False
    >>> is_valid_section('', 1, 2)
    False
    """
    return len(game_state) % section_length == 0 and (
        len(game_state) / section_length >= section_number)

def swap(game_state: str, start_index: int, end_index: int) -> str:
    """Return the state game_state having swapped the start index (inclusive)
    start_index and the end index (exclusive) end_index.

    percondition: start_index and end_index are valid for the game_state and
    start_index < end_index - 1

    >>> swap('discombobulated', 0, 7)
    'biscomdobulated'
    >>> swap('dogs', 1, 4)
    'dsgo'
    >>> swap('bAby uR on fire!', 4, 16)
    'bAby!uR on fire '
    >>> swap('dsgo', 2, 4)
    'dsog'
    """
    return (game_state[:start_index] + game_state[end_index - 1] +
            game_state[start_index + 1:end_index - 1] + game_state[start_index]
            + game_state[end_index:])

def shift(game_state: str, start_index: int, end_index: int) -> str:
    """Return the state game_state having shifted the characters between the
    start index start_index and the end index end_index.

    precondition: start_index and end_index are valid for the game_state and
    start_index < end_index - 1

    >>> shift('amazingly', 0, 9)
    'mazinglya'
    >>> shift('saturday', 1, 6)
    'sturdaay'
    >>> shift('computerscience', 6, 10)
    'computrsceience'
    """
    return (game_state[:start_index] + game_state[start_index + 1:end_index] +
            game_state[start_index] + game_state[end_index:])

def check(game_state: str, start_index: int, end_index: int,
          answer: str) -> bool:
    """Return True iff the part of the state game_state between the start index
    start_index (inclusive) and end index end_index (exclusive) is identical to
    the same section of answer.

    precondition: start_index and end_index are valid for the game_state,
    meaning that start_index <= end_index and answer is a valid answer for
    game_state.

    >>> check('ccsa80fun', 6, 9, 'csca08fun')
    True
    >>> check('ccsa80fun', 0, 3, 'csca08fun')
    False
    >>> check('computerscience', 1, 9, 'computerscience')
    True
    >>> check('cototn candy', 1, 5, 'cotton candy')
    False
    """

    return game_state[start_index:end_index] == answer[start_index:end_index]

def check_section(game_state: str, section_number: int, section_length: int,
                  answer: str) -> bool:
    """ Return True iff the section of state game_state with section number
    section_number and length section_length is identical to the same section
    in answer.

    precondition: section_number and section_length are valid for game_state and
    answer is valid for game_state

    >>> check_section('ccsa80fun', 3, 3, 'csca08fun')
    True
    >>> check_section('ccsa80fun', 1, 3, 'csca08fun')
    False
    >>> check_section('mubrell!a', 2, 3, 'umbrella!')
    True
    >>> check_section('mubrell!a', 1, 3, 'umbrella!')
    False
    """

    return (get_section(game_state, section_number, section_length) ==
            get_section(answer, section_number, section_length))

def change_section(game_state: str, move: str, section_number: int,
                   section_length: int) -> str:
    """Return a new state after applying a move, SHIFT or SWAP, to game_state
    with its given section section_number and length section_length

    precondition: move == SWAP or move == SHIFT, and section_number and
    section_length are valid for game_state

    >>> change_section('computerscience', 'W', 2, 5)
    'compucerstience'
    >>> change_section('standup2k0', 'S', 1, 5)
    'tandsup2k0'
    >>> change_section('computerscience', SHIFT, 1, 5)
    'ompucterscience'
    >>> change_section('tuesday!', SWAP, 1, 4)
    'suetday!'
    """

    if move == SWAP:
        return swap(game_state, get_section_start(section_number,
                                                  section_length),
                    get_section_start(section_number + 1, section_length))
    return shift(game_state, get_section_start(section_number, section_length),
                 get_section_start(section_number + 1, section_length))

def get_move_hint(game_state: str, section_number: int, section_length: int,
                  answer: str) -> str:
    """Return a suggestion move SHIFT if shifting the specified section of state
    game_state once or twice with will match the answer with the same section
    section_number and section_length. Otherwise return SWAP.

    Precondition: section_number and section_length are valid for game_state.
    the answer is valid for game_state

    >>> get_move_hint('TCADOGFOXEMU', 1, 3, 'CATDGOXOFEMU')
    'S'
    >>> get_move_hint('TACDOGFOXEMU', 1, 3, 'CATDOGXOFEMU')
    'W'
    >>> get_move_hint('cortxe', 1, 3, 'cortex')
    'W'
    >>> get_move_hint('abanan', 2, 2, 'banana')
    'S'
    """
    first_shift = change_section(game_state, 'S', section_number,
                                 section_length)
    second_shift = change_section(first_shift, 'S', section_number,
                                  section_length)
    if check_section(first_shift, section_number, section_length, answer) or \
       check_section(second_shift, section_number, section_length, answer):
        return SHIFT
    return SWAP

if __name__ == '__main__':
    import doctest
    doctest.testmod()
