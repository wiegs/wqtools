# write the output file header row, close it after
csv_output = "processJSON-RESULTS.csv"      # initialize variables 

with open (csv_output, "a") as outputfile:   
    outputfile.write("Domain;IP;DNS;ASN;Registrar;Created;Expires;Siteadvisor;FQDNs\n")
outputfile.close()
