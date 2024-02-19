# 8.9 循环+判断案例

> 单独的判断语句使用的不多，一般都是与循环结合起来，才能实现更强大的功能。


## 案例一:循环加判断
```python
# 案例一:循环加判断
for i in range(0,10):
    if i <5:
        print (i,"less")
    elif (i==5):
        print (i,"equal")
    else:
       print (i,"more")
```

## 案例二：计算数字值
```python
alist = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E', 6, 'F', 7, 'G']

total_number = 0
for i in alist:
   if str(i).isnumeric():
       total_number += i

print(total_number)
```

## 案例三：判断是否存在
```python
#判断是否存在
moto_brands = ['bmw', 'benz', 'audi', 'byd', 'toyota', 'volvo','honda', 'ford', 'bentley', 'chery', 'gwm', 'nissan']
luxury_brands = ['rolls-royce', 'bentley', 'benz', 'bmw', 'audi', 'volvo']

for i in moto_brands:
    if i in luxury_brands:
        print(f'{i} is a luxury car brands')

# 去除大小写的影响
moto_brands = ['BMW', 'Benz', 'Audi', 'BYD', 'Toyota', 'Volvo','Honda', 'Ford', 'Bentley', 'Chery', 'GMW', 'nissan']
luxury_brands = ['rolls-royce', 'bentley', 'benz', 'bmw', 'audi', 'volvo']

for i in moto_brands:
    for j in luxury_brands:
        if i.lower() == j.lower():
            print(f'{i} is a luxury car brands')
```
**方法二，提前修改数组**
```python
moto_brands = ['BMW', 'Benz', 'Audi', 'BYD', 'Toyota', 'Volvo','Honda', 'Ford', 'Bentley', 'Chery', 'GMW', 'nissan']
luxury_brands = ['rolls-royce', 'bentley', 'benz', 'bmw', 'audi', 'volvo']

moto_brands = [i.lower() for i in moto_brands]
luxury_brands = [i.lower() for i in luxury_brands]

for i in moto_brands:
    if i in luxury_brands:
        print(f'{i} is a luxury car brands')
```   
**获取用户输入**
```python
luxury_brands = ['rolls-royce', 'bentley', 'benz', 'bmw', 'audi', 'volvo']
luxury_brands = [i.lower() for i in luxury_brands]

print(f"Please Enter a Car Brand:")
my_input = input()
if my_input.lower() in luxury_brands:
    print(f'{my_input} is a luxury car brands')
else:
    print(f'{my_input} is not a luxury car brands')
```