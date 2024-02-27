# 5.10 命令行计算工具datamash

> Excel，R和python都是非常好用的统计软件，功能强大，但是有时候只想做一个简单的计算，如果单独打开这些工具，再读入数据就稍显麻烦。如果使用命令行版本的sed，awk，perl等工具，当然也可以完成工作，但是这些工具语法太乱，代码不容易阅读，这里给大家推荐一个好用的命令行工具datamash。

------

## 1 datamash做什么的

datamash是data和mash的组合词语，data是数据，mash捣碎和调情的意思，这里边应该翻译捣碎更加贴切。它是一个GNU工具，和Linux一些基础命令类似，所以可以使用yum或者apt直接安装。这样就可以在命令行中对数据进行各种处理了。

那么通常都对数据要做哪些处理呢，最基础的当然就是四则运算：加减乘除，在稍微复杂点就是各种乘方开方取余操作，还有各种统计检验函数，更加复杂的就是分组计算以及数据透视等。可以将其看成一个命令行版本的R软件。



## 2 软件安装

直接使用apt或者yum工具安装即可。如果不是管理员，可以使用conda安装更加方便。

```shell
#ubuntu系统
apt install -y datamash 
#centos系统
yum install -y datamash 
#conda安装
conda install -y datamash 
```



## 3 使用说明

直接输入软件名datamash --help就可以看到软件说明。

```
(base) root 13:19:36 ~
$ datamash --help
Usage: datamash [OPTION] op [fld] [op fld ...]

Performs numeric/string operations on input from stdin.

'op' is the operation to perform.  If a primary operation is used,
it must be listed first, optionally followed by other operations.
'fld' is the input field to use.  'fld' can be a number (1=first field),
or a field name when using the -H or --header-in options.
Multiple fields can be listed with a comma (e.g. 1,6,8).  A range of
fields can be listed with a dash (e.g. 2-8).  Use colons for operations
which require a pair of fields (e.g. 'pcov 2:6').
```

datamash语法结构是这样的：

**datamash [OPTION] op [fld] [op fld ...]**

和R或者python一样，datamash是表格计算工具，因此输入文件需要是表格格式。

**[OPTION]**是选项参数

```
-C, --skip-comments：跳过注释行，一般井号开头的行；
-f, --full: 全部行进行计算
-g, --group：分组计算，离散数据才可以进行分组
--header-in：指定第一行为表头，不进行计算
--header-out：输出第一行为列名
-i，--ignore-case：忽略大小写
-s,--sort：排序
-t：指定输入文件分隔符
--narm：跳过缺失值NA
-R, --round：保留几位小数点
-W, --whitespace: 使用空格或者tab作为分隔符
--hlep:输出帮助信息
```

**op**是指operation to perform，即使上面那些操作函数；

**fld**是指input field，具体需要计算的某一列。

## 4 使用案例

话不多少，直接上使用案例，对于这种工具类的东西，简单粗暴，直接拿案例最明显。案例来自于官方手册。

<https://www.gnu.org/software/datamash/manual/datamash.html>

案例数据：案例中使用了一个scores.txt，是一个简单的列表，只有三列，分别是学生姓名科目和成绩，其中第二列是离散数据可以用于分组，第三列是连续数据，用于进行计算。这个列表可以从软件安装包里获得。另外一个scores_h.txt内容一致，就是多了一行表头。



```shell
$ wget https://ftp.gnu.org/gnu/datamash/datamash-1.4.tar.gz
$ tar -zxvf datamash-1.4.tar.gz
$ cd datamash-1.4/examples
$ ll
total 2024
-rw-rw-r-- 1 root root 1026624 Jan  3  2016 genes_h.txt
-rw-rw-r-- 1 root root 1026495 Jan  3  2016 genes.txt
-rw-rw-r-- 1 root root    7966 Jan 25  2018 readme.md
-rw-rw-r-- 1 root root    1818 Jan  3  2016 scores_h.txt
-rw-rw-r-- 1 root root    1801 Jan  3  2016 scores.txt
```



案例1：计算1-10的和与平均值

```shell
  $ seq 10 | datamash sum 1 mean 1
  55  5.5
```

案例2：将数据进行转置

```shell
  $ seq 10 | paste - - | datamash transpose
  1    3    5    7    9
  2    4    6    8    10
```

案例3：分组计算频数，根据第二列进行分组。如果计算其他值，只需更换函数就行

```shell
$ cat scores.txt | datamash --sort groupby 2 count 2 
Arts    19
Business    11
Engineering    13
Health-Medicine    13
Life-Sciences    12
Social-Sciences    15
```

案例4：根据第二列进行分组，计算第三列的最大值和最小值

```shell
$ cat scores.txt | datamash --sort groupby 2 min 3 max 3
Arts    46  88
Business    79  94
Engineering    39  99
Health-Medicine    72  100
Life-Sciences    14  91
Social-Sciences    27  90
```



案例5：输出表头

```shell
cat scores.txt | datamash --sort --header-out groupby 2 min  3 max 3
```

案例6：跳过第一行表头

```shell
cat scores_h.txt |  datamash --sort --header-in groupby 2 mean 3
```

案例7：使用列名代替列号

```shell
cat scores_h.txt |  datamash --sort --headers groupby Major mean Score 
```

案例8：按列计算，使用不同的语法

```shell
$ seq 100 | paste - - - - | datamash sum 1 sum 2 sum 3 sum 4
1225  1250   1275   1300

$ seq 100 | paste - - - - | datamash sum 1,2,3,4
1225  1250   1275   1300

$ seq 100 | paste - - - - | datamash sum 1-4
1225  1250   1275   1300

$ seq 100 | paste - - - - | datamash sum 1-3,4
1225  1250   1275   1300
```

## 6 更多案例

更多案例可以查看官方文档。其实只需要掌握下面这些函数即可。如果想了解每个函数更多内容，可以查看软件自带帮助手册。

```shell
man GNU datamash
```

Primary operations:

```shell
groupby：分组
crosstab：交叉统计
transpose：转置
reverse：反转
check：验证数据结构
```

Line-Filtering operations:

```shell
rmdup：删除重复行
```

Per-Line operations:

```shell
round：四舍五入整数值
floor：向上取整
ceil：向下取整
trunc：取整数部分
frac：取小数部分
dirname：取目录名
basename：取文件名
barename：路径中的文件名
extname：扩展名
```

Group-by Numeric operations:

```shell
sum：求和
min：最小值
max：最大值
absmin：最小绝对值
absmax：最大的绝对值
range：最大值 - 最小值
```

Group-by Textual/Numeric operations:

```shell
count ：计算频数
first：获取分组中第一个值
last：获取分组中最后一个值
rand：获取分组中一个随机值
unique：获取唯一值
collapse：逗号分科的所有值
countunique：唯一值的个数
```

Group-by Statistical operations:

```shell
mean：均值
mode：众数
median：中位数
q1：第一四分位数
q3：第三四分位数
iqr：四分位距
perc：百分位值，默认取 95，perc:25 等同于 q1
antimode：最少出现的数
pstdev：总体标准差
sstdev：样本标准差
pvar：总体方差
svar ：样本方差
mad：scaled 绝对中位差
madraw：原始绝对中位差
sskew：样本偏度
pskew：总体偏度
skurt：样本超值峰度
pkurt：总体超值峰度
jarque：Jarque-Beta test for normality P 值
dpo：D’Agostino-Pearson Omnibus test for normality P 值
scov：样本协方差
pcov：总体协方差
spearson：样本pearson相关系数
ppearson：总体pearson相关系数
```