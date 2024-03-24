"""
    file: ParseData.py
    description:
    Parse through Data
    1. will get each student ID and make an array making sure there are no duplicates
    2. will go through other files and get the attributes needed for each student ID
    3. will make a student in the student class and assign it all its variables
    4. will make an array of each student
    5. will print each of those arrays and make them into a csv file
"""

import pandas as pd
from dataclasses import dataclass


#FILES
eoc_checkpoint =  "../datafest_csv_data/checkpoints_eoc.csv"
pulse_checkpoint =  "../datafest_csv_data/checkpoints_pulse.csv"
items = "../datafest_csv_data/items.csv"
media_views = "../datafest_csv_data/media_views.csv"  #Student ID
page_views = "../datafest_csv_data/page_views.csv"   #Student ID needed
responses = "../datafest_csv_data/responses.csv"



@dataclass
class student:
    studentID: int  #eoc checkpoint bc easiest to assign
    engaged: []     # pageviews
    attempt: []     #reponses
    n_attempt:[]    #eoc checkpoint
    time: []        #recheck which datatype it needs to be
    # ^ dt saved and dt started needed




StudentID = []

#initial way of making a student
def make_student(CSVfile):
    df = pd.read_csv(CSVfile,sep=',', chunksize=10)

    for data in df:
        first_column = data.iloc[:, 0].str.strip(' ')  # Strip leading and trailing whitespace
        first_column = first_column.str[1:]
        Student = student(studentID=first_column)
        print(Student)





def read_pageviews(CSVfile):

    read = pd.read_csv(CSVfile, sep=',', )
    print(read)



"""
will add the attempts to each student 
"""
def read_responses(CSVfile):
    df = pd.read_csv(CSVfile, chunksize=10)

    for data in df:
        print(data)
        break


def main():
   # read_pageviews(file05)
   # read_responses(responses)
   make_student(eoc_checkpoint)


"""
This is to turn into a csv file for later 

01) function 
def writecsv(Report,filename):
    delim = ","
    writestring = report.x + delim + report.y + delim + report.lane + delim + report.time + delim + report.event
    with open(filename, "w") as file:
        file.write(writestring)

rep = Report()
filename = "test.csv"
writecsv(rep,filename)

02) command 
https://www.geeksforgeeks.org/convert-numpy-array-into-csv-file/

03) ALT 

"""



main()