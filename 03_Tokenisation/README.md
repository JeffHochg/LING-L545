### Tokenisation Instructions

maxmatch.py opens files by the names of original.train.txt and dictionary.txt
You can either have these files in the directory, or change the filenames within the script
If I get around to it i'll have it take files from the command line 

To make the original and tokenised sentence sets, first use tokeniser.py to construct original.txt, then tokenisationJ.py to construct the tokenised variant.
Head and tail to make the respective .train.txt and .test.txt, run maxmatch, and evaluate
### Evaluation

Using the provided evaluate script, my output.test.txt, which was created from my maxmatch.py and original.test.txt files, returns a word error rate of 44.95%.
