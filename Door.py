class Door(object):
    colour = 'brown'

    def __init__(self, number, status):
        self.number = number
        self.status = status

    @classmethod
    def knock(cls):
        print "Knock!"

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'


class SecurityDoor(object):
    locked = True

    def __init__(self, number, status):
        self.door = Door(number, status)

    def open(self):
        if self.locked:
            return
        self.door.open()

    def __getattr__(self, attr):
        return getattr(self.door, attr)

class ComposedDoor(object):
    def __init__(self, number, status):
        self.door = Door(number, status)

    def __getattr__(self, attr):
        return getattr(self.door, attr)
