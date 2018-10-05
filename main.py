# -*- coding: utf-8 -*-
import threading
from utils.config import Config, get_dir_char
import os
import datetime
import time

str_and = ' && '


def auto_gen():
    cur_date = datetime.datetime.now().date().isoformat()
    for v in Config.repos:
        tmpdir = Config.backup_path + get_dir_char() + v.repo_name
        if not os.path.exists(tmpdir):
            cmd = 'cd ' + Config.backup_path + str_and + 'git clone ' + v.repo_url
            print(os.system(cmd))
            print('git clone end ' + '*' * 20)
        else:
            cmd = 'cd ' + tmpdir + str_and + 'git pull'
            print(os.system(cmd))
            print('git pull end ' + '*' * 20)
    # tar backup directory
    print('tar start' + '*' * 20)
    cmd = 'cd ' + Config.backup_path + str_and + 'cd ..' + str_and + 'tar -czvf ' + 'backup' + cur_date + '.tar.gz' + ' backup'
    print(os.system(cmd))


def main():
    while True:
        auto_gen()
        time.sleep(Config.timing_backup)


if __name__ == '__main__':
    main()
