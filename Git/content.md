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