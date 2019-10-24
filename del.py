import os
import platform
import hashlib
from getpass import getpass
import requests
from uuid import getnode as get_mac
mac = get_mac()

# assert hashlib.md5(str(getpass("pass >> ")).encode('utf-8')).hexdigest() == "098f6bcd4621d373cade4e832627b4f6", "Incorrect password"
# print("\033[A                             \033[A")
# print(mac)
all_key = requests.get("https://gist.githubusercontent.com/cnails/a23105de9e03f02725b1703f246008dc/raw/e079128366901171949e2d21f1ea44928adc9cb0/my%2520id").text

test_key = requests.get("https://gist.githubusercontent.com/cnails/a23105de9e03f02725b1703f246008dc/raw/")

# print(hashlib.md5(("key1").encode('utf-8')).hexdigest())
# print(hashlib.md5(("key2").encode('utf-8')).hexdigest())
# print(hashlib.md5(("key3").encode('utf-8')).hexdigest())


key = hashlib.md5(str(getpass("pass >> ")).encode('utf-8')).hexdigest()
gen_key = hashlib.md5((key + str(mac)).encode('utf-8')).hexdigest()
if key not in all_key and gen_key not in all_key:
	print("Wrong key")
	exit()
if gen_key in all_key:
	print("All good")
	exit()
if key in all_key:
	print("Ваш ключ > " + gen_key)
	exit()
# print(os.path.join(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0], ".pswd"))
# print(platform.platform())
# print(platform.system())
