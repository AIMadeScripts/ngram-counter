# ngram-counter

Run this by
``git clone https://github.com/AIMadeScripts/ngram-counter.git``
``cd ngram-counter``
``python3 run.py``

This project will analyze all the words in wordlist.txt and find their ngram values (where n = input number) eg;
3gram of hello
hel
ell
llo

Then it will find where those ngrams are inside all of the words in the wordlist.txt and print out their position for example:
First digit = how many times it appeared.
Second digit = Where it appeared in the word it found.
Final keyspace = the ngram checked.
1 [0] hel
1 [1] ell
1 [2] llo

This allows us to see that from the below example results:
298 [3] 12345
239 [4] 12345
235 [3] 23456
233 [5] 12345
175 [3] a1234
144 [4] er123
141 [6] 12345

12345 appears after 3 characters the most frequently such as
Joe12345

then again 12345 appears after 4 characters frequently
John12345

From here we can make rules/masks based on the interpreted results
(for hashcat as an example)
