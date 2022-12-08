import codecs

# This function takes a word and an integer n as input and returns a list of n-grams
# for that word
def word_to_ngrams(word, n):
  ngrams = []
  
  # Loop through the word, creating an n-gram for each group of n characters
  for i in range(len(word)-n+1):
    ngrams.append(word[i:i+n])
    
  return ngrams

# Open the wordlist.txt file and read each line
with codecs.open('wordlist.txt', 'r', encoding='utf-8') as f:
  # Create an empty dictionary to store the n-grams and their counts
  ngram_counts = {}
  
  # Prompt the user to enter the value of n
  n = int(input("Enter the value of n: "))

  # Check that the value of n is between 3 and 6
  if n < 3 or n > 6:
    print("Error: the value of n must be between 3 and 6.")
    exit()
  
  for line in f:
    # Remove any leading or trailing whitespace from the line
    line = line.strip()

    # Remove any formatting from the line
    line = line.replace(",", "").replace(".", "").replace("-", "")

    # Convert the line to its corresponding n-grams
    ngrams = word_to_ngrams(line, n)
    
    # Loop through the n-grams and update their counts in the dictionary
    for ngram in ngrams:
      if ngram in ngram_counts:
        ngram_counts[ngram] += 1
      else:
        ngram_counts[ngram] = 1
  
# Open the ngramoutput.txt file for writing
with codecs.open('ngramoutput.txt', 'w', encoding='utf-8') as f:
  # Create a list of tuples containing the n-grams and their counts,
  # sorted in descending order by count
  ngram_counts_sorted = sorted(ngram_counts.items(), key=lambda x: x[1], reverse=True)
  
  # Write each n-gram to the file on a new line
  for ngram, count in ngram_counts_sorted:
    f.write(ngram + "\n")
