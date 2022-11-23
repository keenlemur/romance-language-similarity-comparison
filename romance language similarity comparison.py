# Romance language similarity comparison by Justin Vastola
# This is a tool to compare similarity of sentences in romance languages using jaccard similarity
# Note that jaccard similarity for language comparison is less accurate than dedicated Natural Language Processing (NLP) tools 

import statistics

# 1. JACCARD SIMILARITY
# Define a jaccard similarity function
# This determines how similar a sentence is to another sentence
def jaccard_similarity(a, b):
    # Convert to set
    a = set(a)
    b = set(b)
    # Calculate jaccard similarity
    j = float(len(a.intersection(b))) / len(a.union(b))
    return j


# 2. INITIAL LANGUAGE SENTENCES
# Enter sentences in Italian (IT), Portuguese (PT), Spanish (ES), Catalan (CA), and French (FR)
IT1initial = "Il mio nome è Maria"
PT2initial = "Meu nome é Maria"
ES3initial = "Mi nombre es Maria"
CA4initial = "El meu nom és Maria"
FR5initial = "Mon nom est Maria"


# 3. SPLIT SENTENCES INTO STRINGS
# Split the words in a sentence into separate strings within a list
# We do this because jaccard similarity requires separate strings for accuracy
# The list ["mi", "nombre", "es"] is more accurate than ["mi nombre es"] because the first example is multiple strings and the second is one string
# Instead of having to create a list like ["mi", "nombre", "es"] for ES3initial, you can simply write "mi nombre es"
# Instead of making each word a string yourself (by adding quotation marks around each word), this automatically does the work
IT1 = IT1initial.split()
PT2 = PT2initial.split()
ES3 = ES3initial.split()
CA4 = CA4initial.split()
FR5 = FR5initial.split()


# 4. JOIN THE STRINGS
# Take the lists, join all the strings (words) in a list, and add spaces in between
print("IT: " + (" ".join(IT1)))
print("PT: " + (" ".join(PT2)))
print("ES: " + (" ".join(ES3)))
print("CA: " + (" ".join(CA4)))
print("FR: " + (" ".join(FR5)))

print("")


# 5. JACCARD SIMILARITY OF SENTENCES
# Determine jaccard similarity of different sentences
# Multiply by 100 to move decimal point two places rightward (for example, .98768 becomes 98.768)
IT1_PT2initial = (jaccard_similarity(str(IT1), str(PT2))) * 100
IT1_ES3initial = (jaccard_similarity(str(IT1), str(ES3))) * 100
IT1_CA4initial = (jaccard_similarity(str(IT1), str(CA4))) * 100
IT1_FR5initial = (jaccard_similarity(str(IT1), str(FR5))) * 100

PT2_ES3initial = (jaccard_similarity(str(PT2), str(ES3))) * 100
PT2_CA4initial = (jaccard_similarity(str(PT2), str(CA4))) * 100
PT2_FR5initial = (jaccard_similarity(str(PT2), str(FR5))) * 100

ES3_CA4initial = (jaccard_similarity(str(ES3), str(CA4))) * 100
ES3_FR5initial = (jaccard_similarity(str(ES3), str(FR5))) * 100

CA4_FR5initial = (jaccard_similarity(str(CA4), str(FR5))) * 100


# 6. ROUND JACCARD SIMILARITY RESULT
# Round the jaccard similarity result to two places (for example, 98.768 becomes 98.77)
IT1_PT2 = round(IT1_PT2initial, 2)
IT1_ES3 = round(IT1_ES3initial, 2)
IT1_CA4 = round(IT1_CA4initial, 2)
IT1_FR5 = round(IT1_FR5initial, 2)

PT2_ES3 = round(PT2_ES3initial, 2)
PT2_CA4 = round(PT2_CA4initial, 2)
PT2_FR5 = round(PT2_FR5initial, 2)

ES3_CA4 = round(ES3_CA4initial, 2)
ES3_FR5 = round(ES3_FR5initial, 2)

CA4_FR5 = round(CA4_FR5initial, 2)


# 7. INITIAL COMPARISON LIST
# Initialize a list with the comparison values
complist = [IT1_PT2, IT1_ES3, IT1_CA4, IT1_FR5, PT2_ES3, PT2_CA4, PT2_FR5, ES3_CA4, ES3_FR5, CA4_FR5]


# 8. INITIAL DICTIONARY
# Initialize a dictionary which we can sort from greatest to least later
compdict =	{
  "IT to PT similarity:": complist[0],
  "IT to ES similarity:": complist[1],
  "IT to CA similarity:": complist[2],
  "IT to FR similarity:": complist[3],
  "PT to ES similarity:": complist[4],
  "PT to CA similarity:": complist[5],
  "PT to FR similarity:": complist[6],
  "ES to CA similarity:": complist[7],
  "ES to FR similarity:": complist[8],
  "CA to FR similarity:": complist[9]
}

print("Sorted by most similar to least similar:")


# 9. SORT DICTIONARY
# Sort the items in the dictionary mentioned earlier from greatest to least
complist2 = sorted(compdict.items(), key=lambda x:x[1], reverse = True)

for x, y in complist2:
  print(x, y)

print("")


# 10. MEAN OF COMPARISONS
# Determine the mean of all of the comparisons combined and round the result to two places
finalmean = statistics.mean(complist)
FMround = round(finalmean, 2)
print("The mean score of the comparisons is " + str(FMround) + "%")
print(" ")


# 11. MOST SIMILAR VALUE TO COMPARISONS
# Determine most similar value to the mean score of the comparisons
def myfunc(n):
  return abs(n - finalmean)

complist.sort(key = myfunc)
similarmean = complist[0]
SMround = round(similarmean, 2)


# 12. PRINT MOST SIMILAR VALUE
# Print most similar value
print("The value most similar to the mean of the comparisons is " + str(SMround) + "%")
print(complist)