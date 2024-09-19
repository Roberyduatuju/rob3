#!/usr/bin/python
import os
import http.client
import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("Hackers Shell Finder V1", font = "digital", width = 100)
    print(ascii_banner)
    print('\n made with \u2764\uFE0F  and \u2615 by Keyvan Hardani')

     
def clearing():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
banner()
website = input('\n Enter your target URL: ')
shells = ['wp-includes/SimplePie/Cache/ts.php' , 'wp-includes/assest/ts.php' , 'wp-includes/IXR/ts.php']
foundshells = []

for shell in shells:
    site = website.replace('http://','')
    shell = shell.replace('/', '', 1 )
    host = site + '/' + shell
    conn = http.client.HTTPConnection(site)
    conn.connect()
    request = conn.request('GET',shell)
    response = conn.getresponse()
    #print(response.status)
    if response.status == 200: 
        print ('\n\t[+] Shell found %s \n' %host)
        foundshells.append(host)
    else:
        print ('[-] Calling %s ' %host )

    if response.status == 200:

        fpth = os.getcwd()
        fpth2 = fpth + '/found.txt'
        fob = open(fpth2,'w')
        fob.close()
        fob = open(fpth2,'a')
        fob.writelines(foundshells)
        print ('successfully saved to the found.txt file')

    else:
        print('not found!\n ')
print('\n thank you for using this script')
print('\n made with \u2764\uFE0F  and \u2615 by Keyvan Hardani')
input('\n please enter any keys to exit')
exit()
