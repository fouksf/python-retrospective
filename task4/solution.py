class TicTacToeBoard:

    def __init__(self):
        self.board = {"A1": " ", "A2": " ", "A3": " ",
                      "B1": " ", "B2": " ", "B3": " ",
                      "C1": " ", "C2": " ", "C3": " "}
        self.status = "Game in progress."
        self.last_played = None
        self.winner = None

    def __getitem__(self, key):
        if key not in self.board:
            raise InvalidKey("There is no such field.")
        return self.board[key]

    def __setitem__(self, key, value):
        if value != "X" and value != "O":
            raise InvalidValue("This is not a proper mark")
        if key not in self.board:
            raise InvalidKey("There is no such field.")
        if self.board[key] != " ":
            raise InvalidMove("This field is already filled.")
        if value == self.last_played:
            raise NotYourTurn("The other player hasn't made his move yet")
        self.last_played = value
        self.board[key] = value
        self.check_status()

    def check_status(self):
        if self.winner:
            return
        lines = list(map(lambda x: x[1], sorted(self.board.items())))
        lines = (lines[:3] + lines[3:6] + lines[6:9] +
                 lines[::3] + lines[1::3] + lines[2::3])
        for i, v in enumerate(lines):
            if i % 3 == 0 and i < 18:
                if lines[i] == lines[i + 1] == lines[i + 2] != " ":
                    self.winner = v
        if self.winner:
            self.status = self.winner + " wins!"
        if " " not in self.board.values() and not self.winner:
            self.status = "Draw!"
            self.winner = "Draw"

    def __str__(self):
        return ("\n  -------------\n"
                "3 | {0[A3]} | {0[B3]} | {0[C3]} |\n"
                "  -------------\n"
                "2 | {0[A2]} | {0[B2]} | {0[C2]} |\n"
                "  -------------\n"
                "1 | {0[A1]} | {0[B1]} | {0[C1]} |\n"
                "  -------------\n"
                "    A   B   C  \n").format(self.board)

    def game_status(self):
        return self.status


class TicTacToeError(Exception):
    pass


class InvalidMove(TicTacToeError):
    pass


class InvalidKey(TicTacToeError):
    pass


class InvalidValue(TicTacToeError):
    pass


class NotYourTurn(TicTacToeError):
    pass
