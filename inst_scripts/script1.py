from pathlib import Path
import urllib.request
import subprocess
import json
import sys

current_path = Path().cwd()

args = sys.argv
count = len(args) - 1
if count != 2:
    sys.exit()



# json読み込み
json_open = open("inst_URL.json","r")
json_urls = json.load(json_open)

# URL取得
URL = json_urls[sys.args[2]]
print(URL)
# URL = "https://downloads.raspberrypi.org/imager/imager_latest.exe"


# ファイルパス取得
dl_name = URL.split("/")[-1]

print(current_path.resolve())
# print(dl_name)

# ファイルのDL、実行
urllib.request.urlretrieve(URL, dl_name)
subprocess.call(current_path.joinpath(dl_name))