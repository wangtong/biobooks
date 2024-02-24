## 5.5 bioconda常见问题

> conda在使用过程中会遇到很多问题，本次内容我们系统来介绍一下。

### 1 搜索不到

```shell
ackagesNotFoundError: The following packages are not available from current channels:
```
**原因：**

可能是没有配置bioconda或者conda-forge软件源或者写错了。或者软件名字有问题，或者库里面不存在该软件。

**解决方法：**

查看软件配置文件，尝试添加通配符扩大搜索范围。

### 2 搜索速度慢

conda搜索或者安装初期一直在转圈，一直处于`solving environment`中。

**原因：**

这是因为bioconda中包含的软件越来越多，而且软件的不同版本都保留了下来，软件的索引文件越来越大，安装一个新软件时搜索满足环境中所有软件依赖的软件的搜索空间也会越来越大，导致`solving environment`越来越慢。

**解决方法：**

跳过搜索步奏，直接安装。

通过网页端搜索，然后直接安装；

安装时直接指定版本；

提高网络速度；

设置通道优先级高于软件版本优先级。

```shell
conda config --set channel_priority strict
```
利用mamba替代conda。

### 3 安装中断

安装过程中出现 **`core dump error/Segment fault`**等错误。

**原因：**

出现这个错误原因很多，可能是硬件资源不够，也可能是软件版本冲突。

**解决方法：**如果安装中断可以重新运行安装命令。

也可以选择清空缓存

https://github.com/conda/conda/issues/7815

```shell
conda clean -a
```
### 4 版本冲突
```
Encountered problems while solving:

 - package blast-2.7.1-boost1.64_1 requires boost 1.64*, but none of the providers can be installed
```
由于软件依赖与现有环境中的配置相冲突，导致软件无法安装成功。

解决方法：使用虚拟环境安装。

### 5 权限问题

```shell
The environment is inconsistent, please check the package plan carefully
The following packages are causing the inconsistency:
```
conda目前并不能像R软件一样，为允许每个用户创建私有的库，如果使用系统管理员安装的bioconda，那么普通用户不能使用conda继续安装软件，只能使用软件。

解决方法：

自己安装biocodna到个人目录下。

### 6 使用管理员安装的软件 

如果自己安装了biocodna，同时要使用管理员安装的bioconda安装的软件，这个时候，可以使用软件的全路径。

``` 
#使用软件全路径
/ifs1/Software/miniconda3/bin/bwa
```