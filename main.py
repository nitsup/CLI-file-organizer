
#decoration
print("                              CLI File organizer")
print("                            -----------------------\n")
print("available file extensions: .txt, .pdf, .jpg, .png, .mp3, .mp4, .docx, .xlsx")


#simply input for file name with extension
parcefile = input("Enter the file name with extension: ")


#folders
total_files = []

text_files = []
pdf_files = []
image_files = []
media_files = []
document_files = []
other_files = []
compressed_files = []
executable_files = []
web_files = []


#main class for file organization
class file(str):
    def __init__(self, parcefile):
        self.file = parcefile
        file_extension = parcefile.split(".")[-1]
        self.extension = file_extension
        self.path = parcefile.split("/")
        if self.path[0] == "C:":
            self.path.pop(0)
        self.file_detail = self.path[-1].split(".")
        self.path.append(self.file_detail[0])
        self.path.pop(-2)

    def get_path(self):
        print("The file path is: ", self.path)
        return self.path
        
    def assign_folder(self):
        for name in total_files:
            if name == self.file:
                print("File already organized")
                print("rename the file and try again")
                return None
            

        try :
            type(self.extension) == str(parcefile)
            print(" File extension is: ", self.extension)
        except ValueError:
            print("Invalid file extension")
            return None
        else:
            if self.extension == "txt":
              text_files.append(self.file)
              return "Text_Files"
            elif self.extension == "pdf":
                pdf_files.append(self.file)
                return "PDF_Files"
            elif self.extension == "jpg" or self.extension == "png":
                image_files.append(self.file)
                return "Image_Files"
            elif self.extension == "mp3" or self.extension == "mp4":
                media_files.append(self.file)
                return "Media_Files"
            elif self.extension == "docx" or self.extension == "xlsx":
                document_files.append(self.file)
                return "Document_Files"
            elif self.extension == "zip" or self.extension == "rar":
                compressed_files.append(self.file)
                return "Compressed_Files"
            elif self.extension == "exe" or self.extension == "bat":
                executable_files.append(self.file)
                return "Executable_Files"
            elif self.extension == "html" or self.extension == "css" or self.extension == "js":
                web_files.append(self.file)
                return "Web_Files"

            else:
                other_files.append(self.file)
                return "Other_Files"

        finally:
            total_files.append(self.file)
    def give_folder(self):
        folder = self.assign_folder()
        print("The file will be moved to the folder: ", folder)


#orders for the file to be organized
parcefile = file(parcefile)
parcefile.give_folder()
parcefile.get_path()


#output after each file is organized
print("\n\norganized files:")
print("Text Files: ", text_files)
print("PDF Files: ", pdf_files)
print("Image Files: ", image_files)
print("Media Files: ", media_files)
print("Document Files: ", document_files)
print("Compressed Files: ", compressed_files)
print("Executable Files: ", executable_files)
print("Web Files: ", web_files)
print("Other Files: ", other_files)


# Ask user if they want to organize another file
try:
    entery = input("\n\nDo you want to organize another file? (y/n): ")
    if entery == "y":
        exec(open("main.py").read())
    elif entery == "n":
        print("Thank you for using the file organizer!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
except Exception as e:
    print("Invalid input. Please enter 'y' or 'n'.")
