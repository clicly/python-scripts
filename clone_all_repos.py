import requests, json, subprocess, os

class RepoAccess:
    PUBLIC_HTTPS = 1
    PRIVATE_SSH = 2

#####################################
# Github user name
USER_NAME = '<username>'
# Project repository
FILE_DIR = os.path.expanduser("~") + "/Downloads"
# Repositories to download
ACCESS = RepoAccess.PRIVATE_SSH
# May needed later
ACCESS_TOKEN = '<accesstoken>' 
#####################################

def git(*args):
    """
    Executes git command with list of parameters
    """
    return subprocess.check_call(['git'] + list(args))
    
def clone_public_repositories_https(repository):
    """
    Clones public repository into current working directory
    """
    git("clone", f'{repository["html_url"]}.git')

def clone_private_repositories_ssh(repository):
    """
    Clones private repository into current working directory
    """
    git("clone", f'{repository["ssh_url"]}')

def request_api(api_url):
    """
    Creates a rest api call to parameter url with error handling
    """
    r = requests.get(api_url)
    r.raise_for_status()
    return json.loads(r.content)

if __name__ == "__main__":

    os.chdir(FILE_DIR)
    
    if (ACCESS is RepoAccess.PRIVATE_SSH):
        private_repositories = request_api(f'https://api.github.com/user/repos?access_token={ACCESS_TOKEN}')
        for repository in private_repositories:
            clone_private_repositories_ssh(repository)
    else:
        public_repositories = request_api(f'https://api.github.com/users/{USER_NAME}/repos')
        for repository in public_repositories:
            clone_public_repositories_https(repository)
