######################################################
# Author : Manisha Radhakrishna
# Organisation : Graduate Student in San Diego State Univeristy in Big Data Analytics Program
# Run Command : python /Users/Manisha/Documents/MS/SDSU/research/NOAA/Climate-Informatics-Lab/ManishaRadhakrishna/GHCN_data_load.py
# GHCN data link: https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/
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
    def load_data(data_path):
        countries = GHCN_data_load.get_file("https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-countries.txt",data_path)
        station_inventory = GHCN_data_load.get_file("https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt",data_path)
        ghcnd_stations = GHCN_data_load.get_file("https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/doc/ghcnd-stations.txt",data_path)
        GHCN_data_load.parse_ghcnd_stations(ghcnd_stations,data_path+"/stations")
        return

GHCN_data_load.load_data("/Users/Manisha/Documents/MS/SDSU/research/NOAA/Climate-Informatics-Lab/ManishaRadhakrishna/dataset")