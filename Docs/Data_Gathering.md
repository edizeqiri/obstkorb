# Data Gathering

For this project 2 types of data were gathered. Malware and Scicore binaries.

The purpose was to get a better view of how the fuzzy hashers compare the files.
Since they are created for Malware purposes only it could be that they perform worse for different types of binaries.

## Malware

To get a statistical relevant database of classified malware sampels I used VX-Underground to gather the malware.

At first the idea was to webscrape every field with a selenium framework. But after analysing the webpage, I noticed that
the path to all the binaries is embedded in the index.html. Therefore, I only had to play combine the relevant path of each binary and do a get request.

The source code can be found in Data_Gathering/cleaner.py. web_scraper.py was used inititally to learn more about the
structure of the website.

## Scicore

The most relevant binaries seem to be /scicore/apps/soft. These binaries, which can be used by every user, are the easiest way
to classify slurm jobs and their purpose.

Since the folder is bigger than 300GB with more than 1000 families, just secure copying is not efficient. Thus, I first grepped all the bin* folders.
I saved the result to the Data_Gathering/directories.txt file. With the list I now can find all the binaries which relate to the folder and are relevant for us.
For example, in the folder nodejs I am only interested in the binary node and not npm or others. Therefore, the challenge is to find the longest matching substring.
The python script lon.py was created for this purpose. It finds all the relevant binaries and generates another list called sci_bin_list.txt.

This list allows me to generate an archive with the correct folder/file architecture needed by Obstkorb. The python script for this is sci_cp_bins.py

