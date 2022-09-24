Joseph Petrock

status
	-Keeps track of the repository
	-Will tell you if files have been created but not added to the repository
	-Will tell you when a file has been modified
	- "git status

clone
	-Allows user to clone new repositories into directories
	-Can also clone different branches of a repository
	- "git clone <url>"

add
	-adds all new files to a list of commits ready to be pushed
	-also gives a summary of changes to files whether it's adding or removing or editing files
	-can also add ignored items using the -f flag
	-"git add <directory>"

rm
	-removes tracked files from the git index
	-only works in the current branch
	-cannot remove in progress changes
	-"git rm -f <file>"


commit
	-commits the changes from git add to the branch
	-gives a log of the changes to the branch
	-can shorthand the add command with a -a flag
	-"git commit -a"

push
	-pushes the commits from the branch to main
	-"git push"

fetch
	-fetches the current version of the branch if there are new files that were added from outside of your cloned repository
	-also used to download remote repositories
	-"Git fecth <repository>"

merge
	-allows you  to merge branches of a repository into one as a new commit
	-"git merge <name of repository you're merging with>


pull
	-similiar to fetch it will grab chnages from remote repositories
	-this one requires merges however if the two branches are not the exact same
	-"git pull <repository>


branch
	-lists all the branches -l
	-creates new branches
	-deletes branches -d
	-also can rename a branch
	-"git branch -d <branch name>"

checkout
	-switches from one branch to another
	-"git checkout <branchname>"

.git
	-contains all necessary files for viewing all the changes to the repository

.gitignore
	-puts the name of ignored files into here so they will be ignored by the git tracker

Pull Requests
	-allows you to explain the changes you've made and then pushed to a repository on GitHub

SSH Authentication
	-Instead of having to sign in to use commit you can use an SSH key you've created and added to your account
	-More secure since it's harder for someone to get your SSH key than it is your account

