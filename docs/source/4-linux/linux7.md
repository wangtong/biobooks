# 4.7 编写脚本以及运行脚本
## 1 什么是脚本
脚本：Scripts指表演戏剧、拍摄电影等所依据的底本或书稿的底本，简写为sh。脚本可以分为交互式（Interactive）执行与批处理（batch）。在生物信息分析中，将执行的一条或多条命令保存在一个文件中，称为脚本文件，脚本文件可以记录运行的命令状态，并且便于分享，而且可以自动化运行多个命令。
脚本五要素：
1.	软件：软件写在第一位
2.	输入内容：可以是文件，也可以是命令行输入。
3.	输出内容：可以屏幕输出，也可以保存到文件内。
4.	选项参数：通过单个连字符的短选项-，或者两个连字符的长选项--
5.	日志：记录软件运行信息及错误信息，便于排错，通过重定向保存。

## 2 vim编辑脚本
### 2.1 打开文件

vim是Linux系统自带的文本编辑器，可以理解成为windows系统下的word软件。
vim scripts.sh 
i a u 切换为插入模式
ESC切换为命令模式
按“i”切换进入插入模式insert mode，从光标当前位置开始输入文件；
按“a”进入插入模式后，是从目前光标所在位置的下一个位置开始输入文字；
按“o”进入插入模式后，是插入新的一行，从行首开始输入文字。

### 2.2 如何退出 vim？ 

按ESC将vim从插入模式或者visual模式切换为命令模式。首先按 esc 键切换到命令模式 然后按“shift+：”冒号表示可以输入命令了 然后按 
q！不保存退出 
wq 保持退出或者 x 保存退 
w+文件名 另存为一个文件

### 2.3移动光标

vi可以直接用键盘上的光标来上下左右移动，但正规的vi是用小写英文字母h、j、k、l，分别控制光标左、下、上、右移一格。

　　按ctrl+b：屏幕往"后"移动一页。
　　按ctrl+f：屏幕往"前"移动一页。
　　按ctrl+u：屏幕往"后"移动半页。
　　按ctrl+d：屏幕往"前"移动半页。
　　按数字0：移到文章的开头。
　　按G：移动到文章的最后。
　　按$：移动到光标所在行的"行尾"。
　　按^：移动到光标所在行的"行首"
　　按w：光标跳到下个字的开头
　　按e：光标跳到下个字的字尾
　　按b：光标回到上个字的开头
　　按#l：光标移到该行的第#个位置，如：5l,56l。

### 2.4删除文字

```
    x：每按一次，删除光标所在位置的"后面"一个字符。
　　#x：例如，6x表示删除光标所在位置的"后面"6个字符。
　　X：大写的X，每按一次，删除光标所在位置的"前面"一个字符。
　　#X：例如，20X表示删除光标所在位置的"前面"20个字符。
　　dd：删除光标所在行。
　　#dd：从光标所在行开始删除#行
```

### 2.5复制

```
　　yw：将光标所在之处到字尾的字符复制到缓冲区中。
　　#yw：复制#个字到缓冲区
　　yy：复制光标所在行到缓冲区。
　　#yy：例如，6yy表示拷贝从光标所在的该行"往下数"6行文字。
　　p：将缓冲区内的字符贴到光标所在位置。注意：所有与"y"有关的复制命令都必须与"p"配合才能完成复制与粘贴功能。
```

### 2.6替换

```
　　r：替换光标所在处的字符。
　　R：替换光标所到之处的字符，直到按下ESC键为止。
```

### 2.7回复上一次操作

```
u：命令模式下，按u，后退
ctrl+R：命令模式下，前进
```

### 2.8 更改

　

```
  　cw：更改光标所在处的字到字尾处
　　c#w：例如，c3w表示更改3个字
```

### 2.9跳至指定的行

```
　　ctrl+g列出光标所在行的行号。
　　#G：例如，15G，表示移动光标至文章的第15行行首。
```

## 3 vim配置

vim配置文件在家目录下创建一个.vimrc文件即可。

```
$ vim ~/.vimrc #以下内容选择性设置即可

filetype on #支持不同文件扩展名不同语法高亮
syntax on  #语法高亮  
set autoindent  #自动缩进 
set nu  #设置行号
set tabstop=4 #Tab缩进数目
set softtabstop=4
set expandtab
set shiftwidth=4
set ruler # 设置标尺
set backspace=indent,eol,start
set backspace=2 
set expandtab  #设置自动缩进 
set cindent shiftwidth=4  缩进的字符个数 
set foldcolumn=4  #设置折叠模式
```

