class BadConfigirationError(Exception):
    def __init__(self, info:str) -> None:
        self.info = info
        super().__init__()

