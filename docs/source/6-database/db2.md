# 6.2 下载数据库的几种方法

## 1 数据库下载方法选择

数据库的下载比较容易，最重要的就是找到数据库的下载地址即可。

如果你想要下载数据，首先要明确三个问题。

**第一：下载哪些哪种类型的文件**

这些数据都到哪里去找呢，这个大家要有一些基本常识，比如参考序列一般都在三个核酸数据库，NCBI，embl，ddbj等，ddbj这个用的并不多。清楚每个网站都有哪些内容，比如在做RNAseq时需要gtf文件，可以到embl下载gtf格式。还有就是ucsc基因组浏览器网站也提供很多数据下载，另外，一些基因组序列有单独的网站提供数据下载。这些大家在平时要多注意总结。

**第二：找到下载地址**

登录网站之后，要能够找到数据的下载链接，其实也就是数据所在服务器里的存储位置。这个是非常重要的。现在的很多网站内容越来越多，虽然我们知道可以去NCBI或者EMBL下载物种参考基因组，但是从里面找到数据位置有时候也是比较困难的，拿NCBI为例，里面数据实在是太多了，各种数据库，比如你要能区分genebank与refseq的差别，才能找到数据下载链接。

另外还有一个问题就是数据的权限，有些网站数据库是完全公开的，找到链接就可以下载，比如ncbi，embl，ucsc这种数据库，还有一些是需要注册才能够下载的，一般还要求是教育域名的邮箱才能注册，比如RepeatMasker数据库，还有一些是有权限控制的，比如TCGA数据库，需要很严格的申请流程，才能下载到leve1和level2的数据，也就是原始数据以及原始数据比对的bam文件，普通用户是申请不了的。还有一些数据库是收费的，只有付费用户才能够下载使用，比如kegg数据库等。

**第三：选择合适的工具**

当你千辛万苦找到数据库下载链接之后，那么接下来就可以开始下载了，选择合适的下载工具也非常重要。例如你可以直接从网页端进行下载，这其实是http协议下载，也可以采用ftp进行下载，这两种方式很多时候大家都是下载到本地windows系统，然后在远程传输到服务器端。其实是可以直接在服务器端采用命令进行下载的，这样省去传输的步奏，也减轻了本地硬盘的反复读写消耗。

## 2 命令行下载

下载生物数据可以使用个人电脑的windows或者macos系统，然后传输到服务器上，但这样操作稍微麻烦。但有时个人计算机上具有更快的网络，也可以使用一些高速下载工具，这样可以直接下载，然后传输到服务器上。

也可以使用Linux系统下的下载命令，直接下载到服务器里。Linux命令行下载的工具其实有很多，系统自带wget和curl命令，也可以自行下载axel等命令。wget非常方便，给定链接地址，就可以直接wget下载了。wget和curl都支持http，ftp等多种协议。

```shell
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/human_g1k_v37.fasta.gz
```

 

**wget常用选项参数：**

  -o 下载信息写入日志文件

-O 下载时重命名文件 

-c 断点续传

-b 放到后台下载

-r 递归下载，用于下载整个目录

–spider测试下载链接是否可用 

-i从文件批量下载，将下载地址写入文件

–mirror镜像网站 

-r -A下载指定格式文件 

wget也可以直接输入账户密码访问ftp服务器进行下载。

加` --ftp-user`接用户名，` --ftp-password`接密码，然后给定下载链接直接访问ftp服务器进行下载。

```shell
#wget下载文件夹

wget -r ftp://ftp.ncbi.nlm.nih.gov/genomes/Acanthaster_planci
```

 

curl的使用和wget类似，不过curl可以给出预测下载完成还剩余多少时间，并通过进度条来显示下载进度。

关于wget和curl更多功能，可以加--help选项查看帮助文档。

## 4.3 ftp下载

FTP 是File Transfer Protocol（文件传输协议）的英文简称，相比于http协议，更加稳定，传输速度也更快。很多网站提供ftp协议的数据下载。

