"""
    file: ParseData.py
    description: reads and saves necessary data from files in full_03_04
    Parse through Data to get each individual section
"""
from dataclasses import dataclass
import csv
import pandas as pd

file01 = "../datafest_csv_data/checkpoints_eoc.csv"
file02 = "../datafest_csv_data/checkpoints_pulse.csv"
file03 = "../datafest_csv_data/items.csv"
file04 = "../datafest_csv_data//media_views.csv"  #Student ID
file05 = ".../datafest_csv_data/page_views.csv"   #Student ID needed
#file06 = "../datafest_csv_data/responses.csv"

@dataclass
class Student:
    engaged : list # active time -> page_views.csv
    # intitute_id : int # page_views.csv
    # off_page_breif : list # (filter through for 45 minutes) page_views.csv
    # tried_again_clicks : list # page_views.csv
    # was_complete : list # page_views.csv
    # attempt : list # responses.csv
    # dt_submitted : list # responses.csv
    # item_type : list # responses.csv
    # lrn_dt_started : list # responses.csv
    # lrn_dt_saved : list # responses.csv
    # page : list # responses.csv
    # points_earned : list # responses.csv
    # points_possible : list # responses.csv
    # release_version : int # responses.csv
        
"""
Reads the data from the pageviews 
:param 
:return
"""

def read_pageviews(CSVfile):
    read = pd.read_csv(CSVfile, sep=',')

def main():
    read_pageviews(file05)
    
    students = dict
    chunk_size = 1

    for chunk in pd.read_csv(file01, chunksize=chunk_size): 
        print(chunk)

main()