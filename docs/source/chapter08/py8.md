# 8.8 判断
>条件判断也是编程中非常重要的内容，一般编程语言中都使用if条件语句，python中也是一样。if语句的格式是if然后接条件判断，条件判断的值为逻辑值是或者否，然后决定接下来如何处理。在python中if 条件语句不需要加括号，后面同样接冒号。
这个条件可以判断是否等于，大于或者小于，是否存在，是否匹配等等。一般循环和判断一起使用。

## if-else结构
```python
# if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")

# if else结构
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 判断完进行处理
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

## if-elif-else结构
如果有两个以上条件，可以使用if-elif-else结构。注意这里的elif，表示else if，但是写成elif，不能书写错误。
```python
#判断
i=6
if i <5:
    print ("i is less than 5!")
elif(i==5):
    print ("i is equal to 5!")
else:
    print ("i is more than 5!")
```

## 循环+判断

### 循环控制
如果不想让循环全部结束，可以加入循环控制，在python中，可以在循环中加入break终止循环，continue继续执行循环。
```python
# break终止循环
for i in range(10):
    if i == 7:
        break
    print("The Number is :" , i)

#continue 跳过循环
for i in range(10):
    if i == 7:
        continue
    print("The Number is :" , i)

#挑选奇数
i = 0

while i < 10:
    i += 1
    if i %2 ==0:
        continue
    print(i)
```