# Before you PUSH to the Repository IMPORTANT

Make sure to pull any updated files up to your local repository before pushing OR editing content to/in the repository.

Use the `git pull` or `git pull https://github.com/probstcj/Hackathon` to pull the files. Then you can start working.

# File System

All files will be in folders named accordingly once we know the project.

# To get GIT started

- First, download [Git for Windows](https://gitforwindows.org/)
- Once downloaded and installed, make a folder where you will store your repository.
- Right click, and click `Git Bash Here`
- Type and enter the command `git init`. This initializes a new GIT repo.
- Type and enter the command `git config --global user.name [INSERT YOUR USERNAME HERE]` and replace the `[INSERT YOUR USERNAME HERE]` with your Github username. This will set your username for the repo, to allow you access.
- Type and enter the command `git config --global user.email [INSERT YOUR EMAIL HERE]` and replace the `[INSERT YOUR EMAIL HERE]` with your Github email. This will set your email for the repo, to allow you access.
- Type and enter the command `git remote add origin git@github.com:probstcj/Hackathon.git`
- Type and enter the command `git clone https://github.com/probstcj/Hackathon` and type and enter `yes`
- Type and enter the command `ssh-keygen -t rsa -C "[ENTER YOUR EMAIL]"`, hit enter 3 times and it should be saved.
- Go to the directory where it saved (it will say in the command prompt) and copy the contents of the file `id_rsa.pub` (should start with ssh-rsa)
- Type and enter the command `eval "$(ssh-agent -s)"`
- Type and enter the command `ssh-add ~/.ssh/id_rsa`
- Now go to your Github account, and click on your profile and click settings.
- Go to SSH and GPG Keys
- Click New SSH Key
- Name it your name
- Paste the contents of the file into the box and click "Add SSH Key"
- Go back to your repo and add a new file called `test[YOUR NAME].txt`
- Type and enter the command `git add .`
- Type and enter the command `git commit -m "[YOUR NAME]"`
- Type and enter the command `git fetch`
- Type and enter the command `git pull https://github.com/probstcj/Hackathon`
- Type and enter the command `git push --set-upstream origin main`

This has effectively created your repo and ensured that you now have a copy of your files on your local computer as well. With this, any changes that you make in your local directory will effect the repo once it is added, so please be careful.

Before you add and change, please pull. That is said above

The sequence to add files is very easy. Simply do the following.

- `git add .`
- `git commit -m "[Enter a comment]"`
- `git push`

If there are errors, please let Caleb know so he can fix them.

# Topic

Currently unknown
