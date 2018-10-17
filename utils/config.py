# -*- coding: utf-8 -*-
import platform


def get_backup_path():
    if platform.system() == 'Windows':
        return r'E:\PyWorkspace\GitBackup\backup'
    else:
        return r'/home/pi/pyworkspace/GitBackup/backup'


def get_dir_char():
    if platform.system() == 'Windows':
        return '\\'
    else:
        return '/'


class GitInfo:
    def __init__(self, repo_url, repo_name=None, user_name=None, passwd=None, email=None):
        self.repo_url = repo_url
        self.repo_name = repo_name
        if not repo_name:
            i = repo_url.rfind('/')
            self.repo_name = repo_url[i + 1:]
            ii = self.repo_name.rfind('.git')
            if -1 != ii:
                self.repo_name = self.repo_name[:ii]
        self.user_name = user_name
        self.passwd = passwd
        if user_name and passwd:
            i = repo_url.find('//') + 2
            self.repo_url = repo_url[:i] + user_name + ':' + str(passwd) + '@' + repo_url[i:]
        self.email = email


class Config:
    repos = [
        GitInfo(repo_url='https://github.com/zzcontinent/CliffMemSQL'),
        GitInfo(repo_url='https://github.com/zzcontinent/CliffQueue'),
        GitInfo(repo_url='https://github.com/zzcontinent/GitBackup'),
        GitInfo(repo_url='https://github.com/zzcontinent/linaro-ubuntu-axi-driver-test'),
        GitInfo(repo_url='https://github.com/zzcontinent/ipsniffer'),
        GitInfo(repo_url='https://github.com/zzcontinent/EthernetPortSpeedTest'),
        GitInfo(repo_url='https://github.com/zzcontinent/services.git'),
        GitInfo(repo_url='https://github.com/zzcontinent/pyutils.git'),
        GitInfo(repo_url='http://git.woda.ink/woda/services/BrokerAssistant/BA_General', user_name='cliff', passwd='xxx'),
        GitInfo(repo_url='http://git.woda.ink/dw/metadata', user_name='cliff', passwd='xxx'),
        GitInfo(repo_url='http://git.woda.ink/dw/ods_controller', user_name='cliff', passwd='xxx'),
        GitInfo(repo_url='http://git.woda.ink/dw/dw-etl', user_name='cliff', passwd='xxx'),
    ]

    backup_path = get_backup_path()
    timing_backup = 60 * 60 * 1 
