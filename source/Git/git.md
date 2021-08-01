# 恢复一个已经在GitHub上的提交中被删除的文件

1. 找到当时被删除文件对应的提交

   ```shell
   git log --diff-filter=D --summary
   ```

2. 使用如下命令checkout出来当时对应的被删除的文件

   ```shell
   git checkout $commit~1 path/to/file.txt
   ```

   这里的```$commit```是对应的提交ID（hash），后面的```~n```表示追溯某个提交的第```n```个祖先。

   所以这里的```~1```表示找到删除这个文件的提交的上一个提交中对应的问。