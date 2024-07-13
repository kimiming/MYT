#get_current_MYT_list.py

import requests

MYTServer_url=''
android_ip=''


def get_current_MYT_list(MYTServer_url,android_ip):
    get_MYT_list_api= '/get/'+ android_ip
    response = requests.get(MYTServer_url + get_MYT_list_api)
    if response.status_code == 200:
        # 获取返回的JSON对象
        json_data = response.json()
        print(json_data)
        print("stop android successful!")
    else:
        print("stop android failed!")


if __name__ == '__main__':
    get_current_MYT_list()
