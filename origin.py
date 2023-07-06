# Import regex module
import re
# Import sys moduel
import sys
print("Opening origin.txt")

# Open/close reading of origin.txt file with "r"
with open("origin.txt", "r") as in_stream:
    print("Opening origin_output.txt")
    # Open/close creatation/writing of new origin_output.txt file with "w"
    with open('origin_output.txt', "w") as out_stream:
        # Assign regex pattern to variable (use as first argument in findall() method)
        # occurance = r'\b(heritab(?:ilit(?:y|ies)|le|ly)|inherit(?:ance|ed|ing|s|able))\b'
        # loop through read file line by line using enurmerate to get index of each line
        for num, line in enumerate(in_stream):
            # assign found occurances of word to variable (can use sys.argv[1] <--second element passed in command line, to pass regex in CLI); don't forget to ignorecase
            matches = re.findall(sys.argv[1], line, re.IGNORECASE)
            # findall returns a list of matches, and empty list [] if no match, so if length is greater than 0, loop through each match list
            if len(matches) > 0:
                for match in matches:
                    # print("d: ", num, match)
                    # Test with print to see data
                    print("data: ", f"{num +1}\t{match}\n")
                    # Create and write to origin_output.txt; use f-string to write to file (\t= tab, \n= new line)
                    out_stream.write(f"{num +1}\t{match}\n")
print("Done!")
print("origin.txt is closed?", in_stream.closed)
print("origin_output.txt is closed?", out_stream.closed)

# Comment