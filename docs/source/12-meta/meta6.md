# 12.6 宏基因组分析环境配置

## 1 安装软件

```shell
#创建meta虚拟环境
conda create -n meta -y
conda activate meta
mamba install -y fastqc
mamba install -y multiqc
mamba install -y fastp 
mamba install -y seqkit  
mamba install -y centrifuge
mamba install -y taxonokit
mamba install -y bwa 
mamba install -y bwa-mem2
mamba install -y kraken2

```



## 2 宏基因组数据库

### 2.1 NCBI物种分类taxonomy数据库

NCBI的分类数据库，包括大于7万余个物种的名字和种系，这些物种都至少在遗传数据库中有一条核酸或蛋白序列。其目的是为序列数据库建立一个一致的种系发生分类学。截止到目前，各个物种的统计结果见下表。

数据库地址：https://www.ncbi.nlm.nih.gov/taxonomy

数据下载地址：https://ftp.ncbi.nih.gov/pub/taxonomy

表 4 NCBI物种分类数据库统计

​                               

### 2.2 nt/nr库

nt库：NT(Nucleotide Sequence Database)，核酸序列数据库，包含所有已测序基因组序列，以及各种测序片段的序列。里面的数据是冗余的，比如同样一个物种，每测序一次，就添加一次，随着测序测序数据越来越多，nt也越来越大。

nr库：Non-Redundant Protein Sequence Database，非冗余蛋白库，包括 GenPept, Swissprot, PIR, PDF, PDB, and NCBI RefSeq等库。

下载地址：[ftp://ftp.ncbi.nih.gov/blast/db](ftp://ftp.ncbi.nih.gov/blast/db)

#nt库下载：
wget -c [ftp://ftp.ncbi.nih.gov/blast/db/FASTA/nt.gz](ftp://ftp.ncbi.nih.gov/blast/db/FASTA/nt.gz)

```shell
#nr库下载：
wget -c ftp://ftp.ncbi.nih.gov/blast/db/FASTA/nr.gz
```




### 2.3 Refseq数据库：

RefSeq数据库：the reference sequence database，参考序列数据库，是经过NCBI和其他组织校正的数据库，使用人类基因命名委员会定义的术语，并且包括了官方的基因符号和可选的符号。RefSeq数据库和GenBank数据库的区别在于：GenBank是一个开放的数据库，对每个基因都含有许多序列。genbank的数据可能重复或者不准。而RefSeq数据库是NCBI提供的校正的序列数据和相关的信息。

refseq网址：https://www.ncbi.nlm.nih.gov/refseq/

 

### 2.4 GTDB

GTDB：Genome Taxonomy Database，基因组分类数据库，是基于大量基因组的系统发育分析来构建基因组分类学研究的标准流程，从而对微生物进行分类 。

数据库主页：http://gtdb.ecogenomic.org/

可以使用工具GTDB-Tk来基于该数据库对未知基因组进行分类。

### 2.5 EBI MGNify

以前是EBI Metagenomics，欧洲分子生物学中心EBI下属机构。提供了一个免费使用的平台，用于组装，分析和归档源自特定环境中存在的微生物种群的测序的微生物组数据。

https://www.ebi.ac.uk/ena

https://www.ebi.ac.uk/metagenomics/

### 2.6 功能注释数据库

UniProtKB： https://www.uniprot.org/

Gene Ontology：http://www.geneontology.org/

CARD数据库： https://card.mcmaster.ca/

KEGG数据库： https://www.kegg.jp

COG数据库：https://www.ncbi.nlm.nih.gov/COG/

CAZy数据库：http://www.cazy.org/

## 3 公共分析平台

目前有一些公众的宏基因组数据分析平台，这些平台采用网页应用，无需敲命令，只需提交数据，即可完成分析，使用简单。但是运行速度较慢，对于数据大小有限制。

Qitta：https://qiita.ucsd.edu/static/doc/html/index.html

MG-RAST：[https://ww](https://www.mg-rast.org/)[w](https://www.mg-rast.org/)[.m](https://www.mg-rast.org/)[g](https://www.mg-rast.org/)[-rast.org](https://www.mg-rast.org/)

gcMeta：https://gcmeta.wdcm.org/

galaxy：http://huttenhower.sph.harvard.edu/galaxy/

epi2me：https://epi2me.nanoporetech.com/

