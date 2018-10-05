# -*- coding: utf-8 -*-
import platform


def get_backup_path():
    if platform.system() == 'Windows':
        return r'E:\PyWorkspace\GitBackup\backup'
    else:
        return r'/home/pi/GitBackup/backup'


class GitInfo:
    def __init__(self, repo_url, repo_name=None, user_name=None, email=None):
        self.repo_url = repo_url
        self.repo_name = repo_name
        if not repo_name:
            i = self.repo_url.rfind('/')
            self.repo_name = self.repo_url[i + 1:]
        self.user_name = user_name
        self.email = email


class Config:
    repos = [GitInfo(repo_url='https://github.com/1046102779/oklog'),
             GitInfo(repo_url='https://github.com/1046102779/grbac')]
    backup_path = get_backup_path()
    timing_backup = 60 * 60 * 1
