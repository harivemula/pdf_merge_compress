from PyPDF2 import PdfFileMerger
import os

out_file_name = input("Output file name with extension: ")
#Create and instance of PdfFileMerger() class
merger = PdfFileMerger()

#Create a list with PDF file names
path_to_files = r'input/'

#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_files):
    #Iterate over the list of file names
    for file_name in file_names:
        #Append PDF files
        print("filename: ["+file_name+"]")
        merger.append(path_to_files + file_name)

#Write out the merged PDF
print("Saving as..", out_file_name)
merger.write(out_file_name)
merger.close()