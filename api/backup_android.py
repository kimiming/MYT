# backup_android.py

import requests
android_ip=''
android_name=''
local_name=''
MYT_url = 'http://127.0.0.1:5000/'

backup_url = f"export/{android_ip}/{android_name}/{local_name}"

def backup_android():
    response = requests.get(MYT_url + backup_url)
    if response.status_code == 200:
        print("Backup successful!")
    else:
        print("Backup failed!")

if __name__ == '__main__':
    backup_android()