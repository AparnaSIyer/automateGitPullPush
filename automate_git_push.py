from subprocess import *
import os

# Popen(['git','clone',str('https://github.com/AparnaSIyer/hello-world'),'/home/aparna/my_project_1'])
os.chdir(os.path.abspath('/home/aparna/PycharmProjects/myFirstProject'))

Popen(['git', 'add', '--all'])
message = "Can be changed"
Popen(['git', 'commit', '-m', message])
remote_url = 'git@github.com:AparnaSIyer/automateGitPullPush.git'
remote_url2 = 'git@github.com:AparnaSIyer/hello-world.git'
print(call("git remote set-url origin 'git@github.com:AparnaSIyer/automateGitPullPush.git'", shell=True))
print(call(['git', 'remote', '-v']))
# print('setting remote repo')
(Popen('git push', shell=True))