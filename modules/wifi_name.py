import subprocess

#https://stackoverflow.com/questions/33227160/how-do-i-get-python-to-know-what-wifi-the-user-is-connected-to
def find_wifi():
    '''
    Finds the name of the current SSID for the network the host is on
    
    Inputs: None
    Outputs: String of the name of the SSID
    '''
    wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
    data = wifi.decode('utf-8')
    newting = data.splitlines()
    for i in newting:
        if "SSID" in i:
            for j, k in enumerate(i):
                if k == ":":
                    wifi_net = i[j+2::]
                    return wifi_net