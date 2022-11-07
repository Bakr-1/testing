import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

pro = []

for i in data:
    if "All User Profile" in i:
        i = i.split(":")[1]
        i = i[1:-1]
        pro.append(i)

print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))

for i in pro:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}| {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(i, "ENCODING ERROR"))