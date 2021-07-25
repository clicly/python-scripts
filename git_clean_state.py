import os, subprocess

# insert repository paths here
PROJECT_PATHS = ['']
COMMAND_PREFIX = 'Command:'

class GitCommands():
    git_base = 'git'
    pull = 'pull'
    fetch = 'fetch'
    fetch_prune_flag = '--prune'
    switch = 'switch'

class GitCommandExecutor:
    def pull():
        print(f'{COMMAND_PREFIX} {GitCommands.pull}')
        subprocess.call([GitCommands.git_base, GitCommands.pull])

    def fetch():
        print(f'{COMMAND_PREFIX} {GitCommands.fetch}')
        subprocess.call([GitCommands.git_base, GitCommands.fetch])

    def fetch_prune():
        print(f'{COMMAND_PREFIX} {GitCommands.fetch} {GitCommands.fetch_prune_flag}')
        subprocess.call([GitCommands.git_base, GitCommands.fetch, GitCommands.fetch_prune_flag])

    def switch_branch(branch_name):
        print(f'{COMMAND_PREFIX} {GitCommands.switch}')
        subprocess.call([GitCommands.git_base, GitCommands.switch, branch_name])
    
    def show_branches():
        print(os.listdir('.git/refs/heads'))

def navigate_to_path(project_path):
    print(f'{COMMAND_PREFIX} Navigate to {project_path}')
    os.chdir(project_path)

def clean_projects(projects_paths):
    for project_path in projects_paths:
        clean_project(project_path)

def clean_project(project_path):
    navigate_to_path(project_path)

    git = GitCommandExecutor
    git.fetch_prune()
    git.switch_branch("development")
    git.show_branches()

if __name__ == "__main__":
    clean_projects(PROJECT_PATHS)  