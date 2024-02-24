# 5.8 利用bioconda管理R和python环境
## 1 利用bioconda管理R
bioconda中包含了大量R包，可以通过bioconda管理R包。相比于R内置的函数，bioconda提供了更加方便的环境管理，安装R包更加方便。
在使用bioconda管理R包之前，首先需要知道R包在bioconda中名字为r-base，一些Bioconductor包的名字为bioconductor-前缀。这样就可以使用conda命令安装和管理R包了。bioconda安装的R包，安装路径在下面目录下。
```shell
~/miniconda3/lib/R/library"
```
## 2 安装R
```shell
#安装R
mamba install -y r-base
#创建R虚拟环境
mamba create -n R -y r-base
```
## 3 安装CRAN R包
```shell
mamba install -y r-tidyverse
mamba install -y r-monocle3
mamba install -y r-seurat
mamba install -y r-wgcna
mamba install -y r-biocmanager
mamba install -y r-vcd
mamba install -y r-qqman
mamba install -y r-rwordseg
mamba install -y r-pheatmap
mamba install -y r-maps
mamba install -y r-ggsci
mamba install -y r-ggpubr
mamba install -y r-ggthemes
mamba install -y r-factoextra
mamba install -y r-circlize
mamba install -y r-factominer
mamba install -y r-gridExtra
mamba install -y r-ggfortify
mamba install -y r-vioplot
mamba install -y r-venn
mamba install -y r-plotrix
```
## 4 安装Bioconductor R包
```shell
mamba install -y bioconductor-deseq2
mamba install -y bioconductor-edgeR
mamba install -y bioconductor-clusterprofiler
mamba install -y bioconductor-biobase 
mamba install -y bioconductor-genomicalignments 
mamba install -y bioconductor-tcgabiolinks 
mamba install -y bioconductor-rsamtools
mamba install -y bioconductor-rsubread
mamba install -y bioconductor-txdb.hsapiens.ucsc.hg19.knowngene
mamba install -y bioconductor-txdb.hsapiens.ucsc.hg38.knowngene
mamba install -y bioconductor-tximport
```
## 5 配置R包搜索库
如果想让自己安装的R包，在网页端使用，需要将自己配置的R包安装路径，也就是R的库，需要将库目录，通过`.libPath()`函数添加到搜索目录中。
```
(base) wangtong 10:24:06 ~
#使用自己安装的R
$ /ifs1/Software/biosoft/R-4.1.1/bin/R

#列出当前R包目录，有两个
> .libPaths()
[1] "/home/wangtong/R/x86_64-pc-linux-gnu-library/4.1"
[2] "/ifs1/Software/biosoft/R-4.1.1/library"    
#通过new选项增加新的目录      
> .libPaths(new="/ifs1/Software/miniconda3/lib/R/library")
#新的目录增加进来了，这样一下子就多了很多包可以使用
> .libPaths()
[1] "/ifs1/Software/miniconda3/lib/R/library"
[2] "/ifs1/Software/biosoft/R-4.1.1/library" 
new选项会去掉之前默认的，可以通过在函数中增加一个向量增加多个目录。
> .libPaths()
[1] "/home/wangtong/R/x86_64-pc-linux-gnu-library/4.1"
[2] "/ifs1/Software/biosoft/R-4.1.1/library"          
> .libPaths(c(.libPaths(),"/ifs1/Software/miniconda3/lib/R/library"))
> .libPaths()
[1] "/home/wangtong/R/x86_64-pc-linux-gnu-library/4.1"
[2] "/ifs1/Software/biosoft/R-4.1.1/library"          
[3] "/ifs1/Software/miniconda3/lib/R/library"   
```
## 6 利用bioconda管理python
```shell
#配置python数据分析环境
conda create -n pydata -y
conda activate pydata
conda install -y numpy
conda install -y pandas
conda install -y matplotlib
conda install -y scipy
conda install -y scikit-learn
conda install -y seaborn
conda install -y patsy
conda install -y plotnine
conda install -y statsmodels
conda install -y plotly
conda install -y pytorch
conda install -y tensorflow
conda install -y keras

#安装opencv
conda create -n opencv -y
conda activate opencv
conda install -y opencv
```