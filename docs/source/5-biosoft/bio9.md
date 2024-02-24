# 5.9 利用Apptainer安装生物软件

>Apptainer是一种容器，之前名字是Singularity，现在改了名字，成为Linux基金会项目。不过之前的singularity部分成员没加入，继续维护singularity项目。

## 1 apptainer简介
现在各种容器技术已经很多了，比如docker，podman，singularity等。每一个都有优缺点，有一定的使用范围。
docker适合一些服务，比如web服务器等。但docker之前需要管理员权限，现在支持rootless面膜是。podman是redhat的容器技术，不需要像docker后台一直要有一个进程守护。但是podman需要redhat的系统原生支持，ubuntu需要较新版本才支持。另外podman目前有一个bug，如果用户主不在/home目录下，开启selinux会有问题。后面可能会修复。
官方网站：<http://apptainer.org>

## 2 为什么选择apptainer？

为什么选择apptainer或者singularity更适合配置生物软件，主要有以下几点：
1. 权限问题，apptainer可以继承用户的权限，比如A用户使用的容器，只有A用户有权限进行操作；
2. apptainer方便迁移，拉取镜像直接放到自己目录下，而docker所有人的镜像都放在固定位置，虽然docker也可以打包拷贝走，但操作起来比较麻烦。
3. 和现有系统无缝整合：系统用户权限、网络等均直接继承宿主机配置，直接就可以运行镜像文件中的命令。
4. 不需运行 daemon守护进程：生物软件安装到一个虚拟机文件中，随时启动，不占用任何资源。资源限制和权限问题也得以解决。
5. 绑定目录的问题，docker每次运行都要绑定目录到容器中，非常麻烦，而apptainer可以直接访问。
6. 可以直接使用docker镜像文件。
7. apptainer可以直接使用bioconda进行安装，无需管理员配置。
8.可直接将整个apptainer文件迁移使用。

## 3 安装apptainer
apptainer可以使用系统工作yum或者apt等直接安装，也可以选择bioconda安装，推荐系统直接安装。如果是普通用户可以选择bioconda安装。
```shell
mamba install -y apptainer
```

## 4 使用apptainer安装软件
**安装ubuntu镜像**
```shell
#下载镜像
apptainer pull ubuntu.sif docker://ubuntu:latest
#创建沙盒
apptainer build --sandbox --fakeroot  ubuntu ubuntu.sif
#进入沙盒
apptainer shell --writable --fakeroot ubuntu
#安装软件
apt update
apt install -y bwa
apt install -y bwa
apt install -y samtools 
apt install -y bcftools
apt install -y ncbi-blast+
apt install -y bedtools
apt install -y seqtk
apt install -y minimap2
apt install -y bowtie2
```
**打包软件**
```shell
#打包软件
apptainer build --fakeroot bio.sif ubuntu
```
**运行软件**
```shell
./bio.sif bwa
./bio.sif samtools
```
**利用Apptainer安装google deepvariant**
```shell
apptainer pull docker://google/deepvariant
```