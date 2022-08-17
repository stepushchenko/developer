# Git
Это распределенная система контроля версий, то есть - это система, записывающая <br>
изменения в файл или набор файлов в течение времени и позволяющая вернуться <br>
позже к определённой версии. Мы хотим гибко управлять некоторым набором файлом, <br>
откатываться до определенных версий в случае необходимости. Можно отменить те <br>
или иные изменения файла, откатить его удаление, посмотреть кто что поменял. <br>
Как правило, системы контроля версий применяются для хранения исходного кода, <br>
но это необязательно. Они могут применяться для хранения файлов совершенно любого типа. <br>
Такая Система контроля версий помогает отслеживать изменения, внесённые в базу кода.  <br>
Более того, Система записывает, кто внёс изменения и может восстановить стёртый <br>
или изменённый код.

Перезаписанных кодов не существует, поскольку Git сохраняет несколько копий в хранилище, <br>
то есть говоря простым языком, если вы решили накосячить где-нибудь на проекте внеся <br>
свои изменения, то можно вернуть в рабочее русло исправный билд проекта.

`https://gitexplorer.com/ `Git Command Explorer

### Setup
```bash
# Set the name and email that will be attached to your commits and tags
git config --global user.name "<user name>"
git config --global user.email "<user email>"
```

### Start project
```bash
# Create a local repo to initialise the current directory as a git repo
git init "<directory>"

# Download a remote repo
git clone "<url>"
```

### Make a change
```bash
# Add a file to staging
git add "<file>"

# Stage all files
git add .

# Commit all staged files to the git
git commit -m "<commit message>"

# Add all changes made to thacked files and commit
git commit -am "<commit message>"
```

### Basic Concepts
**main:** default development branch <br>
**origin:** default upstream repo <br>
**HEAD:** current branch <br>
**HEAD^:** parent of HEAD <br>
**HEAD~4:** great-great greadparent of HEAD 

### Branches
```bash
# List all local branches. Add -r flag to show all remote branches. -a flag for all branches. <br>
git branch

# Create a new branch
git branch "<new-branch>"

# Switch to a new branch and update the working directory
git checkout "<branch>"

# Create a new branch and switch to it
git checkout -b "<branch>"

# Delete a merged branch
git branch -d "<branch>"

# Delete a branch, whether merged or not
git branch -D "<branch>"

# Add a tag to current commit (often used for a new version releases)
git tag "<tag-name>"
```

### Merging
```bash
# Merge branch A into branch B. Add --no-ff option for no-fast-forward merge
git checkout B
git merge A

# Merge  and squash all commits into one new commit
git merge --squash A
```

### Rebasing
```bash
# Rebase feature branch onto main (to incorporate new changes made to main).
# Prevents unnecessary merge commits into feature, keeping history clean.
git checkout feature
git rebase main

# Interatively clean up a branches commits before rebasing onto main <br>
git rebase -i main

# Interatively rebase the last 3 commits on current branch
git rebase -i Head~3
```

### Undoing Things
```bash
# Move and/or rename a file and stage move
git mv "<existing_path>" "<new_path>"

# Remove a file from working directory and staging area, then stage the removal
git rm "<file>"

# Remove from staging area only
git rm --cached "<file>"

# View a previous commit
git checkout "<commit ID>"

# Create a new commit, reverting the changes from a specified commit
git revert "<commit ID>"

# Go back to a previous commit and delete all commits ahead of it (rever it safer).
# Add --hard flag to also delete a workspace changes.
git reset "<commit ID>"
```

### Review your Repo
```bash
# List new or modified files not yet commited
git status

# List commit history, with respective IDs
git log --oneline

# Show changes to unstaged files. For changes to staged files, add --cached option.
git diff

# Show changes between two commits
git diff "<commit ID>" "<commit ID>"
```

### Stashing
```bash
# Store modified and staged changes.
# To include untracked files, add -u flag.
# For untracked and ignored files, add -a flag.
git stash # временно сохранить незакоммиченные изменения и убрать их из рабочей директории

# As above, but add a comment
git stash save "comment"

# Partial stash. Stash just a sing file,a collection of files,
# or individual changes from within files.
git stash -p

# List all stashes
git stash list

# Re-apply the stash without deleting it.
git stash apply

# Re-apply the stash at index 2, then delete if from the stash list.
# Omit stash@{n} to pop the most recent stash.
git stash pop stash@{2}

# Show the diff summary of stash 1. Pass the -p flag to see the full diff.
git stash show stash@{1}

# Delete stash at index 1. Omit stash@{n} to delete last stash made.
git stash drop stash@{1}

# Delete all stashes
git stash clear
```

### Synchronizing
```bash
# Add a remote repo
git remote add "<alias>" "<url>"

# View all remote connections. Add -v flag to view urls.
git remote

# Remove a connection
git remote remove "<alias>"

# Fetch all branches from remote repo (no merge)
git fetch "<alias>"

# Fetch a specific branch
git fetch "<alias>" branch

# Fetch the remote repo's copy of the current branch, then merge
git pull

# Move (rebase) your local changes onto the top of new changes made
# to the remote repo (for clean, linear history)
git pull --rebase "<alias>"

# Upload local content to remote repo
git push "<alias>"

# Upload to a branch (can then pull request)
git push "<alias>" "<branch>"
```