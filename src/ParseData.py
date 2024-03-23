"""
    file: ParseData.py
    description:
    Parse through Data to get each individual section
"""

import pandas as pd



file04 =  "../datafest_csv_data/media_views.csv"  #Student ID
file05 = "../datafest_csv_data/page_views.csv"   #Student ID needed
file06 = "../datafest_csv_data/responses.csv"

"""
Reads the data from the pageviews 

:param 
:return
"""

def read_pageviews(CSVfile):

    read = pd.read_csv(CSVfile, sep=',', )

#dtype={"book": "string" , "release": "string", "chapter": "string" ,"page": "string",
 #                                               "chapter_number": "string", "section_number": "string", "institution_id": "int"})

def read_responses(CSVfile):
    read = pd.read_csv(CSVfile, sep=',',low_memory=False)







def main():
    print(read_pageviews(file05))

main()