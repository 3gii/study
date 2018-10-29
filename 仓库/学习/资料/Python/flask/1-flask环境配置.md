### 虚拟环境
1. 安装虚拟环境

    * 第一种方法
        * `pip install virtualenv`
    * 第二种方法
        * `pip install virtualenv`
        * `pip install virtualenvwrapper`

2. 创建虚拟环境
    * 第一种方法
        - 虚拟环境会创建在当前目录
        * Python2
            `virtualenv 虚拟环境名` 
        * Python3
            `virtualenv -p python3 虚拟环境名`
    * 第二种方法
        - 虚拟环境会创建在，`virtualenvwrapper`工作目录
        - 可以在`~/.bashrc`中指定, 运行`source ~/.bashrc`

            `export WORKON_HOME=$HOME/.virtualenvs`

            `source /usr/local/bin/virtualenvwrapper.sh`
        * Python2
            `mkvirtualenv 虚拟环境名`
        * Python3
            `rmvirtualenv -p python3 虚拟环境名`

3. 激活虚拟环境
    * 第一种方法
        * Windows 进入`virtualenv`安装目录的`script`目录，运行`activate`
        * Linux 进入`virtualenv`安装目录的`script`， `source activate` 或直接使用绝对路径
    * 第二种方法
        * 查看虚拟环境
            `workon`
        * 激活虚拟环境
            `workon 虚拟环境名`
        * 退出虚拟环境
            `deactivate`
        * 删除虚拟环境
            `rmvirtualenv 虚拟环境名`

4. 导出Python依赖包

    * `pip freeze > 依赖包名`

5. 导入Python依赖包

    * `pip install -r 依赖包名`