ncbi的ftp地址为，[ftp://ftp.ncbi.nlm.nih.gov/](ftp://ftp.ncbi.nlm.nih.gov/)

embl的ftp地址为：[ftp://ftp.ensembl.org/pub/](ftp://ftp.ensembl.org/pub/)

访问ftp服务器需要四个元素。

第一：ftp的地址，

第二，用户名和密码，可以匿名访问，Anonymous，也就是数据是公开的，不需要要填写。

第三，端口号，ftp默认端口号是21，一般也不用填写；

第四，连接工具。 

其实ftp的地址是可以直接通过浏览器或者资源管理器进行访问的。通过浏览器访问非常不方便，不能直接下载整个文件夹，而且不能断点续传。Linux系统可以使用ftp命令访问下载，但是由于ftp命令不支持文件夹下载，lftp工具更加强大，下面我们直接演示一下通过lftp工具来下载数据。

```shell
#lftp，后面跟用户名，然后at符号，ftp服务器地址。
lftp [ftp://ftp.ncbi.nlm.nih.gov/](ftp://ftp.ncbi.nlm.nih.gov/)

#lftp anonymous@ftp.ncbi.nlm.nih.gov/blast/db
#这里密码是空的，我们直接敲回车即可
#ls列出文件
>ls

>cd /blast/db
> mget swissprot.tar.gz
#mirror下载文件夹
>mirror v4
> exit
```



## 4 高速下载

Asprea是一款非常神奇的工具，它可以极大的提高数据传输的效率，Asprea是一家专门做数据传输解决方案的公司，后来被IBM公司收购了。Aspera 解决方案的核心是 Aspera FASP (Fast, Adaptive and Secure Protocol) 传输专利技术，它是一项突破性传输协议，利用现有广域网 (WAN) 基础架构和通用硬件，传输速度比 FTP 和 HTTP 快数百倍。FASP 提供企业级安全性、出色的可靠性以及卓越的带宽控制能力。有测试显示原本在美国国内 FTP 需要超过10小时才能传完的数据，现在 Aspera 只需 8.4 秒就能搞定。总之就是数据传输速度非常非常快。

目前NCBI以及EBI等机构的数据都支持aspera下载。首先我们来介绍一下Aspera的下载安装。

http://asperasoft.com/

```
#安装aspera

wget https://download.asperasoft.com/download/sw/connect/3.9.9/ibm-aspera-connect-3.9.9.177872-linux-g2.12-64.tar.gz

tar -zxvf ibm-aspera-connect-3.9.9.177872-linux-g2.12-64.tar.gz

sh ibm-aspera-connect-3.9.9.177872-linux-g2.12-64.sh
```

 利用aspera下载数据

```
.aspera/connect/bin/ascp -i .aspera/connect/etc/asperaweb_id_dsa.openssh --overwrite=diff -QTr -l6000m anonftp@ftp.ncbi.nlm.nih.gov:blast/db/FASTA/nt.gz . &

blast/db/FASTA/

.aspera/connect/bin/ascp -i .aspera/connect/etc/asperaweb_id_dsa.openssh --overwrite=diff -QTr -l6000m anonftp@ftp.ncbi.nlm.nih.gov:blast/db/FASTA/nr.gz . &

.aspera/connect/bin/ascp -i .aspera/connect/etc/asperaweb_id_dsa.openssh --overwrite=diff -QTr -l6000m anonftp@ftp.ncbi.nlm.nih.gov:pub/COG/ . &

.aspera/connect/bin/ascp -i .aspera/connect/etc/asperaweb_id_dsa.openssh --overwrite=diff -QTr -l6000m anonftp@ftp.ncbi.nlm.nih.gov:blast/db/swissprot.tar.gz ./ &
```

 

注意事项：

1、aspera只能普通用户使用，管理员无法使用；

2、aspera会占用大量带宽，带来网络拥堵，使用时要注意；

3、使用时需要正确给出aspera-license，在-i后面接license文件，这里是asperaweb_id_dsa.openssh

4、ftp下载时账号要写正确，ncbi是anonftp@ftp.ncbi.nlm.nih.gov

5、ftp地址后面接冒号，然后是ftp上面文件的具体位置，不要写错了。

6、不是所有的网站都支持Aspera下载的，需要服务提供方购买Aspera服务，用户才可以使用。

## 5 批量下载序列

虽然前面介绍过ftp和Aspera下载很方便，例如下载某个物种全部的数据。但是如果想下载来自多个物种的不同基因序列，例如给定一个基因列表list，如何下载到这些序列呢？这时就需要用到**Batchentrez**。

批量下载基因序列有多种方式，例如可以通过编程实现，也可以通过固定模块例如bioperl，biopython等。如果不会编程，那么batchentrez就是最好的选择了。Entrez是NCBI官方的数据检索系统，Batch Entrez显然就是批量检索。

https://www.ncbi.nlm.nih.gov/sites/batchentrez

**1、Accession number** 

An Accession number is a unique identifier given to a sequence when it is

submitted to one of the DNA repositories (GenBank, EMBL, DDBJ). The initial deposition of a sequence record is referred to as version 1. If the sequence is updated, the version number is incremented, but the Accession number will remain constant.

**2、GI**

The GenInfo Identifier is a sequence identification number for a nucleotide sequence. If a

nucleotide sequence changes in any w ay, a new GI number will be assigned. A separate GI number is also assigned to each protein translation within a nucleotide sequence record, and a new GI is assigned if the protein translation changes in any w ay. GI sequence identifiers run parallel to the new accession.version system of sequence identifiers (see the description of Version).

**3、GeneID**

GeneID is a unique identifier that is assigned to a gene record in Entrez Gene. It is an integer and is species specific. In other words, the integer assigned to dystrophin in human is different from that in any other species. For genomes that had been represented in LocusLink, the GeneID is the same as the LocusID. The GeneID is reported in RefSeq records as a 'db_xref' (e.g./db_xref="GeneID:856646", in GenBank format).

https://www.ncbi.nlm.nih.gov/genbank/acc_prefix/

第一，注意输入文件格式，ID只能使用accession numbers or identifiers。

第二、选择的数据库要和输入的序列ID相一致，不能输入的是核酸序列，下载的数据库选择蛋白的库。

第三、序列ID后面不要加空格，另外就是注意一下不同系统中换行符问题。