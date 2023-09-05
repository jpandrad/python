import pysftp

# SFTP Credentials
sftpServer = "SFTP_SERVER_ADDRESS"
sftpUsername = "USERNAME"
sftpPassword = "PASSWORD"

# File Path
remotePath = "/opt/test/"
localPath = "/tmp/"

#File Name and Extension
fileName = "FILE_NAME"
now = datetime.now()
yesterday = now - timedelta(days = 1)
fileDate = yesterday.strftime("%Y%m%d")
fileExtension = ".tgz"


# Get File
def getFile():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host=sftpServer, username=sftpUsername, password=sftpPassword, cnopts=cnopts) as sftp:
    print "Connection succesfully stablished ... "
    sftp.get(remotePath+fileName+fileDate+fileExtension, localPath)
    sftp.close()

# Put File
def putFile():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host=sftpServer, username=sftpUsername, password=sftpPassword, cnopts=cnopts) as sftp:
    print "Connection succesfully stablished ... "
    sftp.put(localPath+fileName+fileDate+fileExtension, remotePath)
    sftp.close()


## Uncomment getFile line to download the file or putFile line to upload the file
#getFile()
#putFile()
