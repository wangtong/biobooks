# 8.7 循环

>循环结构重复地执行一个或一系列语句，直到某个条件不为真为止。python的循环结构包括for结构和while结构，这与其他编程语言类似。

## for循环

python的for循环非常简单，其中最重要的部分是可迭代类型，也就是in后面的部分，要想构成循环，可迭代部分不能是一个值，在python中一般是列表或者元组类型，也可以是字典，集合或者序列，总之包含多个值就行，否则只循环一次。

第二个要注意的地方是python中不使用花括号包含代码块，而是使用一个冒号`“**：**”`；

第三点要注意的地方是，下一行的语句一定要缩进，否则提示错误。

 ```python
#循环
for i in [1, 2, 3, 4]:
  print(i)

# 序列循环 
for i in 'ABCDEF':
  print(i)

for i in range(0,10):
  print (i)

 ```

 

## 批量生成脚本

 ```python

#循环

for i in ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5']:
  print(i)

 #添加更多内容

for i in ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5']:
  reads1="sample_"+ str(i) +"_1.fq.gz"
  reads2="sample_"+ str(i) +"_2.fq.gz"
  print (reads1,reads2)

fastqc='/ifs1/Software/bin/fastqc'

for i in ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5']:
  reads1="sample_"+ str(i) +"_1.fq.gz"
  reads2="sample_"+ str(i) +"_2.fq.gz"
  print(f'{fastqc} -f fastq -o qc -t 6 {reads1} {reads2}')
 ```


## while循环

for循环是对集合中的每一个元素分别操作，而while循环则不断的运行，直到指定的条件不再满足。

while循环体的结构为首先一个判断条件，如果判断条件为真（True）则执行，否则停止循环。

如果条件为True，则是一个死循环，死循环**（endless loop）**是指无法靠自身的控制终止的循环，也就是循环一直执行下去，直到加入外接条件才能改变循环，例如终止程序。


```python
\#死循环

while True:
   print(f"This is a endless loop")

死循环是非常危险的，如果是写入文件，死循环会一直往文件内输入内容，知道把整个磁盘写满。

\#死循环写入文件，下面代码很危险
 
 file_out = open('myfile.txt', 'w')
 while True:
   file_out.write("This is a endless loop\n")
```


不过死循环也有用处，比如操作系统开机之后有些程序就一直在循环运行，直到关机操作才终止执行。另外，服务器端一个序列的程序，一直在检测是否有上传的序列，直到检测到有人上传了序列，则跳出循环。

 

for循环一般是先判断条件，在执行，相对安全一些，而while循环如果条件为真，很容易造成死循环。因此，在while循环中一定要设置好跳出循环条件。

```python 
#while循环    
i=0

while i<10:
  print (i)
  i=i+1  

```

上面的案例中，如果忘记每次给i的值增加，就是一个死循环。

```python
i=0
 while i<10:
   print (i)
  \# i=i+1

```

 

## for循环改成while循环
```python
# for循环

for i in ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5']:
  reads1="sample_"+ str(i) +"_1.fq.gz"
  reads2="sample_"+ str(i) +"_2.fq.gz"
  print (reads1,reads2)

# while 循环

alist = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5']
i = 0;

while i < len(alist):
  name = alist[i]
  reads1 = "sample_" + str(name) + "_1.fq.gz"
  reads2 = "sample_" + str(name) + "_2.fq.gz"
  print(f"{reads1} {reads2}")
  i += 1
  
```