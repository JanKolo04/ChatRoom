from ftplib import FTP  

host = '127.0.0.1'
user = 'root'
password = 'admin123'

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    ftp.cwd("mydir")
    
    with open('specialfile.txt', 'wb') as f:
       ftp.retrbinary('RETR ' + 'otherfile.txt', f.write, 1024)

    ftp.quit()
