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
shells = ['wp-includes/assets/ts.php','wp-includes/ID3/ts.php','wp-includes/IXR/ts.php','wp-includes/PHPMailer/ts.php','wp-includes/Requests/library/ts.php','wp-includes/Requests/src/Auth/ts.php','wp-includes/Requests/src/Cookie/ts.php','wp-includes/Requests/src/Exception/Http/ts.php','wp-includes/Requests/src/Exception/Transport/ts.php','
wp-includes/Requests/src/ts.php','wp-includes/Requests/src/Proxy/ts.php','wp-includes/Requests/src/Response/ts.php/','wp-includes/Requests/src/Transport/ts.php','wp-includes/Requests/src/Utility/ts.php','wp-includes/SimplePie/XML/Declaration/ts.php','wp-includes/SimplePie/XML/ts.php','wp-includes/SimplePie/Parse/ts.php','wp-includes/SimplePie/Net/ts.php','wp-includes/SimplePie/HTTP/ts.php','wp-includes/SimplePie/Decode/HTML/ts.php','wp-includes/SimplePie/Decode/ts.php','wp-includes/SimplePie/Content/Type/ts.php','wp-includes/SimplePie/Content/ts.php','wp-includes/SimplePie/Cache/ts.php']
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
php','/templates/ja-helio-farsi/index.php','/wp-admin/m4d.php','/d.php']
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
 