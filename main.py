from documentcloud.addon import AddOn

class Clear(AddOn):

    def main(self):

        for document in self.get_documents():
            if document.status == 'error' or document.status == 'nofile':
                document.delete()
 

if __name__ == "__main__":
    Clear().main()
