import csv
'''file = open('Exa.csv')
file_reader = csv.reader(file)
#print(list(file_reader))
for i in file_reader:
    print(file_reader.line_num,i)
'''
output_file = open('out.py','a',newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['1','2','3','4'])
output_writer.writerow(['11','22','33','44'])
