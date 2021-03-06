from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from shutil import make_archive
from zipfile import ZipFile
from os import path, chdir
from sys import argv
import options
import yadisk
import time
import os

class backup:

    def commands(self, com):
        for i in range(len(com)):
            if com[i] == '-h' or com[i] == '--help':
                print(options.helps)
            elif com[i] == '--check-ya-token':
                print(yandex_disk().yandex_check(yandex_disk().yandex_auth()))
            elif com[i] == '--create-ya-dir':
                if options.Yandex_disk_switch == 'on':
                    if len(com) < 2:
                        raise Exception('Enter folder name')
                    yandex_disk().yandex_create_dir(yandex_disk().yandex_auth(), com[i+1])
                else:
                    raise Exception('Yandex_disk_switch is "off", please change to "on')
            elif com[i] == '--check-valid-dir':
                if path.isdir(options.homedir):
                    print('the folder is accessible')
                else:
                    print('invalid folder. please change homedir to options.py')
            elif path.isfile(com[i]) or path.isdir(com[i]):
                self.backup(com[i])

    def backup(self, pwd):
        if options.homedir == '':
            raise Exception('Please enter homedir in options')
        date = time.strftime(options.format_backups)
        if path.isfile(pwd):
            try:
                filepath, filename = path.split(pwd)
                chdir(filepath)
            except OSError:
                filename = pwd
            name = options.homedir+str(date)+f'-{filename}.zip'
            if options.Make_zip == 'on':
                with ZipFile(name, 'w') as zipf:
                    zipf.write(filename)
                if options.Yandex_disk_switch == 'off':
                    pass
                elif options.Yandex_disk_switch == 'on':
                    yandex_disk().yandex_upload(yandex_disk().yandex_auth(), name)
            elif options.Make_zip == 'off':
                if options.Yandex_disk_switch == 'on':
                    with ZipFile(name, 'w') as zipf:
                        zipf.write(filename)
                    yandex_disk().yandex_upload(yandex_disk().yandex_auth(), name)
                    os.remove(name)
                else:
                    raise Exception('Please enable Make_zip = on or Yandex_disk_switch = on')

        if path.isdir(pwd):
            dirpath, dirname = path.split(pwd)
            name = options.homedir+str(date)+'-'+dirname
            if options.Make_zip == 'on':
                make_archive(name,"zip",pwd)
                if options.Yandex_disk_switch == 'off':
                    pass
                elif options.Yandex_disk_switch == 'on':
                    yandex_disk().yandex_upload(yandex_disk().yandex_auth(), name+'.zip')
            elif options.Make_zip == 'off':
                if options.Yandex_disk_switch == 'on':
                    make_archive(name,"zip",pwd)
                    yandex_disk().yandex_upload(yandex_disk().yandex_auth(), name+'.zip')
                    os.remove(name+'.zip')

class yandex_disk:

    def yandex_auth(self):
        api = yadisk.YaDisk(token=options.Yandex_token)
        if self.yandex_check(api) == True:
            return api
        else:
            return 'Invalid token'

    def yandex_check(self, api):
        return api.check_token()        

    def yandex_disk_backup(self):
        pass
    
    def yandex_create_dir(self, api, name_dir):
        api.mkdir(name_dir)

    def yandex_upload(self, api, files):
        filepath, filename = path.split(files)
        api.upload(files, options.Yandex_name_dir+filename)

class google_drive:
    
    def google_auth(self):
       '''
       will be soon
       '''

if __name__ == '__main__':
    if len(argv) == 1:
        raise Exception('No arguments')
    backup().commands(argv[1:])