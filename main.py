# -*- coding: utf-8 -*-
import threading
from utils.config import Config, get_dir_char
import os
import datetime
import time
from utils.logger import *

str_and = ' && '


def auto_gen():
    cur_date = datetime.datetime.now().date().isoformat()
    for v in Config.repos:
        tmpdir = Config.backup_path + get_dir_char() + v.repo_name
        if not os.path.exists(tmpdir):
            cmd = 'cd ' + Config.backup_path + str_and + 'git clone ' + v.repo_url
            debug_log(os.system(cmd))
            debug_log(cmd + '*' * 20)
        else:
            cmd = 'cd ' + tmpdir + str_and + 'git pull'
            debug_log(cmd + '*' * 20)
            debug_log(os.system(cmd))

    # tar backup directory
    cmd = 'cd ' + Config.backup_path + str_and + 'cd ..' + str_and + 'tar -czvf ' + 'backup' + cur_date + '.tar.gz' + ' backup'
    debug_log(cmd + '*' * 20)
    debug_log(os.system(cmd))


def main():
    init_log(log_path='/var/log/GitBackup/GitBackup.log', log_level='NOTSET')
    while True:
        auto_gen()
        time.sleep(Config.timing_backup)


if __name__ == '__main__':
    main()
