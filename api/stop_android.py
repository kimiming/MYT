# stop_android.py

import requests
MYT_ip = ''
android_ip=''
android_name=''
local_name=''
MYTServer_url = 'http://127.0.0.1:5000/'

stop_android_url = f"stop/{MYT_ip}/{android_name}"

def stop_android():
    response = requests.get(MYTServer_url + stop_android_url)
    if response.status_code == 200:
        print("stop android successful!")
    else:
        print("stop android failed!")

if __name__ == '__main__':
    stop_android()