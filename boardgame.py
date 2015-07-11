import argparse
import logging


class GameManager(object):

    def __init__(self):
        self.logger = logging.getLogger()

    def make_piece(self, id, owner):
        return Piece(id, owner)

    def place_piece_at_location(self, piece, board, x, y):
        self.logger.debug("Moving player %s's %s piece to position %s, %s",
                          piece.owner, piece.id, x, y)
        board[x][y] = piece


class GameBoard(object):

    def __init__(self, rows, cols, max_players):
        self.rows = rows
        self.cols = cols
        self.max_players = max_players

        self.logger = logging.getLogger()

        self.build_board(self.rows, self.cols)

    def __repr__(self):
        "Displays board in stdout."
        str_board = ""
        for col in self.board:
            for el in col:
                str_board += (str(el) + " ")
            str_board += "\n"

        return str_board

    def __getitem__(self, item):
        "For external indexing"
        return self.board[item]

    def build_board(self, rows, cols):
        "Builds a blank n by n board with 0s"
        self.logger.debug("Building a %sx%s board", self.rows, self.cols)
        self.board = [[0 for x in xrange(self.rows)] for y in xrange(self.cols)]


class Piece(object):

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner

        self.logger = logging.getLogger()
        self.logger.debug("Making piece %s for %s player", self.id, self.owner)

    def __repr__(self):
        "Applied color to piece based on color. Utilizes ANSI colors."

        colors = {1: "\033[0;31m",  # red
                  2: "\033[0;34m",  # blue
                  3: "\033[0;32m",  # green
                  4: "\033[0;35m",  # purple
                  "end": "\033[0m"   # returns stdout to default color
                  }
        return colors[self.owner] + str(self.id) + colors["end"]


def main(args):
    log_fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format=log_fmt)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="build a boardgame")
    parser.add_argument("--rows", type=int, help="n rows")
    parser.add_argument("--cols", type=int, help="n columns")
    parser.add_argument("--max_players", type=int,
                        help="up to four")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
