import tkinter as tk
import subprocess

class MyApp(tk.Tk):
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
        self.listBox.insert(tk.END, "Raspberry Pi Imager")
        self.listBox.insert(tk.END, "Item 2")
        self.listBox.insert(tk.END, "Item 3")

        # リストボックスの要素をクリックしたら、関数を呼び出す
        self.listBox.bind("<<ListboxSelect>>", self.on_select)

    def on_select(self, event):
        # 選択された要素のインデックスを取得
        index = self.listBox.curselection()[0]

        # 選択された要素に応じたスクリプトを実行
        if index == 0:
            subprocess.call(["python", "./inst_scripts/script1.py"])
        elif index == 1:
            subprocess.call(["python", "./inst_scripts/script2.py"])
        elif index == 2:
            subprocess.call(["python", "./inst_scripts/script3.py"])

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
