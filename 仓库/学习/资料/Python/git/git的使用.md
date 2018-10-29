### 工作区&暂存区&仓库区

![](./images/git_main.png)

1. 工作区

   > 对于` 添加`、` 修改`、`删除` 文件的操作，都发生在工作区中

2. 暂存区

   > 暂存区指将工作区的操作完成小阶段的存储，是版本库的一部分

3. 仓库区

   > 仓库区表示个人开发的一个小阶段的完成
   > 	仓库区中记录的各版本是可以查看并回退的
   >
   > ​	但是在暂存区的版本一旦提交就再也没有了

### git安装

`sudo apt-get install git`

### git常用命令

1. 创建仓库
   `git init`

2. 配置个人信息
   `git config user.name 张国鹏`
   `git config user.email 3gii@sina.cn`

3. 查看文件状态
   `git status`  文件有变动未提交到暂存区时，文件名为红色

4. 将工作区文件添加到暂存区
   `git add .` 或` git add login.py`  文件名由红色变成绿色

5. 将暂存区文件提交到仓库

   * commit会生成一条版本记录
   * -m 后面是版本描述信息
     `git commit -m '版本描述' ` 
   * 添加和提交合并命令
     `git commit -am '版本描述'` 

6. 查看历史版本

   * ` git log`  
     不能查看已经删除了的commit记录
   * `git reflog `  
     可以查看所有分支的所有操作记录（包括commit和reset的操作），包括已经被删除的commit记录。

7. 回退版本

   * 方案一
     * `HEAD`表示当前最新版本
     * `HEAD^` 表示当前最新版本的前一个版本
     * `HEAD^^` 表示当前最新版本的前两个版本，以此类推...
     * `HEAD~1`表示当前最新版本的前一个版本，以此类推...
       `git reset --hard HEAD^`
   * 方案二
     * 通过版本号回退到指定的版本
       `git reset --hard 版本号` 

8. 撤销修改

   * 只能撤销工作区、暂存区的代码、不能撤销仓库区的代码

   * 撤销仓库区的代码就相当于回退版本操作

     * 撤销工作区的代码
       `git checkout 文件名 `

     * 撤销暂存区代码

       `git reset HEAD 文件名`  # 将暂存区的代码撤销到工作区
       `git checkout 文件名`       # 撤销工作区代码

9. 对比版本号

   * 对比版本库与工作区
     * `git diff HEAD -- 文件名`
   * 对比版本库
     `git diff HEAD HEAD^ -- 文件名`

10. 删除文件

    * 确定删除

      ```shell
      rm 文件名
      git rm 文件名
      git commit -m 删除描述
      ```

      

    * 误删除

      ```shell
      rm 文件名
      git checkout -- 文件名
      ```

### 远程仓库GitHub

1. 克隆远程仓库的命令
   `git clone url`

2. 拉取代码
   `git pull`

3. 推送到远程仓库
   `git push`

4. 设置密码

   ```shell
   # 设置记住密码（默认15分钟）
   git config --global credential.helper cache
   # 设置密码有效时间（1小时后失效）
   git config credential.helper 'cache --timeout=3600'
   # 长期存储密码
   git config --global credential.helper store
   ```

   

5. 标签

   * 在本地打标签
     `git tag -a 标签名 -m 标签描述`

   * 推送标签到远程仓库

     `git push origin 标签名`

   * 删除标签
     `git tag -d 标签名` # 删除本地标签

     `git push origin --delete tag 标签名`

6. 分支

   * 查看当前分支

   * 创建并切换到分支

   * 设置本地分支跟踪远程指定分支（将分支推送到远程）
     `git push -u origin dev`

   * 合并分支到master分支

     ```shell 
     # 切换到master
     git checkout master
     # 合并
     git merge dev
     # 推送到远程
     git push
     ```

     


 