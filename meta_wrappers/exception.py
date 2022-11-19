class APIError(Exception):
    def __init__(self, object: dict):
        super().__init__()
        self.object = object

    def __str__(self):
        return self.object.__str__()
