# Experiment No.5 Program to count the occurrences of each word in a given string sentence.
def word_count(str):
     counts = dict()
     words = str.split()

     for word in words:
          if word in counts:
               counts[word] += 1
          else:
               counts[word] = 1
     
     return counts

str=input("Enter Sentence: ")
print(word_count(str))