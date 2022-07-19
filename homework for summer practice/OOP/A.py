class Balance():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0


    def add_right(self, x):
        self.x += x
    
    
    def add_left(self, y):
        self.y += y


    def result(self):
        if(self.x > self.y):
            return "R"
        elif(self.y > self.x):
            return "L"
        else:
            return "="

    
def main():

    balance = Balance()
    balance.add_right(10)
    balance.add_left(9)
    balance.add_left(2)
    print(balance.result())


main()