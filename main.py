import subprocess, requests, time, os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('pastebin link here')

try:
    if hwid in r.text:
        pass
    else:
        print('[ERROR] HWID Not in database')
        print(f'HWID: {hwid}') 
        time.sleep(5)
        os._exit()
except:
    print('[ERROR] Failed to connect to database')
    time.sleep(5) 
    os._exit() 

print('You are Logged in')
