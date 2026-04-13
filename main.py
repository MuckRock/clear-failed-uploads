import time
from documentcloud.addon import SoftTimeOutAddOn

class Clear(SoftTimeOutAddOn):
    def main(self):
        self.client.session.headers.update({'User-Agent': 'Clear Failed Uploads Add-On'})
        for document in self.get_documents():
            if document.status == 'error' or document.status == 'nofile':
                document.delete()
                time.sleep(5)
 
if __name__ == "__main__":
    Clear().main()
