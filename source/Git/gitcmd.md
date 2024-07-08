# Frequently used git commands

date: 2022-04-22 17:48:28

## Create a git repository

```sh
git init
```

## Set the name and email

Globally

```shell
$ git config --global user.name <USER_NAME>
$ git config --global user.email <EMAIL>
```

Locally

```shell
$ git config --local user.name <USER_NAME>
$ git config --local user.email <EMAIL>
```

## Existing configurations

use command

```shell
$ git config --list
```

To get a specific configuration, use command `git config <CONFIG_NAME>`, e.g.

```shell
$ git config user.name
```

## To get help

use command like this, `git help <KEYWORD>`, e.g.

```shell
$ git help config
```

## Check logs

```shell
# Check last 4 git logs by printing each log in one line
git log --oneline --graph -4
# Check last one log, w/o modified files
git log -1
# Check last one log, w/ modified files
git log -1 --name-only
# Check last one log, w/ added/modified/deleted files
git log -1 --name-status
# Show commits before/after/between data(s)
git log --oneline --after="2022.06.09" --before="2022.06.12"
git log --oneline --since="2022.06.09" --until="2022.06.12"
git log --oneline --after="2022.06.09"
git log --oneline --since="2022.06.09"
git log --oneline --before="2022.06.12"
git log --oneline --until="2022.06.12"
```

## Add & Commit

If you add a new file which hasn't been tracked before in the repository,
first you have to put this file into the so-called "staged area", using command below,

```shell
git add <FILE_NAME>
```

If you have already modified a file which has been tracked before in the repository,
you also have to put file into the so-called "staged area", using the command below (indeed same as the command above),

```shell
git add <FILE_NAME>
```

After you have put the file (newly added or already be tracked in repo), you put file(s) into (local) repository using the command below,

```shell
git commit
```

## Differences (`git diff`)

If you modify a file, you can tell the difference by the command below,

```shell
git diff
```

If you have already put the file(s) into the staged area, you will see nothing by 'git diff'.
This time, you should use the command below to tell the differences,

```shell
git diff --cached
git diff --staged  --> git version >= 1.61
```

Use a tool to check the differences of files,

```shell
# full
git difftool --tool=tkdiff
# short
git difftool -t <tool_name>
```

To see all the differences in current branch and master branch, use command below to output those differences,

```shell
git format-patch -M master -o <OUTPUT_DIR>
```

## Patch a branch

To patch the current branch with `*.patch` files, use command,

```shell
git am ~/<SOME_DIR>/*.patch
```

## Create/Delete branch

To create a new branch from current master branch, use command,

```shell
git checkout -b <BRANCH_NAME> master
```

To remove/delete a branch (git branch), use command

```shell
git branch -d <BRANCH_NAME>
```

If there's anything not fully merged, git will stop the deletion. Use force command to do it (if confirmed to delete),

```shell
git branch -D <BRANCH_NAME>
```

## Clean untracked files

One way to remove untracked files is,

(1) To see all the untracked files,

```shell
git clean -n
```

Note here the option `-n` is very important, it just shows files untracked, no deleting

(2) Clean if all the files listed above are supposed to be removed,

```shell
git clean -f
```

## Remove unstaged files

To remove unstaged files, use commands below,

(1)    For a specific file use:

```shell
git checkout <PATH_TO_FILE_TO_REVERT>
```

(2)    For all unstaged files use:

```shell
git checkout -- .
```

## Rename a branch

```shell
git branch -m <OLD_BRANCH_NAME> <NEW_BRANCH_NAME>
```

## Rebase a branch

1. Switch to a branch which need rebase

```shell
git checkout <DEV_BRANCH>
```

2. Rebase

```shell
git rebase master
```

## Show origin information

```shell
$ git remote
$ git remote -v
$ git remote show origin
```

## Move a file

```shell
git mv <OLD_FILE> <NEW_FILE>
```

By moving files with git, we notify git about two things

