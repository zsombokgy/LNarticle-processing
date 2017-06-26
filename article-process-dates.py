#Import re (Regular Expressions), os (Operating system), glob
import re, os, glob

#Change current directory
os.chdir("ENTER PATH HERE")

#Set split pattern. The output will not contain this string
split_pattern = r"\W*[0-9]*\W*of\W*[0-9]*\W*DOCUMENTS?\W*"

#Find all TXT file in the directory
files = glob.glob("*.txt")

#Read in all text files, and then split them on the pattern.
text2 = []
for name in files:
    with open(name, encoding = "utf8") as f:
        text = f.read()
        text2.append(text)

textlist0 = []
for element in text2:
    splittext = re.split(split_pattern, element)
    textlist0.append(splittext)

#Delete the very first, useless element of each list
for element in textlist0:
    del element[0]

#Merge all list together
textlist = sum(textlist0, [])

preprocessing = []
for element in textlist:
    extranewlines = re.sub(r"\n\n?\W*", r"\n", element)
    extraspaces = re.sub(r"  ", r" ", extranewlines)
    copyright1 = re.sub(r"(\n?Copyright.*)(\n?)", r"", extraspaces)
    copyright2 = re.sub(r"(\n?Copyright.*All rights reserved)(\n?)", r"", copyright1)
    tousdroits = re.sub(r"(\n?Tous droits réservés)(\n?)", r"\2", copyright2)
    encart = re.sub(r"(ENCART:\W|HEADLINE:\W)", r"", tousdroits)
    metainfo = re.sub(r"[A-Z-]+:.*\n?", r"", encart)
    startingday = re.sub(r"(^.*\n)([Ll]undi|[Mm]ardi|[Mm]ercredi|[Jj]eudi|[Vv]endredi|[Ss]amedi|[Dd]imanche)(\W*)(\d)", r"\1\4", metainfo)
    endingday = re.sub(r"(\W*)([Ll]undi|[Mm]ardi|[Mm]ercredi|[Jj]eudi|[Vv]endredi|[Ss]amedi|[Dd]imanche)(\n)", r"\3", startingday)
    subJDN = re.sub(r"Journal\W?du\W?Net,\W?JDN\W?Solutions", "Journal du Net", endingday)
    preprocessing.append(subJDN)

#Reorder DAY MONTH YEAR dates into YEAR MONTH DAY
subdates = []
for element in preprocessing:
    subdate1 = re.sub(r"(\n)(\d{,2})\W*([JjFfMmAaSsOoNnDd]\w{0,8})\W*(\d{4})", r"\1\4 \3 \2", element)
    subdate2 = re.sub(r"(\n)([JjFfMmAaSsOoNnDd]\w{0,8})\W*(\d{,2}),?\W*(\d{4})", r"\1\4 \2 \3", subdate1)
    subdates.append(subdate2)

#Finalize YEAR MONTH DAY line with new formatting
subdates2 = []
for element in subdates:
    if re.search(r"\n\d{4}\W*[Jj]an.i?.ry?\W*\d{1,2}\n", element):
        januaryelem = re.sub(r"(\d{4})\W*([Jj]an.i?.ry?)\W*(\d{1,2})", r"\1-01-\3", element)
        subdates2.append(januaryelem)
    elif re.search(r"\n\d{4}\W*[Ff]..r..ry?\W*\d{1,2}\n", element):
        februaryelem = re.sub(r"(\d{4})\W*([Ff]..r..ry?)\W*(\d{1,2})", r"\1-02-\3", element)
        subdates2.append(februaryelem)
    elif re.search(r"\n\d{4}\W*[Mm]arc?.\W*\d{1,2}\n", element):
        marchelem = re.sub(r"(\d{4})\W*([Mm]arc?.)\W*(\d{1,2})", r"\1-03-\3", element)
        subdates2.append(marchelem)
    elif re.search(r"\n\d{4}\W*[Aa].ril\W*\d{1,2}\n", element):
        aprilelem = re.sub(r"(\d{4})\W*([Aa].ril)\W*(\d{1,2})", r"\1-04-\3", element)
        subdates2.append(aprilelem)
    elif re.search(r"\n\d{4}\W*[Mm]a.\W*\d{1,2}\n", element):
        mayelem = re.sub(r"(\d{4})\W*([Mm]a.)\W*(\d{1,2})", r"\1-05-\3", element)
        subdates2.append(mayelem)
    elif re.search(r"\n\d{4}\W*[Jj]ui?ne?\W*\d{1,2}\n", element):
        juneelem = re.sub(r"(\d{4})\W*([Jj]une|[Jj]uin)\W*(\d{1,2})", r"\1-06-\3", element)
        subdates2.append(juneelem)
    elif re.search(r"\n\d{4}\W*[Jj]ui?ll?[yet]{1,2}\W*\d{1,2}\n", element):
        julyelem = re.sub(r"(\d{4})\W*([Jj]ui?ll?[yet]{1,2})\W*(\d{1,2})", r"\1-07-\3", element)
        subdates2.append(julyelem)
    elif re.search(r"\n\d{4}\W*[Aa]o?.g?u?s?t\W*\d{1,2}\n", element):
        augustelem = re.sub(r"(\d{4})\W*([Aa]o?.g?u?s?t)\W*(\d{1,2})", r"\1-08-\3", element)
        subdates2.append(augustelem)
    elif re.search(r"\n\d{4}\W*[Ss].ptemb[er]{2}\W*\d{1,2}\n", element):
        septemberelem = re.sub(r"(\d{4})\W*([Ss].ptemb[er]{2})\W*(\d{1,2})", r"\1-09-\3", element)
        subdates2.append(septemberelem)
    elif re.search(r"\n\d{4}\W*[Oo]ctob[er]{2}\W*\d{1,2}\n", element):
        octoberelem = re.sub(r"(\d{4})\W*([Oo]ctob[er]{2})\W*(\d{1,2})", r"\1-10-\3", element)
        subdates2.append(octoberelem)
    elif re.search(r"\n\d{4}\W*[Nn]ovemb[er]{2}\W*\d{1,2}\n", element):
        novemberelem = re.sub(r"(\d{4})\W*([Nn]ovemb[er]{2})\W*(\d{1,2})", r"\1-11-\3", element)
        subdates2.append(novemberelem)
    elif re.search(r"\n\d{4}\W*[Dd].cemb[er]{2}\W*\d{1,2}\n", element):
        decemberelem = re.sub(r"(\d{4})\W*([Dd].cemb[er]{2})\W*(\d{1,2})", r"\1-12-\3", element)
        subdates2.append(decemberelem)

#Correct some of the date formats
subdates3 = []
for element in subdates2:
    subdate5 = re.sub(r"(\d{4})-(\d{2})-(\d{1,1})", r"\1-\2-0\3", element)
    subdate6 = re.sub(r"(\d{4})-(\d{2})-0(\d{2})", r"\1-\2-\3", subdate5)
    subdates3.append(subdate6)