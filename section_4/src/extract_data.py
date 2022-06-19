import datetime
import logging
import sys
from typing import Any, Dict, List, Optional
import requests
import json
import pandas as pd
import argparse

class BaseCountryCovidAPI():
    """Base extraction service class that contains most of extraction method and attributes"""
    COUNTRY=None
    START_DATE=None
    END_DATE=None
    BASE_URL = "https://api.covid19api.com/country/{0}/status/confirmed?from={1}T00:00:00Z&to={2}}T00:00:00Z"

    def _request(self, url) -> Any:
        try:
            resp = requests.get(url)
                
        except requests.ConnectionError as ce:
            logging.error(f"There was an error with the request, {ce}")

        if resp.status_code == 200:
            content = resp.content
        else:
            logging.error(f"Url {url} returned a non-200 status code {resp.status_code}")
            raise Exception("API Error")

        return content

    def _url_maker(self) -> str:
        final_url = self.BASE_URL.format(
            self.COUNTRY,
            self.START_DATE,
            self.END_DATE,
        )

        return final_url
    
    def _parse(self, content):
        json_content = json.load(content)

        final=[]
        for item in json_content:
            data={}
            data['country'] = item.get("Country")
            data['cases'] = item.get("Cases")
            data['date'] = item.get("Date")

            final.append(data)

        df = pd.DataFrame(final)
    
        try:
            df.to_csv('temp/covid_data.csv')
            logging.info("Successfully saved data to csv")
        except Exception as e:
            logging.error(f'Failed to save raw data . Error message {e}')

    def _main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--country", type=str, required=True, help="Target country")
        parser.add_argument("--start", type=str, required=True,help="Start date for the covid api")
        parser.add_argument("--end", type=str, default=default_end, required=True, help="End date for the covid api")

        default_end = datetime.datetime.now().strftime("%d-%m-%Y") #Default end time is today

        args = parser.parse_args()

        self.COUNTRY = args.country
        self.START = args.start
        self.END = args.end

        url = self._url_maker()

        content = self._request(url)

        self._parse(content)