(1) The hello.html file was deleted.

(2) The lib/hello.html file was created.

Both facts are staged immediately and ready for a commit. Git status command reports the file has been moved.

## Git aliases

Equals to `git checkout`

```shell
$ git config --global alias.co checkout
```

Equals to `git branch`

```shell
$ git config --global alias.br branch
```

Equals to `git commit`

```shell
$ git config --global alias.ci commit
```

Equals to `git status`

```shell
$ git config --global alias.st status
```

## Steps to create branch & push

Create a new branch in local and then push it to the remote (GitHub) and then track it

```shell
# 1. Create a new branch in local
git branch <NEW_BRANCH_NAME>
# 2. Get the remote repo name
git remote
# 3. Push the new branch to remote repo
git push <REMOTE_REPO_NAME> <NEW_BRANCH_NAME>
# Usually remote repo name is 'origin'
git push origin <NEW_BRANCH_NAME>
# 4. Connect this new local branch with the new branch just pushed to the remote repo
git branch --set-upstream-to=origin/<NEW_BRANCH_NAME>
# 5. After that, modify code and push as usaul
git add -A
git commit -m "XXXXX"
git push (or use git push origin <NEW_BRANCH_NAME>)
```

## Remove files and restore files

Reference website [git 删除文件与恢复](https://www.jianshu.com/p/c3ff8f0da85e)

- A file was deleted locally by `shell` commands other than `git` commands, but it was not added to the stage area, use `checkout` option to restore
  
  ```shell
  # Remove a file locally by shell commands
  rm <FILE>
  # Restore the file
  git checkout -- <FILE>
  ```

- A file was deleted locally by `shell` commands other than `git` commands, and it **was** added to the stage area, first use `reset` command to rollback the file to the status of locally removed, and then use `checkout` option to restore
  
  ```shell
  ##### 1st situation
  # Remove a file locally by shell commands
  rm <FILE>
  # Add to staged area (deleted)
  git add <FILE>
  # Rollback
  git reset HEAD <FILE>
  # Restore the file
  git checkout -- <FILE>
  
  ##### 2nd situation
  # Remove a file locally by git command which will add it to staged area (deleted)
  git rm <FILE>
  # Rollback
  git reset HEAD <FILE>
  # Restore the file
  git checkout -- <FILE>
  ```

- A file was deleted locally either by `shell` commands or `git` commands, and it **was** not only added to the stage area, but also committed to local repository, then we need to use `reset --hard <ID>` to rollback (ID is got by using `git log` command)
  
  ```shell
  ##### 1st situation
  # Remove a file locally by shell commands
  rm <FILE>
  # Add to staged area (deleted)
  git add <FILE>
  # Commit
  git commit -m "Delete a file"
  # Get the version ID by using the log option
  git log --pretty=oneline
  # Rollback
  git reset --hard <ID>
  
  ##### 2nd situation
  # Remove a file locally by git command which will add it to staged area (deleted)
  git rm <FILE>
  # Commit
  git commit -m "Delete a file"
  # Get the version ID by using the log option
  git log --pretty=oneline
  # Rollback
  git reset --hard <ID>
  ```

- A file was deleted locally either by `shell` commands or `git` commands, and it **was** not only committed to the local repository, but also push to the remote repository (e.g., Github), then following the steps above, and the use `git push -f`to push the restored files back to the remote repository. Note here `-f` is a must, because git doesn't allow lower versions override higher versions.
  
  ```sh
  ##### 1st situation
  # Remove a file locally by shell commands
  rm <FILE>
  # Add to staged area (deleted)
  git add <FILE>
  # Commit
  git commit -m "Delete a file"
  # Get the version ID by using the log option
  git log --pretty=oneline
  # Rollback
  git reset --hard <ID>
  # Push to remote
  git push -f
  
  ##### 2nd situation
  # Remove a file locally by git command which will add it to staged area (deleted)
  git rm <FILE>
  # Commit
  git commit -m "Delete a file"
  # Get the version ID by using the log option
  git log --pretty=oneline
  # Rollback
  git reset --hard <ID>
  # Push to remote
  git push -f
  ```

## Change repository's fetch origin

如何修改当前本地的repository目录对应的`fetch origin`

```bash
### Check current fetch & push orign
Pyrad@SSEA $ git remote -v
origin  git@github.com:Pyrad/cpp11.git (fetch)
origin  git@github.com:Pyrad/cpp11.git (push)
origin  git@gitee.com:pyrad/cpp11.git (push)

### Delete current fetch origin
Pyrad@SSEA $ git remote set-url --delete origin git@github.com:Pyrad/cpp11.git

### Check current fetch & push orign again
Pyrad@SSEA $ git remote -v
origin  git@gitee.com:pyrad/cpp11.git (fetch)
origin  git@gitee.com:pyrad/cpp11.git (push)

### Add another repo URL as PUSH origin
Pyrad@SSEA $ git remote set-url --add origin git@github.com:Pyrad/cpp11.git

### Check current fetch & push orign at last
Pyrad@SSEA $ git remote -v
origin  git@gitee.com:pyrad/cpp11.git (fetch)
origin  git@gitee.com:pyrad/cpp11.git (push)
origin  git@github.com:Pyrad/cpp11.git (push)
```

注意，目前多个`fetch`的`origin`是不允许的，所以如果在没有删除旧的`fetch origin`之前，就直接添加新的，会报错，错误信息如下。

```bash
$ git remote set-url origin git@gitee.com:pyrad/cpp11.git
warning: remote.origin.url has multiple values
fatal: could not set 'remote.origin.url' to 'git@gitee.com:pyrad/cpp11.git'
```

## Set editor when committing

修改`git`提交`commit`时所使用的编辑器

```bash
$ git config --global core.editor "vim"
```

## Change last commit message

修改最后一次提交的commit信息

```bash
$ git commit --amend
```

## Change history commit message

[我想试试教会你如何修改Git提交信息](https://blog.csdn.net/itartisans/article/details/131564377)

1. 首先需要退回到需要修改的commit之前的一个commit

    ```shell
    git rebase -i <hash_id_before_commit_to_edit>
    ```

    比如，

    ```shell
    git rebase -i ba4afdc957468f42d960e322047f6b4fc1dea427
    ```


2. 指向了上述命令之后，会打开一个临时文件，这个文件上部会列出来当前提交之后的所有的提交信息，顺序是按照时间顺序由早到晚排序的。
    
    每个提交信息的前面有字段代表需要执行的操作，具体选项在这个临时文件的下部有说明。
    
    常用的包括 `pick`，修改时使用的 `reword` 和 `edit`。`reword` 和 `edit` 的区别是 `reword` 提交后会自动合并，所以只能编辑提交信息，而 `edit` 提交后会停留在修改的提交，之后可以通过 `--amend` 修改提交内容。
    
    在需要修改的commit前面把 `pick` 修改为 `reword`，然后保存（或许不需要退出？），此时就会打开另外一个临时文件，这第二个临时文件展示的就是指定的要修改的提交的内容，此时修改提交内容之后，保存退出即可。

3. 之后要记得用 `git rebase --continue`，将head重新指向最新的commit。
4. 之后使用 `git push`（或者 `git push --force`）推送到远程仓库中。

其他参考文章

- [git修改历史提交(commit)信息](https://blog.csdn.net/A_man_of_ideas/article/details/130919624)


## Git to show messages of only one commit

Only show the names of files modified, w/o diff

```shell
git show SHA_COMMIT_KEY --name-only
```


## Permenantly delete commits after a commit number

[Answer in Stack Overflow](https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit)

This will destroy any local modifications after 0d1d7fc32 (0d1d7fc32 is not destroyed)

Don't do it if you have uncommitted work you want to keep.

```shell
git reset --hard 0d1d7fc32
```

Alternatively, if there's work to keep
```shell
git stash
git reset --hard 0d1d7fc32
git stash pop
```

This saves the modifications, then reapplies that patch after resetting.

You could get merge conflicts, if you've modified things which were changed since the commit you reset to.

## Git cheat-sheet from GitLab

[git-cheat-sheet.pdf](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)

## Git Reset Soft

Going back to HEAD

```shell
git reset --soft HEAD
```

Going back to the commit before HEAD

```shell
git reset --soft HEAD^
```

or equivalent

```shell
git reset --soft HEAD~1
```

Going back to 2 commits before HEAD

```shell
git reset --soft HEAD~2
```



## Use a stash for temp backup

[A practical guide to using the git stash command | Opensource.com](https://opensource.com/article/21/4/git-stash)

If you have some files modified in current branch, but suddenly you want to switch to other branches with a clean directory (no modified file), then you can use `git stash`.

Save your current modified files to a stash

```shell
git stash
```

or,

```shell
git stash save "My temp modified files"
```

or,

```shell
git stash push -m "My temp modified files"
```

Note, this only saves the files being tracked, if there's any file which is not tracked by the git (i.e., newly added), option `--include-untracked` (or `-u` for short) could be used to save that files,

```shell
git stash push --include-untracked -m "My temp modified files"
git stash push -u -m "My temp modified files"
```

To check how many stashes you have,

```shell
git stash list
```

This might show something like this,

```shell
stash@{0}: WIP on dev: 40d943c63b Fix a bug
stash@{1}: WIP on dev: f0000c6066 Update code format
```

To show a diff summary of a specific stash, for example, to check `stash@{0}`

```shell
git stash show stash@{0}
```

This will show something like this,

```shell
 src/array.cpp          |  2 +-
 src/geom.cpp           | 37 +++++++++++++--------------
 2 files changed, 19 insertions(+), 20 deletions(-)
```

To bring up your code from a specific stash, for example, retrieve code from `stash@{0}`

```shell
git stash apply stash@{0}
```

The above command will not remove the stash. If you want to remove it from the stash list, use `pop` instead as the following,

```shell
git stash pop stash@{0}
```

To show detailed diff, use `--patch` or `-p` flag together with `show` option.

```shell
git stash show stash@{0}
git stash show stash@{0} --patch
```

To show files in a stash, stash `0` for example, use `-u` option or `--include-untracked`. To include untracked files, version >= 2.32.

```shell
git stash show -u 0
```

## Git show untracked files as a list

```shell
git ls-files --others --exclude-standard
```

This will output a list of files that are not tracked by Git and are not ignored by .gitignore or other exclude files.

You can also use the -z option to separate the file names with null characters instead of newlines.

This can be useful if you want to pipe the output to xargs or other commands that can handle null-delimited input. For example:

```shell
git ls-files -z --others --exclude-standard | xargs -0 rm
```

This will delete all untracked files that are not ignored by Git.


## Resolve conflicts when merging from another branch

once conflict occurs after `git merge $branch_name`, it will show what file has conflicts, and it needs to be resolved before merged.

Just open that file using `vi` or other text editor, and find conflict marker `<<<<<<<<`. Then fix the conflicts.

After conflicts are resolved, just add that file(s) by using

```shell
git add .
```

Then commit it by using

```shell
git commit
```

Now it seems like below,

```shell
 1 Merge branch 'master' into dev
 2                                                                                 
 3 # Conflicts:                                                                    
 4 #       src/array.cpp
 5 #                                                                               
 6 # It looks like you may be committing a merge.                                  
 7 # If this is not correct, please remove the file                                
 8 #       .git/MERGE_HEAD                                                         
 9 # and try again.                                                                
10                                                                                 
11                                                                                 
12 # Please enter the commit message for your changes. Lines starting              
13 # with '#' will be ignored, and an empty message aborts the commit.             
14 #                                                                               
15 # On branch allangle                                                            
16 # All conflicts fixed but you are still merging.                                
17 #                                                                               
18 # Changes to be committed:                                                      
19 #       modified:   src/array.hpp
```

It reminds you that current you are committing a merge.

Save and commit, then it's done.

## The simplest way to list conflicted files in Git

[What's the simplest way to list conflicted files in Git?](https://stackoverflow.com/questions/3065650/whats-the-simplest-way-to-list-conflicted-files-in-git)

```shell
git diff --name-only --diff-filter=U --relative
```


## Get rid of '... does not point to a valid object' for an old git branch

[Stack Overflow - Get rid of ...](https://stackoverflow.com/questions/6265502/getting-rid-of-does-not-point-to-a-valid-object-for-an-old-git-branch)


Clean up all of the missing refs by using the following commands (bash)

```shell
git for-each-ref --format="%(refname)" | while read ref; do
    git show-ref --quiet --verify $ref 2>/dev/null || git update-ref -d $ref
done
```

Refer to [git-for-each-ref](https://git-scm.com/docs/git-for-each-ref) and [git-show-ref](https://git-scm.com/docs/git-show-ref) for more details.


## Git repo control line ending styles

[Git End-of-Line Issues](https://learn.openwaterfoundation.org/owf-learn-git/eol/)


## Not possible to fast-forwad, aborting

参考链接：[git - Error "Fatal: Not possible to fast-forward, aborting" - Stack Overflow](https://stackoverflow.com/questions/13106179/error-fatal-not-possible-to-fast-forward-aborting)


一般情况下，如果本地的repo进行了修改，commit了，但没有push，同时remote又已经接受了其他repo的commit push，那么本地的repo在做push的时候就会出现类似下面的问题，

```shell
To github.com:Pyrad/pyradnotes.git
! [rejected] master -> master (fetch first)
error: failed to push some refs to 'github.com:Pyrad/pyradnotes.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See 'Note about fast-forwards' in 'git push --hlep' for details.
```

如果此时再执行 `git pull`，并且当前的策略设置是 `fast-forwards`，那么就会出现如下问题，

```shell
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 42.36 KiB | 116.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
fatal: Not possible to fast-forward, aborting.
```

为了临时解决这个问题，可以使用 `--no-ff` 选项，临时避开这个问题，

```shell
git pull --no-ff
```

此时再查看当前repo的状态，就会发现存在没有push到remote的commits，

```shell
git status

On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (Use "git push" to publish your local commits)

nothing to commit, working tree clean.
```

此时在使用 `git push` ，把当前repo中还没提交的commit再提交即可。

## How to handle git gc fatal: bad object refs/remotes/origin/HEAD error?

[How to handle git gc fatal: bad object refs/remotes/origin/HEAD error?](https://stackoverflow.com/questions/37145151/how-to-handle-git-gc-fatal-bad-object-refs-remotes-origin-head-error)

比如，如果有如下的报错，

```shell
fatal: bad object refs/tags/m_handoff-latest-merged
error: XXXX did not send all necessary objects
```


一般情况，只需要把报告出来的 `refs/tags/m_handoff-latest-merged` 删除（或移动至其他不使用的位置）即可。

```shell
mv .git/refs/tags/m_handoff-latest-merged /tmp
```

产生问题的原因是，remote端的这个branch/tag已经被删除（重命名）了，但本地还是指向之前的branch/tag，因此产生不一致。

## Git pull error did not send all necessary objects

（似乎和上一条重复？2024年7月8日23:02:45）

[BitBucket Git Error: did not send all necessary objects - StackOverflow](https://stackoverflow.com/questions/8788975/bitbucket-git-error-did-not-send-all-necessary-objects)

可以按照其中第一个回答，把报错的那个文件删除掉，然后再 `git pull` 即可

```shell
rm .git/refs/remotes/origin/<name of branch>
```
