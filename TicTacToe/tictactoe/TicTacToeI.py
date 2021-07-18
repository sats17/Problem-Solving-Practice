class TicTacToeI:
    __values = {'x': 0, 'o': 1}

    def __init__(self, size: int) -> bool:
        """Initialize board with size"""
        pass

    def capture_move(self, index: str, value: str) -> object:
        """Capture move from user and put into board"""
        pass

    def get_values(self):
        return self.__values
