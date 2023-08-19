class NoUserFound(Exception):
    def __init__(self, message="No user found"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Failed while fetched users'
