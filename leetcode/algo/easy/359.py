class Logger:

    def __init__(self):
        self.mp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mp:
            self.mp[message] = timestamp
            return True
        prev = self.mp[message]
        if timestamp-prev>=10:
            self.mp[message] = timestamp
            return True
        return False
