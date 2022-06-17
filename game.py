import random


class Game:

    def __init__(self):
        self._board = {}
        for i in range(1, 10):
            self._board[i] = '_'
        self._game_mode = 0
        self._winner = None
        self._players = {}
        self.player1 = None
        self.player2 = None
        self._current_user = None
        self._charsXO = ['X', 'O']
        self._winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                                      [1, 4, 7], [2, 5, 8], [3, 6, 9],
                                      [1, 5, 9], [3, 5, 7]]

    def start(self):
        self._set_game_mode()
        self._set_players()

        print('\nTic Tac Toe is started!\n')
        self.game_process()

    def _set_game_mode(self):
        while not self._game_mode:
            select = input('Select game mode:\n 1 - Player vs Player mode\n 2 - Player vs PC'
                           ' \n 3 - PC vs PC\n'
                           'or type "e" to exit game: \n').lower()
            if select == 'e' or select == 'exit':
                exit()
            try:
                int_select = int(select)
            except ValueError:
                print('Int input is required. Try again.')
                continue
            if int_select not in [1, 2, 3]:
                print('Only 1, 2, 3 are available. Try again.')
                continue
            self._game_mode = int_select

    def _set_players(self):
        if self._game_mode == 1:
            self.player1 = 'Player 1'
            self.player2 = 'Player 2'
        elif self._game_mode == 2:
            self.player1 = 'Player'
            self.player2 = 'PC'
        else:
            self.player1 = 'PC 1'
            self.player2 = 'PC 2'

        self._set_players_chars()

        print(f'{self.player1} plays with "{self._players[self.player1]}"')
        print(f'{self.player2} plays with "{self._players[self.player2]}"')

    def _select_character(self):
        while True:
            char_input = input(f'So, {self.player1}, what character do you want to play? Type:\n"1" for play with "X"'
                               f'\n"2" for play with "O"\n'
                               '"X" starts first always. So, select: ')
            try:
                int_char_input = int(char_input)
            except ValueError:
                print('Int input is required. Try again.')
                continue
            if int_char_input not in [1, 2]:
                print('Only 1 or 2 available. Try again.')
                continue

            return self._charsXO[0] if int_char_input == 1 else self._charsXO[1]

    def change_current_user(self):
        self._current_user = self.player1 if self._current_user == self.player2 else self.player2

    def _set_players_chars(self):
        if self._game_mode == 1 or self._game_mode == 2:
            char = self._select_character()
        else:
            char = random.choice(self._charsXO)

        self._players[self.player1] = char
        self._players[self.player2] = self._charsXO[0] if char == self._charsXO[1] else self._charsXO[1]

        self._current_user = self.player1 if self._players[self.player1] == self._charsXO[0] else self.player2

    def game_process(self):
        while True:
            self.print_board()
            self._make_move()
            if self.is_game_over():
                self.print_board()
                if self._winner:
                    print(f'\nGame over. The winner is "{self._current_user}"')
                else:
                    print('Game over! It\'s draw!')
                break
            self.change_current_user()

    def is_game_over(self):
        board = self._board
        for comb in self._winning_combinations:
            if board[comb[0]] == board[comb[1]] == board[comb[2]] == self._charsXO[0]:
                self._winner = self._charsXO[0]
                return True
            elif board[comb[0]] == board[comb[1]] == board[comb[2]] == self._charsXO[1]:
                self._winner = self._charsXO[1]
                return True

        free_cells = [k for k, v in board.items() if v == '_']
        if not free_cells:
            return True

        return False

    def _make_move(self):
        if self._current_user.rfind('PC') == -1:
            self._user_move()
        else:
            self._pc_move()

    def _user_move(self):
        while True:
            turn_input = input(f'{self._current_user}, please select cell index to fill [1,2...9]: ')
            try:
                turn = int(turn_input)
            except ValueError:
                print('Int input is required. Try again.')
                continue
            if self._board[turn] == '_':
                self._board[turn] = self._players[self._current_user]
                return True
            else:
                print('This cell is unavailable. Try another')
                continue

    def _pc_move(self):
        left = [k for k, v in self._board.items() if v == '_']
        if left:
            self._board[random.choice(left)] = self._players[self._current_user]
            print(f'{self._current_user} has moved.')

    def print_board(self):
        desk = ""
        for k, v in self._board.items():
            if k % 3 == 0:
                desk += v + '\n'
            else:
                desk += v + '|'
        print(desk[:-1])


game = Game()
game.start()
