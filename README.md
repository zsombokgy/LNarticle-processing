# article-processing
Project to process French newspaper articles.

The goal of this project is to process French newspaper articles downloaded from the data base Lexis Nexis Academic.
Example files are provided in the "Prescribed1" folder.

This project has multiple steps:

1. Date processing:
    
    Newspaper articles have been archived in different ways on Lexis Nexis Academic, which resulted in different date formats. It included French and English date formats, day and month names, DAY-MONTH-YEAR, MONTH-DAY-YEAR format, etc. The first major step of this project is to get rid of all unnecessary metainformation about the article, and to harmonize date formats from all sources. By the end of this step, the article will not have any metainformation about the length, etc. Also, the date format will be harmonized in the following way:
    
    19 avril 2009 dimanche → 19 avril 2009 → 2009 avril 19 → 2009-04-19
    
    'article_dates.py' contains the main execution of this cleaning, while 'article_dates_modules.py' contains the functions used in the main file. Each file is annotated to make it easier to understand what things do. An output file is created as a sample.
    
    Note: make sure to store these python files in the same directory. Additionally, have the folder 'Prescribed1' in the same directory, or don't forget to modify the path to it.

2. Remove duplicates:

    Due to the fact that certain newspapers were digitalized on Lexis Nexis Academic at different times, it not only resulted in different date format (that we resolved in STEP 1), but also in duplicate articles. This was because the same article was digitalized once in the late 1990s, and again in the early 2000s, and again in the mid 2000s. This is an issue that STEP 2 intends to resolve.
    
    In this step, the articles in the list are further cleaned to minimize any remaining differences. After that, they are sorted based on their length, so that the same articles follow each other - it is highly unlikely that two different articles share the same length. After getting sorted by length, we check the similarities between consecutive articles, and only keep the original ones. Finally, these articles are sorted again by publication and date.
    
    'article_duplicates.py' contains the main execution for removing the duplicates, while 'article_duplicates_modules.py' contains the functions used in the main file. Please note that you need to have the variable 'textlist4' from the first step. An output file is created as a sample - in that output, the article is a long string of text, which will be useful in later steps.
    
DISCLAIMER: The article do not contain the original text of the article. I changed them to text from Wikipedia articles. For any remaining information from the article (e.g. journal, publication date, length, etc.), I do not own the rights. All copyrights belong to their respective sources.
