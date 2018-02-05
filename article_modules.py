#Import re (Regular Expressions)
import re

#Defin splitting function that creates a list of articles
def split_list(text):
    split_pattern = r"\W*[0-9]*\W*of\W*[0-9]*\W*DOCUMENTS?\W*" #Split articles based on the recurring sentence
    textlist0 = []
    for element in text:
        splittext = re.split(split_pattern, element)
        textlist0.append(splittext)
    #Delete the first, unnecessary element in each list:
    for element in textlist0:
        del element[0]
    #Merge all list into one
    textlist = sum(textlist0, [])
    return textlist

#Define cleaning function that gets rid of some less important text from the article
#The function takes ONE argument, which is a list of articles
def precleaning(textlist):
    preprocessing = []
    for element in textlist:
        extranewlines = re.sub(r"\n\n?\W*", r"\n", element) #Deletes extra new lines
        extraspaces = re.sub(r"  ", r" ", extranewlines) #Deletes weirdly formatted extra spaces
        copyright1 = re.sub(r"(\n?Copyright.*)(\n?)", r"", extraspaces) #Deletes one format of the Copyright info
        copyright2 = re.sub(r"(\n?Copyright.*All rights reserved)(\n?)", r"", copyright1) #Deletes another Copyright format
        tousdroits = re.sub(r"(\n?Tous droits réservés)(\n?)", r"\2", copyright2) #Deletes copyright in French
        encart = re.sub(r"(ENCART:\W|HEADLINE:\W)", r"", tousdroits) #Deletes ENCART info from text
        metainfo = re.sub(r"[A-Z-]+:.*\n?", r"", encart) #Deletes additional CAPITAL LETTER metainfo from text
        #Deletes day of the week info from the beginning of the date format:
        startingday = re.sub(r"(^.*\n)([Ll]undi|[Mm]ardi|[Mm]ercredi|[Jj]eudi|[Vv]endredi|[Ss]amedi|[Dd]imanche)(\W*)(\d)", r"\1\4", metainfo)
        #Deletes day of the week info from the end of the date format:
        endingday = re.sub(r"(\W*)([Ll]undi|[Mm]ardi|[Mm]ercredi|[Jj]eudi|[Vv]endredi|[Ss]amedi|[Dd]imanche)(\n)", r"\3", startingday)
        #Normalizes "Journal du Net" naming format
        subJDN = re.sub(r"Journal\W?du\W?Net,\W?JDN\W?Solutions", "Journal du Net", endingday)
        preprocessing.append(subJDN)
    return(preprocessing)

#Reorder DAY MONTH YEAR dates into YEAR MONTH DAY
def year_month_day(textlist):
    yearmonthdaylist = []
    for element in textlist:
        subdate1 = re.sub(r"(\n)(\d{,2})\W*([JjFfMmAaSsOoNnDd]\w{0,8})\W*(\d{4})", r"\1\4 \3 \2", element)
        subdate2 = re.sub(r"(\n)([JjFfMmAaSsOoNnDd]\w{0,8})\W*(\d{,2}),?\W*(\d{4})", r"\1\4 \2 \3", subdate1)
        yearmonthdaylist.append(subdate2)
    return yearmonthdaylist

#Use number instead of the name of the month in the YEAR MONTH DAY format
def month_number(textlist):
    monthnumber = []
    #Replace JANUARY/JANVIER with 01, etc.
    for element in textlist:
        if re.search(r"\n\d{4}\W*[Jj]an.i?.ry?\W*\d{1,2}\n", element):
            januaryelem = re.sub(r"(\d{4})\W*([Jj]an.i?.ry?)\W*(\d{1,2})", r"\1-01-\3", element)
            monthnumber.append(januaryelem)
        elif re.search(r"\n\d{4}\W*[Ff]..r..ry?\W*\d{1,2}\n", element):
            februaryelem = re.sub(r"(\d{4})\W*([Ff]..r..ry?)\W*(\d{1,2})", r"\1-02-\3", element)
            monthnumber.append(februaryelem)
        elif re.search(r"\n\d{4}\W*[Mm]arc?.\W*\d{1,2}\n", element):
            marchelem = re.sub(r"(\d{4})\W*([Mm]arc?.)\W*(\d{1,2})", r"\1-03-\3", element)
            monthnumber.append(marchelem)
        elif re.search(r"\n\d{4}\W*[Aa].ril\W*\d{1,2}\n", element):
            aprilelem = re.sub(r"(\d{4})\W*([Aa].ril)\W*(\d{1,2})", r"\1-04-\3", element)
            monthnumber.append(aprilelem)
        elif re.search(r"\n\d{4}\W*[Mm]a.\W*\d{1,2}\n", element):
            mayelem = re.sub(r"(\d{4})\W*([Mm]a.)\W*(\d{1,2})", r"\1-05-\3", element)
            monthnumber.append(mayelem)
        elif re.search(r"\n\d{4}\W*[Jj]ui?ne?\W*\d{1,2}\n", element):
            juneelem = re.sub(r"(\d{4})\W*([Jj]une|[Jj]uin)\W*(\d{1,2})", r"\1-06-\3", element)
            monthnumber.append(juneelem)
        elif re.search(r"\n\d{4}\W*[Jj]ui?ll?[yet]{1,2}\W*\d{1,2}\n", element):
            julyelem = re.sub(r"(\d{4})\W*([Jj]ui?ll?[yet]{1,2})\W*(\d{1,2})", r"\1-07-\3", element)
            monthnumber.append(julyelem)
        elif re.search(r"\n\d{4}\W*[Aa]o?.g?u?s?t\W*\d{1,2}\n", element):
            augustelem = re.sub(r"(\d{4})\W*([Aa]o?.g?u?s?t)\W*(\d{1,2})", r"\1-08-\3", element)
            monthnumber.append(augustelem)
        elif re.search(r"\n\d{4}\W*[Ss].ptemb[er]{2}\W*\d{1,2}\n", element):
            septemberelem = re.sub(r"(\d{4})\W*([Ss].ptemb[er]{2})\W*(\d{1,2})", r"\1-09-\3", element)
            monthnumber.append(septemberelem)
        elif re.search(r"\n\d{4}\W*[Oo]ctob[er]{2}\W*\d{1,2}\n", element):
            octoberelem = re.sub(r"(\d{4})\W*([Oo]ctob[er]{2})\W*(\d{1,2})", r"\1-10-\3", element)
            monthnumber.append(octoberelem)
        elif re.search(r"\n\d{4}\W*[Nn]ovemb[er]{2}\W*\d{1,2}\n", element):
            novemberelem = re.sub(r"(\d{4})\W*([Nn]ovemb[er]{2})\W*(\d{1,2})", r"\1-11-\3", element)
            monthnumber.append(novemberelem)
        elif re.search(r"\n\d{4}\W*[Dd].cemb[er]{2}\W*\d{1,2}\n", element):
            decemberelem = re.sub(r"(\d{4})\W*([Dd].cemb[er]{2})\W*(\d{1,2})", r"\1-12-\3", element)
            monthnumber.append(decemberelem)
    #For some reason, certain DAY numbers will only have 1 digit. We need to correct that issue:
    corrected_monthnumber = []
    for element in monthnumber:
        correctedmonthnumber1 = re.sub(r"(\d{4})-(\d{2})-(\d{1,1})", r"\1-\2-0\3", element)
        correctedmonthnumber2 = re.sub(r"(\d{4})-(\d{2})-0(\d{2})", r"\1-\2-\3", correctedmonthnumber1)
        corrected_monthnumber.append(correctedmonthnumber2)
    return corrected_monthnumber
