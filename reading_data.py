""""
    File name:      reading_data.py
    File type:      script
    Author:         B. Bruncati, P. Cahn, M. Snoussi, P. Wilson
    Date created:   26 October 2021
    Date updated B.B.: 2021: Nov 07 
    Date updated P.C.: 2021:
    Date updated M.S.: 2021: Nov 27
    Date updated P.W.: 2021: 
    Last update:   2021: Nov 27 (M.S.); 

    Usage: TODO

"""

"""This is where we could extract and process data and then call main (/new class) on it"""

import csv
import labelingKnots

def test_transposition(labels, n):
  labelingKnots.traverse_crossing(labels, n)

def get_initial_labels(braidGroup):
  initial_labeling = []
  for i in range(braidGroup):
    t = input("input transposition in second line format: ")
    #string formatting and casting into integers
    t = t.split(" ")
    for j in range(len(t)):
         t[j] = int(t[j])
    initial_labeling.append(t)

  return initial_labeling

def pipeOneBraid(Braid, initialLabeling):
  print(Braid)
  labelingKnots.label_knot(Braid, initialLabeling)
  #print(Labeling.multiply_two_cycle_transpositions([0,1],[1,0]))
  


def read_data_from_csv():
  with open('knotinfo_no_curls.csv') as csvfile:
    braidList = []
    rowreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
    for row in rowreader:
      row[0] = row[0].replace('"',"")
      row[-1] = row[-1].replace('"',"")
      braidList.append(row)
  return braidList

def main() : 
  braidList = read_data_from_csv()
  braidGroup = int(input("Input braid group n: "))
  initialLabeling = get_initial_labels(braidGroup)
  pipeOneBraid(braidList[2], initialLabeling)
  #test_transposition([[1, 2, 0], [0, 2, 1], [2, 1, 0]], 1)



if __name__ == "__main__":
    main()



