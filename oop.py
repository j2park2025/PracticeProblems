'''
class Car:
    def __init__(self, model, color): # contructor
        self.model=model
        self.color=color
    def move(self, d): # method 
        print("moved ", d, "km")
    def back(self):
        print("back")
    def get_model(self):
        return self.model
    def __del__(self):
        print(self.model, "is deleted")

car1=Car('sonata', 'black')
print(car1.model)
car1.move(10)
car2 = Car('Satafe', "white")
print(car2.color)
print(car1.get_model())

'''

class Car:
    count=0 #클래스 변수
    def __init__(self, model, color):
        self.model=model #인스턴스 변수
        self.color=color #를 self 사용하여 인스턴스에 접근한다
        Car.count+=1 #클래스명변수명
    def __del__(self):
        print("Class is deleted")
        Car.count-=1

car1 = Car('sonata', 'black')
print(Car.count)
car2 = Car('santafe', 'white')
print(Car.count)