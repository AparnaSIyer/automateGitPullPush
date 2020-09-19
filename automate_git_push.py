from subprocess import *
import os
import time
from datetime import datetime

# Popen(['git','clone',str('https://github.com/AparnaSIyer/hello-world'),'/home/aparna/my_project_1'])
os.chdir(os.path.abspath('/home/aparna/PycharmProjects/myFirstProject'))
repo_1_pvt_url="git@github.com:AparnaSIyer/Repo_backup_1.git"
repo_2_pub_url="git@github.com:AparnaSIyer/Repo_backup_2.git"
#pullling the latest code changes to above repos
def push_automate_git_repo():
    # Popen(['git', 'clone', str('git@github.com:AparnaSIyer/Repo_backup_1.git'), '/home/aparna/Repo_backup_1'])
    # Popen(['git', 'clone', str('git@github.com:AparnaSIyer/Repo_backup_2.git'), '/home/aparna/Repo_2'])
    print(call("git remote set-url origin 'git@github.com:AparnaSIyer/Repo_backup_1.git'", shell=True))
    print(Popen(['git', 'pull', str('git@github.com:AparnaSIyer/automateGitPullPush.git')]))
    print(Popen('git push',shell=True))
    time.sleep(5)
push_automate_git_repo()
#hello bro 1
Popen(['git','pull'])
Popen(['git', 'add', '--all'])
message = "Updated "+ datetime.now().strftime("%d/%m/%Y %H:%M:%S")
time.sleep(10)
Popen(['git', 'commit', '-m', message])
remote_url = 'git@github.com:AparnaSIyer/automateGitPullPush.git'
remote_url2 = 'git@github.com:AparnaSIyer/hello-world.git'
print(call("git remote set-url origin 'git@github.com:AparnaSIyer/automateGitPullPush.git'", shell=True))
print(call(['git', 'remote', '-v']))
# print('setting remote repo')
(Popen('git push', shell=True))
#Test whether the pull command is working via Github
#test test test
