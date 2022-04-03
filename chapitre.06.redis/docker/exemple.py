#!/usr/bin/python
# -*- encoding: utf-8 -*-
################################################################################
#
#    2020 Rudi Bruchez <rudi@pachadata.com>.
#    Licence : MIT. Pour livre Eyrolles - les bases de données NoSQL
#
################################################################################

import requests
import time

# --------------------------------------------------
# --                   exemple                    --
# --------------------------------------------------
response = requests.get('https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json')

if response:
   data = response.json()
   station17 = data["data"]["stations"][17]
   print(time.asctime(time.gmtime(station17["last_reported"])))

