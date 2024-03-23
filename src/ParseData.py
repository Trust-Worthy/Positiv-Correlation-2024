"""
    file: ParseData.py
    description:
    Parse through Data to get each individual section
"""

import dataclasses as dataclass

file01 = "checkpoints_eoc.csv"
file02 = "checkpoints_pulse.csv"
file03 = "items.csv"
file04 = "media_views.csv"  #Student ID
file05 = "page_views.csv"   #Student ID needed
file06 = "responses.csv"

@dataclass
class Student:
    engaged : list # active time -> page_views.csv
    intitute_id : int # page_views.csv
    off_page_breif : list # (filter through for 45 minutes) page_views.csv
    tried_again_clicks : list # page_views.csv
    was_complete : list # page_views.csv
    attempt : list # responses.csv
    dt_submitted : list # responses.csv
    item_type : list # responses.csv
    lrn_dt_started : list # responses.csv
    lrn_dt_saved : list # responses.csv
    page : list # responses.csv
    points_earned : list # responses.csv
    points_possible : list # responses.csv
    release_version : int # responses.csv

#test01 to give
def main():

    # while going through the data we 

    pass