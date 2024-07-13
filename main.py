import tkinter as tk
from tkinter import messagebox

from run_MYTServer import run_MYTServer
from api.get_current_MYT_list import get_current_MYT_list

# 魔云腾服务器地址
MYT_url = 'http://127.0.0.1:5000/'

# 当前拥有的魔云腾ip
MYTIP_map = {
    'Ip_65': '192.168.200.65',
    'Ip_61': '192.168.200.61',
    'Ip_76': '192.168.200.76',
    'Ip_83': '192.168.200.83',
    'Ip_144': '192.168.200.144',
    'Ip_153': '192.168.200.153',
    'Ip_154': '192.168.200.154',
    'Ip_188': '192.168.200.188',
    'Ip_202': '192.168.200.202',
    'Ip_247': '192.168.200.247'
}

def on_select(event):
    selected_key = listbox.get(listbox.curselection())
    selected_ip = MYTIP_map[selected_key]
    ip_label.config(text=f"当前IP: {selected_ip}")

def start_server():
    server_status = run_MYTServer()
    if server_status:
        messagebox.showinfo("成功", "魔云腾服务器启动成功！")
        get_current_MYT_list(MYT_url, MYTIP_map[listbox.get(listbox.curselection())])
    else:
        messagebox.showerror("失败", "魔云腾服务器启动失败！")

def main():
    global listbox, ip_label
    root = tk.Tk()
    root.title("魔云腾服务器控制")
    root.geometry("900x600")

    # 创建列表框
    listbox = tk.Listbox(root)
    for key in MYTIP_map.keys():
        listbox.insert(tk.END, key)
    listbox.pack(side=tk.LEFT, padx=10, pady=10)
    listbox.bind('<<ListboxSelect>>', on_select)

    # 创建标签显示当前IP
    ip_label = tk.Label(root, text="当前IP: ")
    ip_label.pack(pady=20)

    # 创建启动服务器按钮
    start_button = tk.Button(root, text="启动服务器", command=start_server)
    start_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
