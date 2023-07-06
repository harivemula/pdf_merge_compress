from pdfc.pdf_compressor import compress

in_file_name = input("Input File Name: ")
out_file_name = input("Output File Name: ")
compression_level = int(input("Compress level (0-4):"))
compress(in_file_name, out_file_name, power=compression_level)