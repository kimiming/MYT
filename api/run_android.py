# run_android.py

import requests
MYT_ip = ''
android_ip=''
android_name=''
local_name=''
MYTServer_url = 'http://127.0.0.1:5000/'

run_android_url = f"run/{MYT_ip}/{android_name}"

def run_android():
    response = requests.get(MYTServer_url + run_android_url)
    if response.status_code == 200:
        print("Backup successful!")
    else:
        print("Backup failed!")

if __name__ == '__main__':
    run_android()