from Trokut import Trokut

class JednakokracniTrokut(Trokut):

    def __init__(self, db, dk):
        Trokut.__init__(self, db, dk, dk)