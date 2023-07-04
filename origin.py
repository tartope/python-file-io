import re
print("Opening origin.txt")

with open("origin.txt", "r") as in_stream:
    print("Opening origin_output.txt")
    with open('origin_output.txt', "w") as out_stream:
        occurance = r'\b(heritab(?:ilit(?:y|ies)|le|ly)|inherit(?:ance|ed|ing|s|able))\b'
        for num, line in enumerate(in_stream):
            matches = re.findall(occurance, line, re.IGNORECASE)
            if len(matches) > 0:
                for match in matches:
                    # print("d: ", num, match)
                    print("data: ", f"{num +1}\t{match}\n")
                    out_stream.write(f"{num +1}\t{match}\n")
print("Done!")
print("origin.txt is closed?", in_stream.closed)
print("origin_output.txt is closed?", out_stream.closed)