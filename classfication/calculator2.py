class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 더하기
    def add(self):
        return self.x + self.y

    # 빼기
    def sub(self):
        return self.x - self.y

    # 곱하기
    def mul(self):
        return self.x * self.y

    # 나누기
    def div(self):
        return self.x / self.y
