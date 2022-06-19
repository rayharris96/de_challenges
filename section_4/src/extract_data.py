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
    BASE_URL = "https://api.covid19api.com/country/{0}/status/confirmed?from={1}T00:00:00Z&to={2}T00:00:00Z"

    def _request(self, url) -> Any:
        """
        Simple method for request fetching
        """
        try:
            resp = requests.get(url)
                
        except requests.ConnectionError as ce:
            logging.error(f"There was an error with the request, {ce}")

        if resp.status_code == 200:
            content = resp.content
        else:
            logging.error(f"Url {url} returned a non-200 status code {resp.status_code}")
            raise Exception("API Error")

        #Return data as content - bytes
        return content

    def _url_maker(self, country, start, end) -> str:
        """
        Method to create and format final url
        """
        final_url = self.BASE_URL.format(
            country,
            start,
            end
        )

        return final_url
    
    def _parse(self, content):
        """
        Method to parse returned JSON data, build a dataframe and save it as a csv
        """
        json_content = json.loads(content.decode('utf-8'))

        final=[]
        for item in json_content:
            data={}
            data['country'] = item.get("Country")
            data['cases'] = item.get("Cases")
            data['date'] = item.get("Date")

            final.append(data)

        df = pd.DataFrame(final)
    
        try:
            df.to_csv('../temp/covid_data.csv')
            print("Successfully saved data to csv")
        except Exception as e:
            logging.error(f'Failed to save raw data . Error message {e}')

    def _main(self, args):
        """
        Main wrapper of methods to interact with inputs and coordinate with class methods
        """

        country= args.country
        start = args.start
        end = args.end

        url = self._url_maker(country, start, end)

        content = self._request(url)

        self._parse(content)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--country", type=str, required=True, help="Target country")
    parser.add_argument("--start", type=str, required=True, help="Start date for the covid api")
    default_end = datetime.datetime.now().strftime("%Y-%m-%d") #Default end time is today
    parser.add_argument("--end", type=str, default=default_end, help="End date for the covid api")
    args = parser.parse_args()
    instance = BaseCountryCovidAPI()
    instance._main(args)
