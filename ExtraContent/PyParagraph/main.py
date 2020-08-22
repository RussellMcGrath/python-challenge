#import modules
import os
import re

#define resource file path
txtpath = os.path.join("raw_data","paragraph_1.txt")

#open resource file
txtfile = open(txtpath,"r")

#read resource file and create string
txtstring = txtfile.read()

#DETERMINE WORD COUNT
#split text file string into a list of words
wordlist = txtstring.split(" ")
#count number of words in word list
wordcount = len(wordlist)

#DETERMINE SENTENCE COUNT
#split text file string in a list of sentences
sentencelist = re.split("(?<=[.!?]) +", txtstring)
#count number of sentences in sentence list
sentencecount = len(sentencelist)

#DETERMINE AVG WORD LENGTH
#declare list to be used to store word lengths
wordlengthlist = []
#loop through each word in the word list
for word in range(len(wordlist)):
    #add the length of the current word to the lenth list
    wordlengthlist.append(len(wordlist[word]))
#calculate avg word length
avg_word_length = round(sum(wordlengthlist) / len(wordlengthlist),1)

#DETERMIN AVG SENTENCE LENGTH
#declare variables
sentencelengthlist = []
sentencesplit=[]
#loop through each sentence in the sentences list
for sentence in range(sentencecount):
    #split the current sentence in a list of words
    sentencesplit = re.split(" ", sentencelist[sentence])
    #add the lenge the current sentence to the length list
    sentencelengthlist.append(len(sentencesplit))
#calculate the avg length of the length list
avg_sent_length = round(sum(sentencelengthlist)/len(sentencelengthlist))

#print results
print(f"Word count: {wordcount}")
print(f"Sentence count: {sentencecount}")
print(f"Avg. word length: {avg_word_length} letters")
print(f"Avg. sentence lenge: {avg_sent_length} words")
