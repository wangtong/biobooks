# 5.7 虚拟环境
>虽然目前使用bioconda可以非常方便的管理很多软件，但是由于生物软件的类型实在太多了。完全没有统一的开发平台，因此，即使利用bioconda还是会出现一些问题，比如需要使用的软件是基于python2.7版本，而安装之后的python版本为3.7。必须切换到python 2.7才能使用，这个时候就可以使用bioconda创建的虚拟环境。

## 1 虚拟环境
conda可以创建一个隔离的软件运行环境，利用conda env list可以查看虚拟环境，默认安装的为base环境。通过create可以创建虚拟环境。
```shell
#查看虚拟环境，*号表示当前环境

# conda environments:
#
base                  *  /ifs1/User/wangtong/mambaforge
eggnog                   /ifs1/User/wangtong/mambaforge/envs/eggnog
                         /ifs1/User/wangtong/miniconda3
                         /ifs1/User/wangtong/miniconda3/envs/16s
                         /ifs1/User/wangtong/miniconda3/envs/artic
                         /ifs1/User/wangtong/miniconda3/envs/augustus
                         /ifs1/User/wangtong/miniconda3/envs/biobakery
                         /ifs1/User/wangtong/miniconda3/envs/blast
```
虚拟环境的一个好处是可以创建一个独立环境，在环境中可以安装指定版本软件，可以用于使用特定版本软件重复文献内容，例如安装`blast 2.7.1`，`samtools 1.7`
```shell
#查看虚拟环境
conda env list
2利用虚拟环境安装软件
2.1 安装指定版本软件
#创建虚拟环境
conda create -n test 
#激活虚拟环境
conda activate test
#安装软件
mamba install -c bioconda bwa=0.7.15 samtools=1.6 bcftools=1.12
#退出虚拟环境
conda deactivate
```
## 2 创建python2.7环境
我们最开始安装的是minicodna3的版本，一次默认就是pyhton3的版本。但是有很多软件依然需要使用python2的版本，因此需要创建一个pyhton2的环境。
```shell
#创建python 2.7环境
conda create -n py27 python=2.7 -y
#查看现有虚拟环境
conda env list
#激活python2.7环境
conda activate py27
#查看python版本
python -V
```
在python2中安装软件
```shell
mamba install -y blast=2.7.1
mamba install -y metaphlan2
mamba install -y humann2
mamba install -y htseq
```
## 3 安装rnaseq分析软件
```shell
#创建RNAseq分析环境
conda create -n rnaseq -y
conda activate rnaseq
#安装软件
mamba install -y gffread
mamba install -y fastqc
mamba install -u multiqc
mamba install -y fastp
mamba install -y parallel
mamba install -y hisat2
mamba install -y star
mamba install -y subread
mamba install -y salmon
mamba install -y kallisto
mamba install -y rsem
mamba install -y trinity
```
## 4 普通用户使用虚拟环境
如果没有将管理员的虚拟环境添加到配置文件，也可以使用这些软件，参考下面的方法。
```shell
#查看管理员虚拟环境
ll /ifs1/Software/miniconda3/envs/
#激活环境
conda activate /ifs1/Software/miniconda3/envs/rnaseq
#查看软件
conda list
#退出环境
conda deacivate
```
## 5 不激活虚拟环境使用
目前bioconda提供了一个conda run的模式，类似与docker run，可以不激活虚拟环境直接运行程序，不过该功能目前还处于实验阶段，并不完善。
```shll
#直接运行rnaseq中的hisat2
conda run -n rnaseq hisat2 --version
```
##6 导出虚拟环境
```shell
#导出虚拟环境
conda env export -n rnaseq >rnaseq.yaml
#通过配置文件安装软件
conda env create -n rnaseq --file rnaseq.yaml
```
## 6 删除虚拟环境
conda的虚拟环境可以通过conda env进行管理，除了创建，还可以进行升级，导出以及删除环境等。
create ：创建虚拟环境
export ：导出虚拟环境
list   ：列出虚拟环境
remove ：移除虚拟环境
update ：升级虚拟环境
config ：配置虚拟环境
```shell
#移除虚拟环境
conda env remove -n rnaseq
```
## 7 重置环境
```shell
#1删除bioconda
rm -rf ~/miniconda3/

#2删除bioconda配置文件
rm ~/.condarc

#3 替换默认.bashrc文件
cp /etc/skel/.bashrc ./

#4 刷新设置
source ~/.bashrc
```
##8 conda-pack迁移软件
conda pack是一个独立的软件，根据命名就可以知道该软件主要功能是用来对conda环境进行打包的。
<https://conda.github.io/conda-pack/>

想要迁移conda环境有多种方法，例如可以使用conda env export将环境中的软件导出为一个yaml文件列表，在新环境下重新安装。比如qiime2软件就采用这种方式，提供一个yaml软件列表文件。
另外一种方法可以直接对整个环境进行打包压缩迁移。但该方法需要软件安装路径一致，否则在新环境下会有问题。
conda-pack是第三种选择，它可以直接打包整个环境，同时解决环境问题。
```shell
#安装软件
mamba install conda-pack
#打包环境conda pack或者conda-pack都可以
mamba pack -n genome -o genome.tar.gz

#直接接活环境，然后打包
mamba activate genome
mamba pack
```
**选项参数**
-p 文件目录
-n 环境名字
-j 多线程
-o 输出结果文件

**解压到新环境**
```
#首先创建文件夹
mkidr genome
tar -zxvf genome.tar.gz -C genome

#激活环境
mamba activate genome
source genome/bin/activate

#查看软件列表
mamba list

#退出环境
source genome/bin/deactivate
```
