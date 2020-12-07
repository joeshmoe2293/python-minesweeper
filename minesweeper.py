import sys
from random import randint as rand


class MinesweeperBoard:
    def __init__(self, width, height, auto_gen=True):
        if width < 2 or height < 2:
            raise Exception('Width and Height must be > 2!')

        self.width = width
        self.height = height
        self.data = [[0 for i in range(width)] for j in range(height)] 

        if auto_gen:
            self.auto_generate()

    def auto_generate(self):
        num_spaces = self.width * self.height
        num_mines = min(self.width, self.height) + 1
        generated_positions = [(rand(0, self.width - 1), rand(0, self.height - 1)) for i in range(num_mines)]
    
        for x, y in generated_positions:
            self.set_square(x, y, -1)
            self.inc_neighbors(x, y)

    def set_square(self, x, y, val):
        self.data[y][x] = val

    def inc_neighbors(self, x, y):
        start_x = max(x - 1, 0)
        end_x = min(x + 2, self.width)
        start_y = max(y - 1, 0)
        end_y = min(y + 2, self.height)

        for row in range(start_y, end_y):
            for col in range(start_x, end_x):
                if self.data[row][col] != -1:
                    self.data[row][col] += 1

    def output_board(self):
        letters_dict = {
            1:':one:', 2:':two:', 3:':three:', 4:':four:',
            5:':five:', 6:':six:', 0:':zero:', -1:':boom:'
        }

        out_str = ''

        for row in range(self.height):
            row_str = ''

            for col in range(self.width):
                row_str += '||'
                row_str += letters_dict[self.data[row][col]]
                row_str += '||'

            out_str += row_str + '\n'

        print(out_str)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        board = MinesweeperBoard(width, height)
        board.output_board()
    else:
        print('Usage: {} <width> <height>'.format(__file__))
