# 4.9 进程管理

Linux系统为多用户多任务系统，生物软件运行时要能够查看运行状态，实时监控软件运行状态，例如CPU，内存使用情况等，当运行出现错误时，要能够及时杀死任务，以及任务前后台切换，是否挂起等操作。

```shell
#查看系统运行状态 press "q" to exit   
top 

# press "Ctrl +C" to exit 

top -b    
top -c   
top -u "yourname"
#htop查看系统运行状态     
htop
#杀死进程  
kill -9 "process number"
#查看kill管理列表
kill -l
#暂停任务
kill-19 "process number"
#开始任务
kill -18 "process number"
#修改密码   
passwd
#休眠
sleep
# forehead 前台程序
fg
#background 前台程序   
bg
#查看后台进程  
jobs
#不挂起运行程序，关闭登录窗口后程序继续运行  
nohup
#忘记使用nohup之后，将后台任务转换为nohup
disown 
```
## 2 不间断会话
Linux系统可以使用screen与tmux命令实现不间断会话。
tmux（terminal multiplexer）是Linux上的终端复用神器，可从一个屏幕上管理多个终端。使用tmux，用户可以连接或断开会话，而保持终端在后台运行。也就是登录Linux之后，开始tmux，之后所有的操作都在tmux中完成，这样即使突然掉线了，所有的任务都还在tmux之中。
tmux的结构包括会话(session)、窗口(window)、窗格(pane)三部分，会话实质是伪终端的集合，每个窗格表示一个伪终端，多个窗格展现在一个屏幕上，这一屏幕就叫窗口。tmux的操作主要包括对会话、窗口、窗格的创建、关闭、重命名、连接、分离、选择等等。

```shell
#软件安装
mamba install -y tmux
```

快捷键
使用tmux需要经常使用快捷键，其中最常用的就是ctrl+b，因为Linux shell下很多快捷键都被占用了，只能这样操作了，每次先按一下ctrl+b，在使用对应的快捷键。注意ctrl+b是在tmux窗口中使用，在原始的shell命令行下不管用。下面列出一些最常用的快捷操作：
ctrl+b ?  :         显示快捷键帮助
ctrl+b d   :        脱离当前会话；这样可以暂时返回Shell界面，输入tmux attach能够重新进入之前的会话
ctrl+b 空格键 :     采用下一个内置布局，这个很有意思，在多屏时，用这个就会将多有屏幕竖着展示
ctrl+b !    :        把当前窗口变为新窗口
ctrl+b "    :       横向向分隔窗口
ctrl+b 上下键:      上一个及下一个分隔窗口
ctrl+b &  :         确认后退出当前tmux
ctrl+b c     :      创建新窗口
ctrl+b n     :      选择下一个窗口
ctrl+b l     :      最后使用的窗口
ctrl+b p     :      选择前一个窗口
ctrl+b w     :      以菜单方式显示及选择窗口
ctrl+b s      :     以菜单方式显示和选择会话。
ctrl+b t      :     显示时钟。然后按enter键后就会恢复到shell终端状态

tmux案例

```shell
#1  新建会话，命名为wget
tmux new -s wget

#2 运行命令
wget -c ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/swissprot.gz

#3 按ctrl+b，然后字母d，退出会话，任务仍在运行
$ tmux new -s wget
[detached]

#4 tmux ls查看任务
$ tmux ls
wget: 1 windows (created Wed Jul 24 10:22:34 2019) [114x26]

#5 重新进入wget终端，第一个参数a也可以写成attach，任务正在运行
tmux a -t wget

#6 关闭会话任务,如果在会话中使用ctrl + d，或者exit，就会在退出会话，也关闭了该会话
# tmux ls查看会话
$ tmux ls

#7 kill-session杀死会话，每个会话成为一个session
$ tmux kill-session -t wget

#8 关闭所有会话
$ tmux kill-server
```