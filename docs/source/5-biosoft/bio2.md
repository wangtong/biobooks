# 5.2 编译软件

> 编译(compilation , compile) ，利用编译程序从源语言编写的源程序产生目标程序的过程。编译就是把高级语言变成计算机可以识别的2进制语言，计算机只认识1和0，编译程序把人们熟悉的语言换成2进制的。

## 1 解释语言与编译语言

生物信息软件作者使用多种类型的程序语言，例如C，C++,python，java，python，R等，这些语言都高级程序语言，各有优缺点。计算机最终都需要将其转换为二进制才能执行。那么转换成二进制的过程分为编译型和解释型。

### 1.1 编译型与解释型

- 编译型语言代表有：C语言，C++、Object-C等；通常都会对源代码进行编译，生成可以执行的二进制代码，执行的是编译后的结果

- 解释型语言代表有：JavaScript、Python、Erlang、PHP、Perl、Ruby等；通常不用对源代码进行编译，一般是通过解释器载入脚本后运行。由于每个语句都是执行的时候才进行解释翻译，这样解释性语言每次执行就要翻译一次，效率相对要低。

- Java具有编译与解释两种特性：既可以将其源代码当作脚本执行，也可以进行编译成.class代码（字节码）载入运行。

### 1.2 编译型与解释型的区别

编译型语言的是将源代码编译成二进制代码之后才能运行，因此执行效率更高，可已移植性更好。例如有些C语言编写的程序，直接将编译好的软件拷贝到新的设备上就可以直接运行。但是，编译型语言每次都得编译之后才能运行，在编写程序时，不容易测试。

解释型语言的优点是不需要编译就可以直接运行，方便查看源代码。而且有良好的平台兼容性，在任何环境中都可以运行，可以快速部署，不用停机维护。但是解释型语言移植到新设备上同时需要编译器。例如python程序只有设备上安装了python程序才能解释执行。另外，由于每次运行的时候都要解释一遍，性能上不如编译型语言。

## 2 README文件

一般软件安装包内，除了包含各种源代码文件，还包括测试数据，软件说明，以及README文件。文件名可以为README，readme.md，readme.txt，INSTALL.txt ，INSTALL等。可以直接使用less命令查看。readme文件会对软件进行详细的介绍，包括软件说明，安装方法，使用案例，联系方式等内容，主要看安装方法部分。
```shell
#安装R语言依赖
yum install -y --skip-broken zlib java gcc-gfortran gcc gcc-c++ readline-devel libXt-devel bzip2-devel.x86_64 bzip2-libs.x86_64 xz-devel.x86_64 pcre-devel.x86_64 libcurl-devel.x86_64

#下载
wget https://cloud.r-project.org/src/base/R-4/R-4.1.1.tar.gz
tar -zxvf R-4.1.1.tar.gz -C ~/biosoft
cd ~/biosoft/ R-4.1.1
```

查看编译部分，打INSTALL文件

