from documentcloud.addon import SoftTimeOutAddOn

class Clear(SoftTimeOutAddOn):
    def main(self):
        if not self.documents:
            self.set_message("Please select at least one document.")
            return
        for document in self.get_documents():
            if document.status == 'error' or document.status == 'nofile':
                document.delete()
 
if __name__ == "__main__":
    Clear().main()
