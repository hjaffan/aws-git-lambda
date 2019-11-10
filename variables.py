import os


GIT_REPO = os.getenv("GIT_REPO", '')
GIT_USERNAME = os.getenv("GIT_USERNAME", '')
GIT_PASSWORD = os.getenv("GIT_PASSWORD", '')
SKIP_SSL = os.getenv("SKIP_SSL", True)