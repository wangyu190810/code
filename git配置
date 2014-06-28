tongpao
======
>   This is a organizational website for tongpao. 

tongpao wiki
======
>   <a href='https://github.com/GreatmanBill/tongpao/wiki/tongpao%E4%BB%8B%E7%BB%8D'>tongpao介绍</a>

数据库:
======
>   数据库用mysql， 新建用户名:test， 密码:123456

安装git:
======
1. 在ubuntu或win7下自己安装好git
- 配置用户名和邮箱

    git config --global user.email "me@here.com"  
    git config --global user.name "me"

- 如我的配置:

    git config --global user.email "xiaobingzhang29@gmail.com"  
    git config --global user.name "xiaobing"


git 使用规则:
======
1. 生成SSH key 
    * 若是ubuntu  

        打开终端  
        使用: ssh-keygen -t rsa

    * 若是windows 

        打开git bash  
        使用: ssh-keygen -t rsa

    输入后，直接按三个回车就ok了，不要输入密码   

- 获得SSH key的公钥

    * 若是ubuntu 

        cd ~/.ssh  
        打开id_rsa.pub，全部复制，然后将这个用gmail邮箱发给我  

    * 若是windows    

        在你的自己的目录下，找到同样的目录，这个应该是隐藏文件,打开后，也是用你的gmail发给我    

- 发给我后，我把你们的key加入到我的信息里面去，你们就可以推送和拉取我的文件了

- 在本地建一个目录名为tongpao

    如: mkdir ~/workspace/tongpao

- 将项目拉到本地

    cd ~/workspace/tongpao  
    git pull git@github.com:GreatmanBill/tongpao.git

- 添加远程库的引用

    git remote add tongpao git@github.com:GreatmanBill/tongpao.git  
    查看效果: git remote -v  

    出现这样的就成功了:  
    
        tongpao git@github.com:GreatmanBill/tongpao.git (fetch)  
        tongpao git@github.com:GreatmanBill/tongpao.git (push)

- 之后，就可以使用简单的缩写来拉取代码了，如:

    * 拉数据回本地:

        git pull tongpao master

    * 推数据到远端:

        git push tongpao master

git 修改数据简单命令:
======
1. 添加需要提交的文件

    git add filename   
    该命令为:添加指定的文件进入提交状态， 点号 '.' 为当前目录，及其所有子目录文件都加入到提交状态   

- 提交修改的文件

    git commit -m 'commit messge'   
    该命令用于提交修改的文件到本地的库中，commit message为你对这些文件修改的简短的描述信息

- 将远端数据拉回本地，与本地数据合并

    git pull tongpao master

- 将本地的修改推送到远端

    git push tongpao master

- 查看当前文件的状态

    git status  
    这个可以在任何时候使用，可以查看当前的所有文件所处于的什么版本  
    git status -s  
    显示简短的说明

代码规范要求:
======
1. 所有写的函数名词推荐用'动词 + 名词'形式，如getUsersByGroupid() 

- 所有函数必须写注释
    python的注释写在函数内的第一句，并且对传入参数和返回值进行说明如:    

        def getUsersByGroupid(groupid):  
            """根据用户组来获得用户组下的所有用户信息   
               @param groupid 用户组id  
               @return 返回一个list，每一个子元素为一个dict，包括一个人用户信息   
            """ 

            pass    
    

- 所有变量名，除了部分迭代器变量i，j，k等，其他变量，必须根据实际的意思来命名，如: 

    users ->  用户

- 每两个函数之间空一行

- 返回语句前空一行，如:

        def function():  
            pass    
        
            return None 

- 写函数时，尽量一个方法不要超过60行，如果太多的话，可以考虑一下分开再写一个函数

- 在提交的时候，把提交的信息写好，这个对其他人把代码拉下来合并的时候，有个参照，不然，都不知道你写了些什么

- 如有好的建议，可以添在下面
