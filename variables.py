import os


GIT_REPO = os.getenv("GIT_REPO", '')
GIT_FULLNAME = os.getenv("FULL_NAME", '')
GIT_EMAIL = os.getenv("GIT_EMAIL", '')
GIT_USERNAME = os.getenv("GIT_USERNAME", '')
GIT_PASSWORD = os.getenv("GIT_PASSWORD", '')
SKIP_SSL = os.getenv("SKIP_SSL", True)

NEW_REPO_PATH = '/tmp/'

commit_env = os.environ
commit_env['GIT_AUTHOR_NAME'] = GIT_FULLNAME
commit_env['GIT_AUTHOR_EMAIL'] = GIT_EMAIL
commit_env['GIT_COMMITTER_NAME'] = GIT_FULLNAME
commit_env['GIT_COMMITTER_EMAIL'] = GIT_EMAIL