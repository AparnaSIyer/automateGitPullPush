import base64
from github import Github
from github import InputGitTreeElement

token = '22c145ee022bef7a516137dce8b7f19dc6426ee9'
g = Github(token)
repo = g.get_user().get_repo('test')
file_list = [
    'sample.txt',
    'sample1.txt'
]
commit_message="Initial file commits via py script"
master_ref = repo.get_git_ref('heads/master')
print(master_ref)
master_sha = master_ref.object.sha # returns the sha code for the master branch that is test
base_tree = repo.get_git_tree(master_sha) # question mark
element_list = list()

for entry in file_list:
    element = InputGitTreeElement(entry, '100644', 'text', entry) # ????
    element_list.append(element)

tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)

for entry in file_list:
    with open(entry, 'rb') as input_file:
        data = input_file.read()
    if entry.endswith('.png'):
        old_file = repo.get_contents(entry)
        commit = repo.update_file('/' + entry, 'Update PNG content', data, old_file.sha)