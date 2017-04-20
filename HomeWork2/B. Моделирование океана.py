HUNGER_LIMIT = 5
EXTR_REPR_LIMIT = 5
PRED_REPR_LIMIT = 5
FIELD_WIDTH = 20
FIELD_HEIGHT = 10
ITERATIONS = 3


class Cell(object):
    def __str__(self): pass

    def step(self, game, i, j): pass


class Void(Cell):
    def __str__(self):
        return ' '


class Let(Cell):
    def __str__(self):
        return '#'


def try_eat(game, i, j):
    if i > 0:
        if game.field[i - 1][j].instanse is Extraction:
            return [i - 1, j]
    if j > 0:
        if game.field[i][j - 1].instanse is Extraction:
            return [i, j - 1]
    if i < game.width - 1:
        if game.field[i + 1][j].instanse is Extraction:
            return [i + 1, j]
    if j < game.height - 1:
        if game.field[i][j + 1].instanse is Extraction:
            return [i, j + 1]
    return None


def find_void(game, i, j):
    if i > 0:
        if game.field[i - 1][j].instanse is Void:
            return [i - 1][j]
    if j > 0:
        if game.field[i][j - 1].instanse is Void:
            return [i][j - 1]
    if i < game.width - 1:
        if game.field[i + 1][j].instanse is Void:
            return [i + 1][j]
    if j < game.height - 1:
        if game.field[i][j + 1].instanse is Void:
            return [i][j + 1]
    return None


def try_repr(game, i, j):
    if i > 0:
        if game.field[i - 1][j].instanse is Predator:
            res = find_void(game, i, j)
            if res is not None:
                return res
    if j > 0:
        if game.field[i][j - 1].instanse is Predator:
            res = find_void(game, i, j)
            if res is not None:
                return res
    if i < game.width - 1:
        if game.field[i + 1][j].instanse is Predator:
            res = find_void(game, i, j)
            if res is not None:
                return res
    if j < game.height - 1:
        if game.field[i][j + 1].instanse is Predator:
            res = find_void(game, i, j)
            if res is not None:
                return res
    return None


class Predator(Cell):
    def __init__(self):
        self.hunger = 0
        self.repr = 0

    def step(self, game, i, j):
        res = try_eat(game, i, j)
        if res is not None:
            game.field[res[0]][res[1]] = Void()
            self.hunger = 0
            self.repr += 1
            return
        self.hunger += 1
        if self.hunger >= HUNGER_LIMIT:
            game.field[i][j] = Void
            return
        if self.repr >= PRED_REPR_LIMIT:
            res = try_repr(game, i, j)
            if res is not None:
                game.field[res[0]][res[1]] = Predator()
                self.hunger += 1
                self.repr = 0

    def __str__(self):
        return '®'


class Extraction(Cell):
    def __init__(self):
        self.repr = 0

    def __str__(self):
        return '*'

    def step(self, game, i, j):
        self.repr +=1
        if self.repr >= EXTR_REPR_LIMIT:
            res = try_repr(game, i, j)
            if res is not None:
                game.field[res[0]][res[1]] = Extraction()
                self.repr = 0

class Game(object):
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.field = []
        for i in range(self.height):
            self.field.append([])
            for _ in range(self.width):
                self.field[i].append(Void())
        self.field[0][0] = Predator()
        self.field[1][0] = Let()
        self.field[0][1] = Let()
        self.field[1][1] = Extraction()
        self.field[1][2] = Extraction()
        print(self)

    def __str__(self):
        field_line = ''
        for i in range(self.height):
            for j in range(self.width):
                field_line += str(self.field[i][j])
            field_line += "\n"
        return field_line

    def start(self):
        for _ in range(ITERATIONS):
            self.do_step()
            print(self)

    def do_step(self):
        for i in range(self.height):
            for j in range(self.width):
                self.field[i][j].step(self)


game = Game(FIELD_WIDTH, FIELD_HEIGHT)
game.start()
