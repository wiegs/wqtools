# wqtools
load JSON formatted report data into CSV file for easy review of multiple domains

This script will collect the following fields from the report:

**Domain; IP; DNS; ASN; Registrar; Created; Expires; Siteadvisor; FQDNs; theDataLastUpdated;**

1. set ENVIRONMENT variable to contain the WQ_API_KEY in bash

use your actual key here from the [WisQuas Account page](https://wisquas.lostrabbitlabs.com/account)
```
export WQ_API_KEY=""
```
2. run getResults.py to collect a JSON report on a domain you have previously scanned
   
downloads to /output/ folder
```
mkdir output
python getResults.py
```
3. generate headerRow.py

creates file **processJSON-RESULTS.csv**
```
python headerRow.py
```
4. process the JSON formatted output file with **processJSON.py**

```
python processJSON.py output/example.com_report.json
```
5. collect results from **processJSON-RESULTS.csv**

the CSV file is separated using semicolon 
