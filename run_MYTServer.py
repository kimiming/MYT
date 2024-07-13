# run_MYTServer.py
import os
import sys
import subprocess
import psutil
import ctypes
import logging

MYT_Server_Path = "C:\\Users\\dxdxd\\Desktop\\moyunteng\\myt_sdk_v1.0.14.19\\myt_sdk\\myt_sdk.exe"

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def run_MYTServer(): 
    serverStatus = ''
    
    def is_process_running(process_name):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if process_name.lower() in proc.info['name'].lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def run_as_admin():
        try:
            if not ctypes.windll.shell32.IsUserAnAdmin():
                params = f'"{__file__}"'
                ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", params, None, 1)
                return True
        except Exception as e:
            print(f"请求管理员权限时发生错误: {e}")
            return False

    if not is_process_running("myt_sdk.exe"):
        if run_as_admin():
            exit()         
        try:
            status = subprocess.Popen(MYT_Server_Path)
            logging.info(f"成功打开 {status}")
            serverStatus = '1'
        except FileNotFoundError:
            print(f"文件 {MYT_Server_Path} 未找到")
            serverStatus = '0'
        except Exception as e:
            print(f"发生错误: {e}")
            serverStatus = '0'
    else:
        print("程序已经打开，不再重复执行")
        serverStatus = '2'

    return serverStatus

if __name__ == '__main__':
    run_MYTServer()