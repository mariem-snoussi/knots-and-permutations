"""This is where we could extract and process data and then call main (/new class) on it"""

import csv
  
with open('knotinfo_no_curls.csv') as csvfile:
  rowreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
  for row in rowreader:
    print(row)