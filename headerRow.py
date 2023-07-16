# write the output file header row, close it after
CSV_OUTPUT = "processJSON-RESULTS.csv"      # initialize variables 

with open (CSV_OUTPUT, "a") as outputfile:
    outputfile.write("Domain;IP;DNS;ASN;Registrar;Created;Expires;Siteadvisor;FQDNs;theDataLastUpdated;\n")
outputfile.close()
