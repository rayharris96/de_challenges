# Section 4

## Problem Solutions

For this problem set, the tasks are to extract data using an API and display the data using charts.

I have written python codes which do the following:
- in src/extract_data.py -> this code does the extraction of Covid data over time and saves the data as a csv in the temp/ folder. It takes in arguments such as country, and the start and end date range
- To run the extraction code, run ```python src/extract_data.py --country <Singapore> --start <YYYY-MM-DD> --end <YYYY-MM-DD>``` where start is the start date and end is the end date. You can also modify the country if you are interested in getting data from another country.
- Once the data is at temp folder, run ```python src/visualize.py```
- The chart will be dynamically generated according to your input in the extraction.py arguments. The final charts can be found in `charts/`