```shell
As you are reading this file, you have unpacked the R sources and are
presumably in the top directory.  Issue the following commands:

	./configure
	make

(If your make is not called `make', set the environment variable MAKE to
its name, and use that name throughout these instructions.)
This will take a while, giving you time to read `R-admin.html'.

Then check the built system worked correctly, by

	make check

and make the manuals by either or both of

	make pdf	to create PDF versions
	make info	to create info files

However, please read the notes in `R-admin.html' about paper size and
making the reference manual.
```

## 3 编译软件过程

一般编译软件分成三个步骤，有的分为四个步骤，具体几个步骤根据不同的软件不同，还需要看具体是哪种语言编写的程序。下面以一个典型的软件安装过程来进行介绍。

### 3.1 configure

`configure`是在编译前检查环境配置，也可以通过选项参数，来更改软件安装目录。configure是一个shell脚本文件，可以直接打开查看。configure运行时会不停检查环境，提示一些`warnings`和`error`信息。warnings可以忽略，但是遇到error就会停止，需要解决这个依赖，然后重新运行configure，直到全部检查通过，才可以进行下一步`make`。

```shell
#检测配置
./configure --enable-R-shlib --with-pcre1 
```

 

### 3.2 make

当configure运行结束，且没有问题的时候，可以使用make进行编译。make就是将源代码编译成二进制的过程。有些软件make之前还有一个make test，make check等过程。也有一些软件不需要configure，直接make编译。

make结束之后就会在目录下发现有些可执行文件，或者多出一个bin目录。这个时候就可以直接运行这些软件了。

```shell
#编译
make
```

### 3.3 make install

make已经完成了编译过程，make install主要是将软件链接到指定的安装目录，即第一步configue指定的目录下。如果第一步没有指定，则安装到默认的目录下，一般是/usr目录。这里需要注意，如果不是管理员用户，则没有权限写入/usr目录，这个时候会提示一个权限的问题，“**Permission denied”**，这个不影响软件运行，可以手动将可执行程序链接至自己的软件目录内。

这样configure，make，make install就完成了软件安装，这其中，最重要的就是configure这一步。如果configure没有问题，则make 和 make install一般可以顺利完成。

```shell
#安装
make install
```

## 4安装已编译软件

很多软件除了提供源代码之外，还提供了已编译的版本，也就是编译好的版本，这样的版本可以直接使用。如果软件提供编译好的版本，建议选择这样的版本，非常方便，下载之后，解压缩就可以使用了。源代码与已编译有什么区别呢？源代码编译会首先检查每个系统的硬件和环境配置，然后更有针对性的进行编译，一般来说，这样的软件运行效率比已编译的版本效率更高。不过，这样的效率差别主要针对互联网应用，有很大的运行次数，如果每次差1秒钟就会有很大的影响，生物软件影响不大。

下面将通过几款软件的安装过程，来进行讲解练习。在安装软件之前，我们先创建三个文件目录，分别是bin，biosoft以及src。

```shell
#创建文件夹
mkdir bin biosoft src
```

bin：存放每个软件的可执行程序

biosoft：软件安装目录；

src：软件源代码；

下面给出几个安装已编译好的软件，更多内容见案例代码。

```shell
#1 blast+
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.12.0+-x64-linux.tar.gz
tar -zxvf ncbi-blast-2.12.0+-x64-linux.tar.gz
cd ~/biosoft/ncbi-blast-2.10.1+/bin
ls -1  | while read i;do ln -s $PWD/$i ~/bin/;done;

#2 edirect
wget  https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz
tar -zxvf edirect.tar.gz 
cd ~/bin/
ln -s ~/biosoft/edirect/efetch .
ln -s ~/biosoft/edirect/edirect.pl .

#3 sratookit
#下载指定版本
wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.10.8/sratoolkit.current-centos_linux64.tar.gz
tar -zxvf sratoolkit.current-centos_linux64.tar.gz
cd ~/bin
ln -s  ~/biosoft/sratoolkit.2.11.1-centos_linux64/bin/prefetch ./
ln -s  ~/biosoft/sratoolkit.2.11.1-centos_linux64/bin/fasterq-dump ./
ln -s  ~/biosoft/sratoolkit.2.11.1-centos_linux64/bin/fastq-dump ./
```

## 5自行编译软件

有一些软件没有已编译版本，需要自行进行编译，自行编译的好处是可以更好的适应硬件环境，效率更好一些，但其实对于我们普通用户影响不大，又不是一些互联网应用，每秒处理上亿次请求的工具，会有一些差别。自行编译也不用太过担心，一些工具还是比较容易编译的，直接敲make就可以完成，稍微复杂一点的可以查看帮助文档，这个过程也是一个学习和深入理解计算机原理的过程。由于系统配置环境不同，下面编译软件，有些可能会不成功。如果编译不成功，后面可是使用bioconda来进行安装。将源代码解压至安装目录biosoft下，编译完成之后，将可执行程序ln -s链接到bin目录下即可。

下面给出几个编译软件的案例，更多内容见脚本代码。

```shell 
#1 bwa
cd ~/biosoft
git clone https://github.com/lh3/bwa.git
cd bwa; make

#2 minimap2
git clone https://github.com/lh3/minimap2
cd minimap2 && make

#3 prodigal
git clone https://github.com/hyattpd/Prodigal.git
cd Prodigal
make install 

#4 canu
git clone https://github.com/marbl/canu.git
cd canu/src
make 

#5 flye
git clone https://github.com/fenderglass/Flye
cd Flye
make

#6 mummer4
gti clone https://github.com/mummer4/mummer.git
./configure
make
make install
```