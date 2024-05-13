class RejectedOrder:
    def __init__(self, id, reason : str):
        self.id = id
        self.reason = reason

    def get_id(self):
        return self.id

    def get_reason(self) -> str:
        return self.reason