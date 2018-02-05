#Import re (Regular Expressions), os (Operating system), glob
import re, os, glob
from article_dates_modules import split_list, precleaning, year_month_day, month_number

#Find all TXT file in the PRESCRIBED1 directory
os.chdir("Prescribed1")
files = glob.glob("*.txt")

#Read in all text files
text2 = []
for name in files:
    with open(name, encoding = "utf8") as f:
        text = f.read()
        text2.append(text)

#Split text files into a list
textlist = split_list(text2)
#Clean text from unnecessary information
textlist2 = precleaning(textlist)
#Reorder DAY MONTH YEAR dates into YEAR MONTH DAY
textlist3 = year_month_day(textlist2)
#Replace name of the month by number
textlist4 = month_number(textlist3)
#Correct some of the date formats

#Print output into a file
os.chdir('..') #Do not use 'Prescribed1'
article_dates_output = open("article_dates_output.txt", "w+")
print("\n".join(textlist4), file = article_dates_output)
article_dates_output.close()
