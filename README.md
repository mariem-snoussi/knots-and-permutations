Get knotinfo notations in csv file, store them,
take braidword as a string,
write string processing

Usage :  python reading_data.py

## reading_data

Reading data is where the script is executed and helper functions from labelingKnots are called.

### 1) test_transposition(labels, n) :
this is a function that takes in an array of transposition labels (in line notation) and n a braid group generator.
It calls traverse_crossing(labels, n) from labelingKnots to test the accuracy of it ie. whether the wirtenger relation is verified

### 2) get_initial_labels(braidGroup) :
this function gets the input of the first labels of the braid. they are formatted and stored to be used later during the labeling process.
braidGtoup refers to how many strands the braid has. This is decided by the user for the moment, as braid notations data don't necessarily provide that information.
The user is expected to in put as many transpositions as the braidGroup.
For example, a braidGroup of 3 signifies 3 strands and thus three intial transpositions.
This function returns a list of the intial labels.

### 3) read_data_from_csv():
This reads data from knot info csv file. Some string formatting also happens in the process. this function returns a list of all braid notations in the file.

### 4) pipeOneBraid(Braid, initialLabeling):
This function, called from main(), takes one braid (its notation) and an inital label and prints the labeling for the whole knot.

## labelingKnots functions
