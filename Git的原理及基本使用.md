# Git 的原理及基本使用
## 一、Git的原理
### 1.什么是Git
由于Git是分布式的版本库，所以Git完全可以在没有网络的情况下使用，每个人的开发机都可以作为一个独立的版本库存在，开发者可以在自己的开发机管理代码版本，而不依赖于远程版本库。
![](https://huatu.98youxi.com/markdown/work/uploads/upload_bb863e6d2f242e917a64c38374749107.jpg)


Git跟传统的代码管理器（如:svn）不同， 主要区别在于git多了个本地仓库以及缓存区，所以即使无法联网也一样能提交代码。

工作区间: 即我们创建的工程文件， 在编辑器可直观显示；

缓存区: 只能通过git GUI或git shell 窗口显示，提交代码、解决冲突的中转站；

本地仓库: 只能在git shell 窗口显示，连接本地代码跟远程代码的枢纽，不能联网时本地代码可先提交至该处；

远程仓库: 即保存我们代码的服务器。

## 二、Git的基本使用
### 1.Git配置
* 配置用户信息
```
git config --global user.name "xgfdmv"
git config --global user.email "2096055435@qq.com"
```
* 配置查询
```
git config --list    > [查询git所有配置]
git config user.name    > [查询git的user.name的值]
```
### 2.git创建仓库
git创建仓库后,会在目录下生成 .git 文件夹,git所有的数据和资源都在此目录中
* git init方式
```
git init    > [在./当前目录下创建git库]
git init [文件夹]    > [在指定文件下创建git库]
git add .    > [添加当前目录下所有文件，进入暂缓区，进行版本管理]
git commit -m "提交备注"    > [将暂存区文件快照提交到版本库]
```
* git clone方式
```
git clone <repo>    > [克隆远程仓库到当前目录中]
git clone <repo>  <directory>     > [克隆远程仓库到指定目录中]
```
### git的提交和修改
* git add命令
添加文件到暂存区
```
git add [file]    > [添加file到暂存区中]
git add [dir]    > [添加[dir]目录下所有文件/目录到暂存区中]
git add .     > [添加当前目录下所有文件/目录到本地库]
```
* git status命令
查看仓库当前的状态，显示有变更的文件
```
git status    > [用于查看工作区文件是否被修改]
```
* git diff命令
比较文件的不同
```
git diff [file]    > [查看暂存区和工作区文件区别]
git diff --cached file    > [查看暂存区file和版本库file的区别]
git diff HEAD    > [查看暂存区和版本库中所有文件区别]
```
* git commitd命令
提交暂存区到版本库
```
git commit -m [message]    > [提交暂存区文件到版本库]
git commit -a     > [直接提交工作区修改的文件到版本库，跳过git add]
```

* git reset命令
回退版本
```
git reset cid    > [和mixed等价]
git reset --mixed cid    > [回退版本库到制定的commit id, 并且将回退代码放到工作区]
git reset --soft cid    > [回退版本库到制定的commit id, 并且将回退代码放到暂存区]
git reset --hard cid    > [回退版本库到制定的commit id, 并且同步到工作区和暂存区]
```
* HEAD说明
HEAD           表示当前版本
HEAD^          表示上一个版本
HEAD^^         表示上上个版本
HEAD^^^        表示上上上个版本
HEAD~0         表示当前版本
HEAD~1         表示上个版本
HEAD~2         表示上上个版本
HEAD~3         表示上上上个版本

### git远程操作
* git remote命令
远程操作仓库
```
git remote    > [查询所有远程仓库]
git remote rm name    > [删除远程仓库]
```
### SSH公钥和私钥生成
```
$ ssh-keygen -t rsa -C "2096055435@qq.com"    > [在.ssh文件下生成id_rsa和id_rsa.pub,在GitHub是添加后者]
```
### 写Python程序并推送到远程仓库
```
$ vim test.py
$ git add test.py
$ git commit -m "message"
$ git push
```


