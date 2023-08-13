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
car1 = Car('bmw', 'white')
print(car1.color)
car2 = Car('kia', 'blue')
print(Car.count)

class Employee:
    count=0
    def __init__(self, name, age, posit, salary):
        self.name=name
        self.age=age
        self.posit=posit
        self.salary=salary
    def change_age(self, new_age):
        self.age = new_age
    def change_sal(self, newSal):
        self.salary = newSal
    def change_exi(self, exi):
        self.name=exi
        self.age=exi
        self.posit=exi
        self.salary=exi

emp1 = Employee('장그래', '26', '사원', '3000')
emp1.change_sal('3300')
emp2 = Employee('오상식', '43', '과장', '4500')
emp3 = Employee('안영이', '26', '사원', '3000')  
emp4 = Employee('장백기', '26', '사원', '3000')
emp5 = Employee('김동식', '32', '대리', '3500')
emp5.change_age('34')
'''

# attributes: width, height
# method: area, perimeter 
class Rectangle:
    def __init__(self , width, height):
        self.width=width
        self.height=height
    def area(self):
        self.area = self.width * self.height
        return self.area
    def perimeter(self):
        self.perimeter = (2*self.width)+(2*self.height)
        return (2*self.width)+(2*self.height)

rec1 = Rectangle('3', '4')
print(rec1.area())
print(rec1.perimeter())
rec2 = Rectangle('6', '2')
print(rec2.area())
print(rec2.perimeter())
