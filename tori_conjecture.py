import labelingKnots
import csv

def read_data_from_csv():
  with open('torusknots.csv') as csvfile:
    braidList = []
    rowreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
    for row in rowreader:
      row[0] = row[0].replace('"',"")
      row[-1] = row[-1].replace('"',"")
      braidList.append(row)
  return braidList
# http://przyrbwn.icm.edu.pl/APP/PDF/98/a098z6p01.pdf

#makes braid notation for pretzel knot (p,q)
# q < 0
def make_torus_string(p,q):
    string = '"'
    for j in range(q):
        for i in range(p):
            string += str(i+1) +","
    string = string[:-1]
    string += '"'
    print(string)
    return string

# makes braid notations of pretzel knots (q,q+1) 1<q<n
def make_torus_braids_file(n):
    f = open("torusknots.csv", "w")
    file_string = ""
    for k in range(2,n+1):
        file_string += make_torus_string(k,k+1) + "\n"
    f.write(file_string)
    f.close()

#makes inital transpositon labelings in (0,1), (0,2), (0,p-1) form
def make_p_disjoint_transpositions(p):
    two_cycle_transpositions = []
    for i in range(1,p):
        print(labelingKnots.two_cycle_transposition_to_line([0,i],p))
        two_cycle_transpositions.append(labelingKnots.two_cycle_transposition_to_line([0,i],p))

    print(two_cycle_transpositions)
    return two_cycle_transpositions

def pipeOneBraid(Braid, initialLabeling):
  print(Braid)
  labeling_string = labelingKnots.label_knot(Braid, initialLabeling)
  print(labelingKnots.string_labeling_valid(labeling_string))

def test_conjecture():
    braidList = read_data_from_csv()
    for braid in braidList:
        print(braid)
        braidGroup = int(max(braid))+ 1
        initialLabeling = make_p_disjoint_transpositions(braidGroup)
        pipeOneBraid(braid, initialLabeling)
    return 0
def main():
    #make_torus_string(3,4)
    make_torus_braids_file(10)
    #make_p_disjoint_transpositions(4)
    test_conjecture()

if __name__ == "__main__":
    main()
