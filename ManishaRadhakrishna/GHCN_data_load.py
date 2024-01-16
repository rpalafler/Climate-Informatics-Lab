######################################################
# Author : Manisha Radhakrishna
# Organisation : Graduate Student in San Diego State Univeristy in Big Data Analytics Program
# Run Command : python /Users/Manisha/Documents/MS/SDSU/research/NOAA/Climate-Informatics-Lab/ManishaRadhakrishna/GHCN_data_load.py
# GHCN data link: https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/
#                 https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html
# GCP : bigquery-public-data.ghcn_d : https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ghcn_d&page=dataset&project=gsv-and-homeless-analysis
# AWS S3 : https://noaa-ghcn-pds.s3.amazonaws.com/index.html#csv/by_station/ 
# CONTENTS OF ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily
# all:                  if you want all of GHCN-Daily :: Directory with ".dly" files for all of GHCN-Daily
# gsn:                  if you only want the GCOS Surface Network (GSN) :: Directory with ".dly" files for the GCOS Surface Network (GSN)
# hcn:                  if you only want the U.S. Historical Climatology Network (U.S. HCN) :: .Directory with ".dly" files for U.S. HCN
# by_year:              Directory with GHCN Daily files parsed into yearly subsets with observation times where available.  See the /by_year/readme.txt and  /by_year/ghcn-daily-by_year-format.rtf  files for further details
# by_station:           Directory of GHCN daily station data in period of record comma separate (csv) files.  See readme-by_station.txt for additional details
# grid:	                Directory with the GHCN-Daily gridded dataset known as HadGHCND
# papers:		        Directory with pdf versions of journal articles relevant to the GHCN-Daily dataset
# figures:	            Directory containing figures that summarize the inventory  and processing of GHCN-Daily station records
# superghcnd:	        Directory containing a comma delimited format of GHCN-Daily with station metadata integrated into the data.  Two files  are provided each day.  The superghcnd_full file contains all GHCN-Daily data in comma delimited format and the superghcnd_diff file which contains the differences in the dataset between two successive update runs.  See the readme.txt file in the superghcnd directory for more details.
# ghcnd-all.tar.gz:     TAR file of the GZIP-compressed files in the "all" directory
# ghcnd-gsn.tar.gz:     TAR file of the GZIP-compressed "gsn" directory
# ghcnd-hcn.tar.gz:     TAR file of the GZIP-compressed "hcn" directory
# ghcnd-countries.txt:  List of country codes (FIPS) and names
# ghcnd-inventory.txt:  File listing the periods of record for each station and element
# ghcnd-stations.txt:   List of stations and their metadata (e.g., coordinates)
# ghcnd-states.txt:     List of U.S. state and Canadian Province codes used in ghcnd-stations.txt
# ghcnd-version.txt:    File that specifies the current version of GHCN Daily
# mingle-list.txt:      File that provides a list of each source and source identifiers associated with each GHCN-Daily station.
# readme.txt:           https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt
# status.txt:           Notes on the current status of GHCN-Daily

######################################################

import re
from pathlib import Path
import numpy as np
import requests
import json
import subprocess
import pandas as pd
import time
from builtins import *
from datetime import datetime
import warnings
import wget
import os

warnings.filterwarnings("ignore")
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)


class GHCN_data_load:
    CURRENT_DATE = datetime.now().strftime("%Y%m%d")

    @staticmethod
    def list_files(url):
        return

    @staticmethod
    def get_file(file_link,output_path):
        file_name=file_link.split('/')[-1]
        if os.path.isfile(output_path+"/"+file_name):
            os.remove(output_path+"/"+file_name)
        return(wget.download(file_link, out=output_path))
    
    @staticmethod
    def parse_ghcnd_stations(ghcnd_stations,data_path):
        # print(ghcnd_stations)
        if not os.path.isdir(data_path):
            os.mkdir(data_path)
        station_file = open(ghcnd_stations,'r')
        file_dtls=station_file.read()
        for i in file_dtls.split('\n')[:2]: # @TODO : Remove limit while deploying
            GHCN_data_load.get_file("https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/"+i.split('  ')[0]+".csv",data_path)
            # GHCN_data_load.get_file(,data_path)

    @staticmethod
    def parse_countries_file(file_path):
        country=tuple()
        if os.path.isfile(file_path):
            file_read = open(file_path,'r')
            for i in file_read.read().split('\n')[:2]: # @TODO : Remove limit while deploying
                country+=(i.split(' ')[0],(' '.join(i.split(' ')[1:])).strip()),
        return pd.DataFrame(list(country),columns=('country_code','country_name'))
    
    @staticmethod
    def parse_inventory_file(file_path):
        country=tuple()
        if os.path.isfile(file_path):
            file_read = open(file_path,'r')
            for i in file_read.read().split('\n')[:2]: # @TODO : Remove limit while deploying
                print(i.split(' '))
                # country+=(i.split(' ')[0],(' '.join(i.split(' ')[1:])).strip()),
        return 
        # pd.DataFrame(list(country),columns=('country_code','name'))
    
    @staticmethod
    def load_data(data_path):
        # countries = GHCN_data_load.get_file("https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-countries.txt",data_path)
        # countries_df = GHCN_data_load.parse_countries_file(countries)
        # print(countries_df.head())
        station_inventory = GHCN_data_load.get_file("https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt",data_path)
        inventory_df = GHCN_data_load.parse_inventory_file(station_inventory)
        # print(inventory_df.head())

        # ghcnd_stations = GHCN_data_load.get_file("https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/doc/ghcnd-stations.txt",data_path)
        # GHCN_data_load.parse_ghcnd_stations(ghcnd_stations,data_path+"/stations")
        return

GHCN_data_load.load_data("/Users/Manisha/Documents/MS/SDSU/research/NOAA/Climate-Informatics-Lab/ManishaRadhakrishna/dataset")