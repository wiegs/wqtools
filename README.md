# wqtools
Load JSON formatted report data into CSV file for easy review of multiple domains.

This script will collect the following fields from the JSON report and put them into a row on a CSV file:

**Domain; IP; DNS; ASN; Registrar; Created; Expires; Siteadvisor; FQDNs; theDataLastUpdated;**

1. set ENVIRONMENT variable to contain the WQ_API_KEY in bash

Use your actual key here from the [WisQuas Account page](https://wisquas.lostrabbitlabs.com/account). Alternately, load from a password vault as in this [example](https://github.com/wiegs/wqtools/blob/main/setupEnv.sh).
```
export WQ_API_KEY=""
```
2. create a file with a list of domains, 1 per row called **lildomains.txt**

3. run getResults.py to collect a JSON report on a domain you have previously scanned
   
downloads to /output/ folder
```
mkdir output
python getResults.py
```
4. generate headerRow.py

creates file **processJSON-RESULTS.csv**
```
python headerRow.py
```
5. process the JSON formatted output file with **processJSON.py**

```
python processJSON.py output/example.com_report.json
```
6. collect results from **processJSON-RESULTS.csv**

the CSV file is separated using semicolon 
