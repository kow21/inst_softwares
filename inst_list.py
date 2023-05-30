import tkinter as tk
import subprocess
import json
from pathlib import Path
import urllib.request
import os

class MyApp(tk.Tk):
    # json読み込み
    json_open = open("./inst_scripts/inst_URL.json","r")
    json_datas = json.load(json_open)


    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("300x200")
        self.create_widgets()


    def create_widgets(self):
        # リストボックスの作成
        self.listBox = tk.Listbox(self)
        self.listBox.pack(fill=tk.BOTH, expand=True)

        # リストボックスに要素を追加

        for inst_name in self.json_datas.keys():
            self.listBox.insert(tk.END, inst_name)


        # リストボックスの要素をクリックしたら、関数を呼び出す
        self.listBox.bind("<<ListboxSelect>>", self.on_select)


    def on_select(self, event):
        # 選択された要素のインデックスを取得
        index = self.listBox.curselection()[0]
        select_item = self.listBox.get(index)

        # 選択された要素に応じたスクリプトを実行
        self.install_data(select_item)
            

    def install_data(self, inst_soft):

        # URL取得
        URL = self.json_datas[inst_soft]

        # ファイルパス取得
        dl_name = URL.split("/")[-1]
        current_path = Path().cwd()

        # ファイルのDL、実行
        if not Path(current_path.joinpath(dl_name)).exists():
            urllib.request.urlretrieve(URL, dl_name)
        # subprocess.run( repr(current_path.joinpath(dl_name)) ,capture_output=True, shell=True)
        subprocess.run(dl_name, shell=True)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
