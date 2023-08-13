vegetable = ["tomato", "cabbage", "carrot", "onion", "spinach"]
print(len(vegetable))

numbers = [293, 102, 38, 293, 300, 391, 48, 21]
print(max(numbers))

numbers = [293, 102, 38, 293, 300, 391, 48, 21]
print(min(numbers))

vegetable = ["tomato", "cabbage", "carrot", "onion", "spinach"]
print(max(vegetable))
print(min(vegetable))
#알파벳 순서대로(a 가 제일 작은 min, z가 제일 큰 max)

numbers = [293, 102, 38, 293, 300, 391, 48, 21]
print(sum(numbers))

numbers = [293, 102, 38, 293, 300, 391, 48, 21]
print(sum(numbers)/len(numbers))
#Getting the average of the list

numbers = [293, 102, 38, 293, 300, 391, 48, 21]
#오름차순 정렬
numbers.sort()
#sort()함수는 numbers = numbers.sort() 쓰면 X
print(numbers)

#내림차순 정렬
numbers.sort(reverse=True)
print(numbers)

numbers = [300, 102, 38, 293, 300, 391, 300, 21]
print(numbers.count(300))

a = numbers.count(300)  
#300이 리스트에 count how many are there

#1 
grades = [92, 83, 75, 40, 73, 69, 39, 50, 38, 90, 99, 59, 30]
topf = []
while(len(topf)<5):
    topf.append(max(grades))
    grades.remove(max(grades))
print(topf)
print(sum(topf)/len(topf))
#99, 92, 90, 83, 75

#1-1
grades = [92, 83, 75, 40, 73, 69, 39, 50, 38, 90, 99, 59, 30]
topf = []
grades.sort(reverse=True)
for i in range(5):
    topf.append(grades[i])
print(topf)
print(sum(topf)/len(topf))

#2
l1 = [5, 9, 20, 30, 3, 49]
l2 = [20, 30]
for i in range(2):
    l1.remove(l2[i])
print(l1)
print(sum(l1)/len(l1))

#3
numbers = [300, 102, 38, 293, 300, 391, 300, 21]
a = numbers.count(300) 
for i in range(a):
    numbers.remove(300)
print(numbers)

#4
numbers = [300, 102, 38, 293, 300, 391, 300, 21]
value = []
for i in range(8):
    if(numbers[i] == 300):
        value.append(i)
print(value)