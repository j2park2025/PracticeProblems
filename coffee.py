class Coffee:
    def __init__(self, name, price, HotOrCold, left):
        self.name=name
        self.price=price
        self.HotOrCold=HotOrCold
        self.left=left
        
    def drink(self, drank):
        self.drank=drank
        self.left=self.left-self.drank
        return self.left
    def print(self):
        return self.name, self.price, self.HotOrCold, self.left
    def getPrice(self):
        return self.price
    def getName(self):
        return self.name

class Customer:
    def __init__(self, money):
        self.money=money
        self.mycoffee = None
    def buyProduct(self, coffee):
        self.mycoffee = coffee
        self.money=self.money-coffee.getPrice()
        return self.money
    def eatProduct(self, amount):
        if self.mycoffee == None:
            print("No available coffee")
            return 
        self.mycoffee.drink(amount)

coffeeA = Coffee('아메리카노', 1700, 'C', 250)
coffeeL = Coffee('카페라떼', 2100, 'H', 250)
coffeeM = Coffee('카페모카', 2300, 'H', 250)
coffeeC = Coffee('카라멜마끼야또', 2300, 'C', 250)

customer = Customer(10000)

# print(coffeeA, coffeeL, coffeeM, coffeeC)
# customer.eatProduct(50)
# customer.buyProduct(coffeeM)
# print(customer.money, customer.mycoffee.getName())
# # print(c, "을/를 구매하였습니다. 남은돈: ", buyProduct())

an=1
cof = [coffeeA, coffeeL, coffeeC, coffeeM]

while(an!=0):
    an = int(input("1 : 커피구매 / 2 : 커피섭취 / 0 : 종료"))
    if an==1:
        if customer.money<=0:
            print("No left money")
            break
        print("1 : ", Coffee.print(coffeeA), "2 : ", Coffee.print(coffeeL), "3 : ", Coffee.print(coffeeM), "4 : ", Coffee.print(coffeeC))
        buy = int(input(""))
        if buy==1:
            customer.buyProduct(coffeeA)
            if customer.money<0:
                print("돈이 부족합니다.")
                break
            print(Coffee.getName(coffeeA), "을/를 구매하였습니다. 남은돈: ", customer.money)
        elif buy==2:
            customer.buyProduct(coffeeL)
            if customer.money<0:
                print("돈이 부족합니다.")
                break
            print(Coffee.getName(coffeeL), "을/를 구매하였습니다. 남은돈: ", customer.money)
        elif buy==3:
            customer.buyProduct(coffeeM)
            if customer.money<0:
                break
            print(Coffee.getName(coffeeM), "을/를 구매하였습니다. 남은돈: ", customer.money)
        elif buy==4:
            customer.buyProduct(coffeeC)
            if customer.money<0:
                print("돈이 부족합니다.")
                break
            print(Coffee.getName(coffeeC), "을/를 구매하였습니다. 남은돈: ", customer.money)
        else:
            print("Wrong Number")
    elif an==2:
        if customer.mycoffee==None:
            print("No Coffee bought")
        else:
            amo = int(input("How much would you like to drink?"))
            while amo>customer.mycoffee.left or amo<0:
                print("Please enter a positive number below", customer.mycoffee.left)
                amo = int(input("How much would you like to drink?"))
            customer.eatProduct(amo)
            print(Coffee.getName(customer.mycoffee), "을/를 ", amo, "ml만큼 마셨습니다. 남은용량: ", customer.mycoffee.left)
    elif an==0:
        break