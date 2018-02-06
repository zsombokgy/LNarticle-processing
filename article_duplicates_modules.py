#Import re (Regular Expressions)
import re, difflib

#Processing texts to minimize differences in whitespace, extra character, etc.
def minimize_difference(textlist):
    minimizedifference= []
    for element in textlist:
        semicolonreplace = re.sub(";", ",", element)
        firstsemicolon = re.sub(r"^(.*)\n(.*)\n", r"\1;\2;", semicolonreplace)
        spaceafterpunc = re.sub(r"(\)|\\)", r"\1 ", firstsemicolon)
        deletemark = re.sub(r"\'", r"'", spaceafterpunc)
        deletespaces = re.sub(r"\s+", r" ", deletemark)
        minimizedifference.append(deletespaces)
    return minimizedifference

def deduplicator(textlist):
    # Sort articles based on their length
    # Since duplicates have (almost always) the same length, they will be sorted after each other
    textlist = sorted(textlist, key=len)
    # Since difflib compares consecutive texts, the first text will always be discarded.
    # That is why an EMPTY TEXT is inserted there and at the end of the list
    textlist.insert(0, "Empty text")
    textlist.append(str("Empty text"))
    duplicates = [] #Store duplicates in one list
    originals = [] #Store originals in the other list
    #Compare the FIRST and the SECOND element of a sequence:
    for first, second in zip(textlist, textlist[1:]):
        sequence = difflib.SequenceMatcher(None, first, second)
        similarity = sequence.ratio() * 100 #Multiply similarity ratio by 100 to see it as a percentage
        #If the similarity is less than 50%, they are treated a
        if similarity < 50:
            originals.append(second)
        else:
            duplicates.append(first)
    del (originals[-1]) #Delete the last text, which is EMPTY TEXT
    #Sort articles based on their publications + dates
    originals = sorted(originals)
    return originals