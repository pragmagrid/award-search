# NSF award search summary 

Display CSV file as a searchable, filterable, pretty HTML table. 
Original csv-to-html code from http://derekeder.github.io/csv-to-html-table/
See original csv-to-html setup instructions in readme-csv-to-html.md (renamed from README.md)
Download 2017-12-20 per repo latest available commit (Latest commit 429cd43 on Jan 17, 2017)

Added: 

  + csv file processing 
  + creation of summary html files

## Usage

#### 1. Download  distribution

``` bash
git clone https://github.com/pragmagrid/award-search
```
The resulting directory `award-search` should be in `/var/www/html` 

#### 2. Download csv file 

From NSF simple search results https://www.nsf.gov/awardsearch/
download resulting CSV file, rename as Awards.csv and put in `award-search/data/`

#### 3. Process CSV file 

Execute the following command:

``` bash
cd award-search
./readcsv.py data/Awards.csv
```
This step creates an edited version of csv file `award-search/data/Awards-edited.csv` that will be 
used to load  into the web page. In addition, for each award that is listed in
this edited csv file, there is a summary html file placed in `award-search/abstracts/`. The
summary files represent a specific award description.

Each time the `Award.csv` file is updated this step will need to be rerun 
to recreated needed sumamries and updated edited csv file.

#### 3. View results

Point your browser to http://your.host/award-search


