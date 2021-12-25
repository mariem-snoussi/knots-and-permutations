""""
    File name:      knots_and_permutations.py
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


"""
  Helper Functions

  
  1) Helper functions
  TODO: make sure we're consistently using top-down notations. l,r being the inputs. the relation would hold still. (California (+), FL(-))

  2) Testing and production:
  TODO: Description + input/output formats
  TODO: read from braid database, make sure all methods are compatible
  TODO: make an output pipeline that will give labelings at each level so that we get to compare
  

  3) Long-shot TODO (End-of-month):
  TODO: file an dfolder organization to store all results
  TODO: Store all permutation transpositions so that it takes no extra time calculating them to find all possible labelings (Hint: Dynamic Programming)

  4) (December/next-semester)
  TODO: Graphic interface for easier running and display of results

  
  TODO for fun: converting line notation to product of two-cycles
 
 

  
  
  
  DONE : function to create inverse of transposition - by Mariem 11/9
  DONE: download knotinfo database via Excel or csv, get rid of curly brackets/commas/etc. so it can actually be used by the code - done by Ben 11/7
  DONE: Create a function to convert transpositions in 2-cycle ((a_1a_2)) form to a line notation MS 11/8
  DONE: Create a function to convert general transpositions in  ((a_1a_2..a_n)) form to a line notation MS 11/9

  DONE: function to create inverse of transposition/ permutation (might end up being two separate functions as well) MS 11/15
  TODO: make p_conjugate(a,b). takes in two line notation permutations and produces the conjugate aba^(-1) MS 11/16
"""

def t_conjugate(a,b):
  #print("hello")
  a_inverse = tline_inverse(a)
  ba_inverse = multiply_transpositions(a_inverse, b)
  conjugate = multiply_transpositions(ba_inverse, a)
  return conjugate
  # returns aba^-1

def tline_inverse(transposition):
  #reverses permutation/transposition in line notation
  result = [0]*len(transposition)
  #switching lines
  for i in range(len(transposition)):
    result[transposition[i]] = i
  #print(result)
  return result


def transposition_to_line(transposition, n):
  result_line = [0]*n

  #initialize result to identity
  for j in range(n):
    result_line[j] = j

  for i in range(len(transposition)-1):
      result_line[transposition[i]] = transposition[i+1]
  #last element maps to first elemnt in transposition
  result_line[transposition[-1]] = transposition[0]
  return transposition

def tcycle_inverse(transposition):
  inverted = [0]*len(transposition)
  for i in range(len(transposition)):
    inverted[len(transposition) - i-1] = transposition[i]
  return inverted

#this one takes user input
def multiply_transpositions(p1,p2):
  #returns p2*p1
  #gets user input
    # input format is "a b c d"
    # p1 = input("input permutation p1 : ")
    # p2 = input("input permutation p2 : ")
    # #string formatting and casting into integers
    # p1 = p1.split(" ")
    # p2 = p2.split(" ")
    # for i in range(len(p1)):
    #     p1[i] = int(p1[i])
    #     p2[i] = int(p2[i])
    #initialize
    n = len(p1)

    product = [0] * len(p1)
    #print(len(product))
    #product might not always be a transposition
    #product will be a list of length n
    for i in range(n):  #starts at 0 and goes to n-1
        product[i] = p2[p1[i] - 1]

    #print("product p2*p1 is: ", product)
    return product

# this one if for hard-coding
def multiply_two_cycle_transpositions(p1, p2):
    product = [0] * len(p1)
    #print(len(product))
    #product might not always be a transposition
    #product will be a list of length n
    for i in range(len(p1)): 
       #starts at 0 and goes to n-1
        product[i] = p2[p1[i] - 1]
    #print("product p2*p1 is: ", product)

    return product


def two_cycle_transposition_to_line(transpositions, n):
    # t1 = (ab)
    # becomes p1 = [x_0, ..., x_{n-1}]
    line_permutation = [0]*n
    #creates identity permutation
    for i in range(n):
      line_permutation[i] = i
    line_permutation[transpositions[0]] = transpositions[1]
    line_permutation[transpositions[1]] = transpositions[0]

    return line_permutation


# def t_conjugate(a, b):
#     #returns aba (for 2-cycles only, TODO generalization)
#     #transposition conjugate
#     ba = multiply_two_cycle_transpositions(a, b)
#     c = multiply_two_cycle_transpositions(ba,a)
#     return c


#https://en.wikipedia.org/wiki/Braid_group
"""This returns the labels of strands after traversing a crossing, for example S_1 would be a positive crossing using the first two strands."""

def traverse_crossing():
    #if braid is in group B_n then len(labels) = n
    n = int(input("Enter braid group generator type. Type n for S_n and -n for S_{n^(-1)}: "))
    labels = input(
        "Enter a comma seperated list of ordered transposition labels: ")
    labels = labels.split(",")
    c = labels[n - 1]
    a = labels[n]

    #if positive crossing
    result_transposition = t_conjugate(c, a)
    labels[n - 1] = a
    labels[n] = result_transposition

    #if negative crossing (the wirtinger relation is the same for negative and positive crossings labeeld with 2-cycles. as the 2-cycles a^(-1) and a are equivalent)
    result_transposition = t_conjugate(c, a)
    labels[n - 1] = a
    labels[n] = result_transposition

    return labels



def traverse_crossing(labels, n):
    #if braid is in group B_n then len(labels) = 
    # print("beginning label is")
    # print(labels)
    c = labels[n - 1]
    a = labels[n]

    #if positive crossing
    result_transposition = t_conjugate(c, a)
    #print("result_transoposition")
    #print(result_transposition)
    labels[n - 1] = a
    labels[n] = result_transposition

    #if negative crossing (the wirtinger relationis the same for negative and positive crossings labeeld with 2-cycles. as the 2-cycles a^(-1) and a are equivalent)
    result_transposition = t_conjugate(c, a)
    labels[n - 1] = a
    labels[n] = result_transposition
    # print("result label is")
    # print(labels)
    return labels


def label_knot(braids_list, beginning_labels):
  # print(beginning_labels)
  all_labels = []
  label_string = ""
  current_labels = beginning_labels
  print("current_labels")
  print(current_labels)
  #all_labels.add("Hello")
  for i in range(len(braids_list)):
   
    #print(current_labels)
    label_string += str(current_labels) + "\n"
    all_labels += current_labels
    result_labels = traverse_crossing(current_labels, int(braids_list[i]))
    current_labels = result_labels
  all_labels += current_labels
  label_string += str(current_labels )+ "\n"
  print("result labeling of braid is : ")
  print(label_string)
  return all_labels


#we know a labeling is correct of the initial and last labels are the same
def labeling_is_valid(AllLabels_list):
  if (AllLabels_list[0] == AllLabels_list[len(AllLabels_list)-1]):
    return True
  return False

def string_labeling_valid(labeling_string):
  labels = labeling_string.split("\n")
  return labels[0] == labels[-1]

def main():

  # import csv
  # all_braids = []
  # with open('knotinfo_no_curls.csv') as csvfile:
  #   rowreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
  #   for row in rowreader:
  #     all_braids.append(row)
  #   print(all_braids)

  perm_inverse([0,4,1,2,3])
    
    #multiply_transpositions()
    #multiply_transpositions()
    

if __name__ == "__main__":
    main()
