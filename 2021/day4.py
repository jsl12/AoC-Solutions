from rich import print

from bingo import BingoGame


def part1(inp):
    game = BingoGame.from_str(inp)
    winning_num, winner = next(game.play_game())
    print(winner)
    return winner.total() * winning_num


def part2(inp):
    game = BingoGame.from_str(inp)
    print(f'{len(game.boards)}')
    winners = list(game.play_game())
    print(f'{len(winners)} winning boards')
    last_num, last_winner = winners[-1]
    print(last_num * last_winner.total())


if __name__ == '__main__':
    from aoc_input import read

    print(part1(read(4)))
    print(part2(read(4)))
