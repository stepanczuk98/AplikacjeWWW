# Z8
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def update_file(self, text_data):
        file = open(self.file_name, "a")
        file.write(text_data)
        file.close()

    def read_file(self):
        file = open(self.file_name, "r")
        print(file.read()) 
