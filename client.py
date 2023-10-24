import sys
import subprocess
import time
from modules import web_pages, dns_check, teams_check, outlook_check, wifi_checker, wifi_name

def do_main():
    wifi_net = wifi_name.find_wifi()
    output_file = open(f"text_files/{wifi_net}_output.txt", "w")
    
    #Checks the status of the current wifi channel
    wifi_checker.wifi_status(output_file)
        
    #Modules stores in the modules folder for checking all our ports and services
    web_pages.web_check("text_files/urls.txt", output_file)
    dns_check.dns_checker("text_files/dns.txt", output_file)
    teams_check.check_teams(output_file)
    outlook_check.check_outlook(output_file)

def main():
    #call procedures
    #Create file for output
    while(True):
        do_main()
        time.sleep(15)

if __name__ == '__main__':
    sys.exit(main()) 
