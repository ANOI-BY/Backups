# Backups
 
### What is it?
**this is a backup machine :)**

Now your files will not be lost!

### How to install?
~~~
git clone https://github.com/ANOI-BY/Backups.git
cd Backups
pip3 install -r requirements.txt # for linux
pip install -r requirements.txt # for windows
~~~
then you need to change the config

open the file options.py and change the following lines:
~~~python
Make_zip = 'on'
homedir = 'Your backup folder' 
~~~
now you can run:
~~~
python3 backup.py (link on file) # For linux
python backup.py (link in file) # For windows
~~~

### Example
~~~
python backup.py C:/dirname # For windows
python3 backup.py /home/user/dirname # For linux
~~~

### Arguments

help and new types of arguments were added to the app:
~~~
python backup.py -h # or --help to open the help

python backup.py --create-ya-dir (folder name) # argument to create a folder on Yandex disk (use only if you specified a Yandex token). use the second argument to specify the folder name.

python backup.py --check-ya-token # to check the Yandex token (use only if you have a token)

python backup.py --check-valid-dir # to check whether a folder is available for backup
~~~

### Additionally
for a quick start, add to alias:
~~~
#for linux
cd
nano .bashrc

#add new line
alias backup='python3 /home/user/Backups/backup.py'

#example:
backup /home/user/dirname
~~~
for windows, it is a little more complicated, you need to create a bat file and write the following into it:
~~~
@echo off
doskey backup=python (link on backups dir) $*
~~~
now open regedit and find:
~~~
HKEY_CURRENT_USER\Software\Microsoft\Command Processor\Autorun
~~~
set the path to .bat file. Example:
~~~
C:\alias\alias.bat
~~~
Done!
now open command line and write:
~~~
backup C:\dirname
~~~

### Use cloud (disks)
so far I've only added Yandex disk but will soon add Google drive

configuring backup to Yandex disk:
~~~python
#open options.py
#change Yandex_disk_switch = 'off'

Yandex_disk_switch = 'on'

#enter yandex disk token
Yandex_token = 'token'

#and enter the directory on Yandex Disk
Yandex_name_dir = '/download/'
~~~
if you want, you can disable archiving on your computer (only if you have enabled archiving on Yandex Disk)
~~~python
#change Make_zip = 'on'
Make_zip = 'off'
~~~

# PROFIT
**if you have any errors, please contact me at telegram @ANOI_BY**
