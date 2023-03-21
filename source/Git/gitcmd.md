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