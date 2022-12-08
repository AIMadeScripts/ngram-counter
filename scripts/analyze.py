# Open the ngramoutput.txt file in read mode
with open("ngramoutput.txt", "r") as ngram_file:
    # Read each line of the file
    for line in ngram_file:
        # Open the wordlist.txt file in read mode
        with open("wordlist.txt", "r") as wordlist_file:
            # Read each word in the wordlist
            for word in wordlist_file:
                # Check if the line from ngramoutput.txt exists in the word from wordlist.txt
                if line in word:
                    # If it does, get the position of the line in the word
                    position = word.index(line)
                    # Print the position and the line from ngramoutput.txt to the output file
                    with open("output.txt", "a") as output_file:
                        output_file.write(f"[{position}] {line}")
