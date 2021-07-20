import dropbox
from dropbox.files import WriteMode
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for (roots,dirs,files) in os.walk(file_from) :
            for file in files :
                local_path = os.path.join(roots,file)
                rel_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,rel_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))

def main():
    access_token = 'fiYvQLKB1-EAAAAAAAAAAURbKfua2J0EuIBGDRtWUE2VV6gqZ3Fv8zYIaOGgRaRt'
    transferData = TransferData(access_token)

    file_from = input("enter the path from which you need to upload")
    file_to = input("enter the path which you want to upload")

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()