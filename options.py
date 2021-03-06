#############################
#OPTIONS#
#MAKE ZIP
Make_zip = 'on'

#HOME DIR - dir for save backups
#Example: 'C:/' or 'C:\\' using a double backslash!
homedir = ''

#TIME FORMAT - format for time 
# days - %d; month - %m; years - %Y; hour - %H; minute - %M; seconds - %S; others in the module time; function time.strf()
format_backups = '%d-%m-%Y_%H-%M-%S'

#Yandex Disk
# for upload backup on yandex disk
Yandex_disk_switch = 'off'

Yandex_token = ''

# only name dir; example dirname: 'download', you write: '/download/'
Yandex_name_dir = ''

#Google Drive
# for upload backup on google drive
Google_disk_switch = 'off' #Don't touch! I didn't work on it! Update will be soon

Google_client_id = '' 

Google_client_secret = ''

#Help
helps = '''
use the --create-ya-dir argument to create a folder on Yandex disk (use only if you specified a Yandex token). use the second argument to specify the folder name
use --check-ya-token to check the Yandex token (use only if you have a token)
use --check-valid-dir to check whether a folder is available for backup
'''