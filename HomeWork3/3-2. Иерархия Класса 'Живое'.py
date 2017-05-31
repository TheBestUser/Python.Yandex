class Animalia(object):
    def __init__(self):
        print("Animalia", end='')


class Chordata(Animalia):
    def __init__(self):
        super().__init__()
        print(" -> Chordata", end='')


class Aves(Chordata):
    def __init__(self):
        super().__init__()
        print(" -> Aves", end='')


class Passeriformes(Aves):
    def __init__(self):
        super().__init__()
        print(" -> Passeriformes", end='')


class Hirundinidae(Passeriformes):
    def __init__(self):
        super().__init__()
        print(" -> Hirundinidae", end='')


class Hirundo(Hirundinidae):
    def __init__(self):
        super().__init__()
        print(" -> Hirundo", end='')


class Hirundo_Rustica(Hirundo):
    def __init__(self):
        super().__init__()
        print(" -> Hirundo Rustica", end='')


a = Hirundo_Rustica()
