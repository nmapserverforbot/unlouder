# CONFIG

import os

api_id = int('9907811') # API ID  (int)
api_hash = str("b5adb7f7d4a096750edec1bc6daacd56") # API HASH  (str)
bot_token = str("6018239903:AAGUzzAcy0JkPZ86ffBpzGQ5hgQzgAYR1ls") # BOT TOKEN 524146561:EGETd-rwferfER_rfeER (str)
channel_id = int('-1001309037895') # CHANNEL ID [put -1001 before channel id] 
download_dir = str(os.path.join(os.getcwd(), 'downloads'))
sessions_dir = str(os.path.join(os.getcwd(), 'sessions'))
files_dir = str(os.path.join(os.getcwd(), 'files'))
status_logs_dir = str(os.path.join(os.getcwd(), 'temp'))

def CheckDirExistence(dir):

    if not os.path.isdir(dir):
        os.mkdir(dir)

CheckDirExistence(download_dir)
CheckDirExistence(sessions_dir)
CheckDirExistence(files_dir)
CheckDirExistence(status_logs_dir)
