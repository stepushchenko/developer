### Setup
Set the name and email that will be attached to your commits and tags <br>
`git config --global user.name "<user name>"` <br>
`git config --global user.email "<user email>"` 

### Start project
Create a local repo to initialise the current directory as a git repo <br>
`git init <directory>` <br>
Download a remote repo <br>
`git clone <url>`

### Make a change
Add a file to staging <br>
`git add <file>` <br>
Stage all files <br>
`git add .` <br>
Commit all staged files to the git <br>
`git commit -m "commit message"` <br>
Add all changes made to thacked files and commit <br>
`git commit -am "commit message"`

### Basic Concepts
**main:** default development branch <br>
**origin:** default upstream repo <br>
**HEAD:** current branch <br>
**HEAD^:** parent of HEAD <br>
**HEAD~4:** great-great greadparent of HEAD 

### Branches
List all local branches. Add -r flag to show all remote branches. -a flag for all branches. <br>
`git branch` <br>
Create a new branch <br>
`git branch <new-branch>` <br>
Switch to a new branch and update the working directory <br>
`git checkout <branch>` <br>
Create a new branch and switch to it <br>
`git checkout -b <branch>` <br>
Delete a merged branch <br>
`git branch -d <branch>` <br>
Delete a branch, whether merged or not <br>
`git branch -D <branch>` <br>
Add a tag to current commit (often used for a new version releases) <br>
`git tag <tag-name>`

### Merging 
Merge branch A into branch B. Add --no-ff option for no-fast-forward merge <br>
`git checkout B` <br>
`git merge A` <br>
Merge  and squash all commits into one new commit <br>
`git merge --squash A`

### Rebasing
Rebase feature branch onto main (to incorporate new changes made to main). <br>
Prevents unnecessary merge commits into feature, keeping history clean. <br>
`git checkout feature` <br>
`git rebase main` <br>
Interatively clean up a branches commits before rebasing onto main <br>
`git rebase -i main` <br>
Interatively rebase the last 3 commits on current branch <br>
`git rebase -i Head~3`

### Undoing Things
Move and/or rename a file and stage move <br>
`git mv <existing_path> <new_path>` <br>
Remove a file from working directory and staging area, then stage the removal <br>
`git rm <file>` <br>
Remove from staging area only <br>
`git rm --cached <file>` <br>
View a previous commit  <br>
`git checkout <commit ID>` <br>
Create a new commit, reverting the changes from a specified commit <br>
`git revert <commit ID>` <br>
Go back to a previous commit and delete all commits ahead of it (rever it safer). <br>
Add --hard flag to also delete a workspace changes. <br>
`git reset <commit ID>`

### Review your Repo
List new or modified files not yet commited <br>
`git status` <br>
List commit history, with respective IDs <br>
`git log --oneline` <br>
Show changes to unstaged files. For changes to staged files, add --cached option. <br>
`git diff` <br>
Show changes between two commits <br>
`git diff <commit ID> <commit ID>`

### Stashing
Store modified and staged changes.  <br>
To include untracked files, add -u flag. <br>
For untracked and ignored files, add -a flag.  <br>
`git stash` <br>
As above, but add a comment. <br>
`git stash save "comment"` <br>
Partial stash. Stash just a sing file,a collection of files, <br>
or individual changes from within files. <br>
`git stash -p` <br>
List all stashes <br>
`git stash list` <br>
Re-apply the stash without deleting it. <br>
`git stash apply` <br>
Re-apply the stash at index 2, then delete if from the stash list. <br>
Omit stash@{n} to pop the most recent stash. <br>
`git stash pop stash@{2}` <br>
Show the diff summary of stash 1. Pass the -p flag to see the full diff. <br>
`git stash show stash@{1}` <br>
Delete stash at insex 1. Omit stash@{n} to delete last stash made. <br>
`git stash drop stash@{1}` <br>
Delete all stashes <br>
`git stash clear`

### Synchronizing
Add a remote repo <br>
`git remote add <alias> <url>` <br>
View all remote connections. Add -v flag to view urls. <br>
`git remote` <br>
Remove a connection <br>
`git remote remove <alias>` <br>
Fetch all branches from remote repo (no merge) <br>
`git fetch <alias>` <br>
Fetch a specific branch <br>
`git fetch <alias> branch` <br>
Fetch the remote repo's copy of the current branch, then merge <br>
`git pull` <br>
Move (rebase) your local changes onto the top of new changes made <br>
to the remote repo (for clean, linear history) <br>
`git pull --rebase <alias>` <br>
Upload local content to remote repo <br>
`git push <alias>` <br>
Upload to a branch (can then pull request) <br>
`git push <alias> <branch>`