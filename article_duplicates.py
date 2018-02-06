#Import functions from the 'article_duplicates_modules.py'
import os
from article_duplicates_modules import minimize_difference, deduplicator

textlist5 = minimize_difference(textlist4)
textlist6 = deduplicator(textlist5)

#Print output into a file
#Since new line characters are cleaned from the articles, they are one long string of text
#This format will be useful in a later step
os.chdir('..') #Do not use 'Prescribed1'
article_dates_output = open("article_duplicates_output.txt", "w+")
print("\n\n".join(textlist6), file = article_dates_output)
article_dates_output.close()