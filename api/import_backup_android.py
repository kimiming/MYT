# import_backup_android.py

import requests
MYT_ip = ''
androidI_ip=''
android_name=''
local_name=''
MYTServer_url = 'http://127.0.0.1:5000/'

import_android_url = f"import/{MYT_ip}/{android_name}"

def import_android():
    response = requests.get(MYTServer_url + import_android_url)
    if response.status_code == 200:
        print("import android successful!")
    else:
        print("import android failed!")

if __name__ == '__main__':
    import_android()