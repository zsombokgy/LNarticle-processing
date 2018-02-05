# article-processing
Project to process French newspaper articles.

The goal of this project is to process French newspaper articles downloaded from the data base Lexis Nexis Academic.
Example files are provided in the "Prescribed1" folder.

This project has multiple steps:

1. Date processing:
    
    Newspaper articles have been archived in different ways on Lexis Nexis Academic, which resulted in different date formats. It included French and English date formats, day and month names, DAY-MONTH-YEAR, MONTH-DAY-YEAR format, etc. The first major step of this project is to get rid of all unnecessary metainformation about the article, and to harmonize date formats from all sources. By the end of this step, the article will not have any metainformation about the length, etc. Also, the date format will be harmonized in the following way:
    
    19 avril 2009 dimanche → 19 avril 2009 → 2009 avril 19 → 2009-04-19
    
    'article_process_dates.py' contains the main execution of this cleaning, while 'article_modules.py' contains the functions used in the main file. Note: make sure to store these python files in the same directory. Additionally, have the folder 'Prescribed1' in the same directory, or don't forget to modify the path to it.


    
DISCLAIMER: The article do not contain the original text of the article. I changed them to text from Wikipedia articles. For any remaining information from the article (e.g. journal, publication date, length, etc.), I do not own the rights. All copyrights belong to their respective sources.
