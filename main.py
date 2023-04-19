from documentcloud.addon import SoftTimeOutAddOn

class Clear(SoftTimeOutAddOn):
""" For all the documents, if the status of the document is error or nofile, deletes the document"""
    def main(self):
        for document in self.get_documents():
            if document.status == 'error' or document.status == 'nofile':
                document.delete()
 
if __name__ == "__main__":
    Clear().main()
