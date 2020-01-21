# DNA analysis

# This program reads in DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
# python dna_analysis.py myfile.fastq

# The sys module supports reading files, command-line arguments, etc.
import sys


# Function to convert the contents of dna_filename into a string of nucleotides
def filename_to_string(dna_filename):
    """
    dna_filename - the name of a file in expected file format
    Expected file format is: Starting with the second line of the file,
    every fourth line contains nucleotides.
    The function will read in all lines from the file containing nucleotides,
    concatenate them all into a single string, and return that string.
    """

    # Creates a file object from which data can be read.
    inputfile = open(dna_filename)

    # String containing all nucleotides that have been read from the file so
    # far
    seq = ""

    # The current line number (= the number of lines read so far).
    linenum = 0

    for line in inputfile:
        linenum = linenum + 1
        # if we are on the 2nd, 6th, 10th line...
        if linenum % 4 == 2:
            # Remove the newline characters from the end of the line
            line = line.rstrip()
            # Concatenate this line to the end of the current string
            seq = seq + line
    # close file
    inputfile.close()
    return seq


# Function to return GC Classification
def classify(gc_content):
    """
    gc_content - a number representing the GC content
    Returns a string representing GC Classification. Must return one of
    these: "low", "moderate", or "high"
    """

    if gc_content > 0.6:
        classification = "high"
    elif gc_content < 0.4:
        classification = "low"
    else:
        classification = "moderate"

    return classification


# Check if the user provided an argument
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this "
          " program.")
    sys.exit(2)

# Save the 1st argument provided by the user, as a string.
# Note: sys.argv[0] is the name of the program itself (dna_analysis.py)
filename = sys.argv[1]

# Open the file and read in all nucleotides into a single string of letters
nucleotides = filename_to_string(filename)

# Total nucleotides seen so far.
total_count = 0

# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
g_count = 0
c_count = 0
a_count = 0
t_count = 0

for base in nucleotides:
    total_count = total_count + 1

    if base == 'G' or base == 'C':
        gc_count = gc_count + 1
        if base == 'G':
            g_count = g_count + 1
        else:
            c_count = c_count + 1
    elif base == 'A' or base == 'T':
        at_count = at_count + 1
        if base == 'A':
            a_count = a_count + 1
        else:
            t_count = t_count + 1

sum_counts = g_count + c_count + a_count + t_count
gc_content = float(gc_count) / sum_counts
at_content = float(at_count) / sum_counts
length_nucl = len(nucleotides)
AT_GC = (a_count + t_count) / (g_count + c_count)
GC_class = classify(gc_content)

print('GC-content:', gc_content)
print('AT-content:', at_content)
print('G count:', g_count)
print('C count:', c_count)
print('A count:', a_count)
print('T count:', t_count)
print('Sum of G+C+A+T counts:', sum_counts)
print('Total count:', total_count)
print('Length of nucleotides:', length_nucl)
print('AT/GC Ratio:', AT_GC)
print('GC Classification:', GC_class, 'GC content')


assert total_count == length_nucl, "total_count != length of nucleotides"
# assert total_count == sum_counts, "total_count != sum of G+C+A+T"
