# Create a dictionary to hold the counts of each unique line in the file
counts = {}

# Open the input file in read-only mode and iterate over its lines
with open('output.txt', 'r') as f:
    for line in f:
        # Strip any leading or trailing whitespace from the line
        line = line.strip()

        # If the line is not in the counts dictionary, add it with a count of 1
        if line not in counts:
            counts[line] = 1
        # Otherwise, increment the count for that line
        else:
            counts[line] += 1

# Sort the counts dictionary by the number of duplicates in each line, with the
# lines having the most duplicates at the top
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

# Open the FinalResults.txt file in write mode and write the sorted counts
# to the file, one line at a time
with open('FinalResults.txt', 'w') as f:
    for line, count in sorted_counts:
        f.write(f'{count} {line}\n')
