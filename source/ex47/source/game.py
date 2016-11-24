"""
Example gaming module
doc tests examples:
>>> Room('gold', 'golden room').name
'gold'

>>> Room('silver', 'silver room').add_paths({'up': 'up'}).go('up')
'up'
"""


class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
        return self

if __name__ == "__main__":
    import doctest
    doctest.testmod()
