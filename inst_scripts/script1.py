from pathlib import Path
import urllib.request
import subprocess

current_path = Path().cwd()
URL = "https://downloads.raspberrypi.org/imager/imager_latest.exe"

dl_name = URL.split("/")[-1]

print(current_path.resolve())
# print(dl_name)


urllib.request.urlretrieve(URL, dl_name)
subprocess.call(current_path.joinpath(dl_name))