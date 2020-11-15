# ================================================================= #
# Houston Independent School District                               #
# Franklin Elementary School                                        #
#                                                                   #
# Script to split a PDF file into single PDF pages for each student #
# Created:       11/14/2020                                         #
# Last Modified: 11/14/2020                                         #
# ================================================================= #

# Import libraries
import os
from PyPDF2 import PdfFileWriter, PdfFileReader


# Define the input file
# Just replace the teacher name, leave the rest alone
teacher = 'Teacher_Name' # Or file name, without .pdf
inputpdf = PdfFileReader(open('input/' + teacher + '.pdf', 'rb'))


# Define the list of students
# Needs to match the order in the PDF file
name = ['student1_name',
        'student2_name',
        'student3_name',
        'student4_name',
        '...'
        ]


# Generate the output files
for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open('output/document%s.pdf' % i, 'wb') as outputStream:
        output.write(outputStream)

# Rename the output files
for i in range(len(name)):
    last = str(i)
    filename = 'document' + last
    os.rename('output/'+filename + '.pdf','output/'+name[i]+ '.pdf')