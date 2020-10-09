class BatailleNavaleError(Exception):
    def __init__(self, navire, msg=None):
        super().__init__()
        self.navire = navire
        self.msg = msg
