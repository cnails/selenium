hwid = str(subprocess.check_output(
    'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
data = requests.get(
    'https://gist.githubusercontent.com/rishav394/z/raw/x')
if hwid in data.text:
    print('Authenticated!')
    auth = True
else:
    print(hwid + ' was not found on the server.\nNot authorised!')