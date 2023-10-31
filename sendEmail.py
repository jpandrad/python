import smtplib
import sys
# Part of solution created ASAP to send new passwords from a CSV list
### For use this script, run the command or send using another script (Ex: ShellScript or PowerShell)
### $ python3.6 sendEmail.py New_Pass email@domain.com
### SYNTAX: python sendEmail.py <NEW_PASS> <EMAIL_TO>

sender = '<EMAIL>@<DOMAIN>.com'
rcvPasswd =  sys.argv[1]
rcvEmail = sys.argv[2]
receivers = [f"{rcvEmail}"]

message = """From: Sender Email <EMAIL>@<DOMAIN>.com
To: """ f"{rcvEmail}" """
Subject: Changing the Password


Hello! Follow your new password.
PASSWORD: """ f"{rcvPasswd}" """
"""

try:
    smtpObj = smtplib.SMTP('smtp.domain.com:25')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except SMTPException:
    pass
