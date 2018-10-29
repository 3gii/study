### Flask-Script
1. 安装
    `pip install flask-script`
2. 集成Flask-Script
    ```python
    from flask import Flask
    from flask-script import Manager

    app = Flask(__name__)

    # 将Manager类与应用实例进行关联
    manager = Manager(app)

    # @manager.command
    # def init():
    #     print('初始化完成')
    # > python manager.py init

    # script_conf.py
    # DBManager = Manager(app)
    # @manager.command
    # def init():
    #     print('初始化完成') 
    # 
    # manager.py
    # from script_conf.py import DBManager
    # ...
    # manager.add_command('db', DBManager)
    # > python manager.py db init

    if __name__ == '__main__':
        manager.run()
    ```
    > 运行：python manager.py runserver
    > 查看帮助信息：python manager.py runserver --help