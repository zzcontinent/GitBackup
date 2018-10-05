# -*- coding: utf-8 -*-
import threading
from utils.config import Config
import os
import datetime
import time

str_and = ' && '


def auto_gen():
    cur_date = datetime.datetime.now().date().isoformat()
    for v in Config.repos:
        tmpdir = Config.backup_path + '\\' + v.repo_name
        if not os.path.exists(tmpdir):
            cmd = 'cd ' + Config.backup_path + str_and + 'git clone ' + v.repo_url
            print(os.system(cmd))
        else:
            cmd = 'cd ' + tmpdir + str_and + 'git pull'
            print(os.system(cmd))
    # tar backup directory
    cmd = 'cd ' + Config.backup_path + str_and + 'cd ..' + str_and + 'tar -czvf ' + Config.backup_path + cur_date + '.tar.gz' + ' ' + Config.backup_path
    print(os.system(cmd))


def timing_task():
    auto_gen()
    timer = threading.Timer(Config.timing_backup, timing_task)
    timer.start()


def main():
    timing_task()
    while True:
        time.sleep(10)


if __name__ == '__main__':
    main()
