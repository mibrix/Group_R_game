class GameAdaptor:

    def __init__(self):
        self.rules : str = "Rules: Game starts with so called initial phase..."
        self.piecesLeftPlayer1 : int = 12
        self.piecesLeftPlayer2 : int = 12
        self.representationOfBoard : dict[str, tuple[str, list[str]]]

    def notify(self, message : str):
        print(message)

    def play(self, move : str):
        True