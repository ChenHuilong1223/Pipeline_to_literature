# Pipleline to literature

#### A Pipeline for Obtaining Relevant Literature Based on Given Keywords

It's a pipeline to help researchers accelerate literature searches and information acquisition

Let's start following the steps!

## Step 1

#### Syntax for obtaining query syntaxes for databases such as PubMed based on keywords

1. ##### Common approach

Take PubMed as an example.

Take the subject keywords of our current study (e.g. **Mycotoxin, enzyme, degrade**, degradation, etc.) as an example.

**Website:** https://pubmed.ncbi.nlm.nih.gov/advanced/

###### Search based on search keyword statements

![1]([E:\typora\chl_export_folder\NLP-pipeline\1.png](https://github.com/ChenHuilong1223/Pipeline_to_literature/blob/main/images/1.png))

**Note:** When you use a literature database to search for relevant literature resources, we recommend that you optimize your keywords. For example, if your research area of interest is a physician topic, you should perform keyword validation at the MeSH URL (http://www.nlm.nih.gov/mesh/). This is to ensure that the most accurate research vocabulary is used. This maximizes the chance of ensuring that the literature resources searched in the database are the most accurate and relevant.

###### Download all retrieved literature information

![2](E:\typora\chl_export_folder\NLP-pipeline\2.png)



For Web of Science:

Website: https://www.webofscience.com/wos/woscc/advanced-search

![3](E:\typora\chl_export_folder\NLP-pipeline\3.png)

![4](E:\typora\chl_export_folder\NLP-pipeline\4.png)

![5](E:\typora\chl_export_folder\NLP-pipeline\5.png)

You can also supplement the relevant literature in other databases such as Google Scholar, Science Direct, etc.

2. ##### Common approach

To minimize manual operations, here we have created a homemade Python script that automatically generates all possible lexical variations and PubMed and Web of Science query syntaxes and corresponding download links based on keywords provided by the user.

**Python script name:** generate_query_statements_and_links_to_literature_database_searches_based_on_keywords.py

Required Modules:

nltk, inflect, argparse, itertools

If your machine does not have the corresponding module, use **pip install module** to install it successfully.

**Usage:**

Enter the following command in the terminal to see help on using the program:

```shell
python generate_query_statements_and_links_to_literature_database_searches_based_on_keywords.py -h
```

![image-20240201144701909](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201144701909.png)

All parameters and descriptions are listed below:

| Parameters | Descriptions                                                 |
| ---------- | ------------------------------------------------------------ |
| -m         | When running the script for the first time, use -m init to download the dictionary library first. Once downloaded, use -m run for subsequent run parameters. |
| -i         | Setting the path to a file containing only keywords.         |
| -o         | Setting the output file path.                                |

**Enter the file format:**

keyword 1

keyword 2

keyword 3

...

As shown in the figure below:

![image-20240201150428130](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201150428130.png)

**Practical training:**

```shell
python generate_query_statements_and_links_to_literature_database_searches_based_on_keywords.py -m run -i keywords.txt -o my_result.txt
```

Outputs the contents of the file:

![image-20240201150847147](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201150847147.png)

![image-20240201151148043](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201151148043.png)

![image-20240201151409344](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201151409344.png)

After that, according to the results given by this program, go directly from PubMed or Web of Science to download the results of searching literature information. You can refer to the next steps in the section **1. common approach**.

## Step 2

#### Consolidation of literature information

Literature collected from different databases was combined into one file through MS Excel. We keep only the Title and DOI number and save it as an xlsx file. Example:

![6](E:\typora\chl_export_folder\NLP-pipeline\6.png)

The file was then processed to remove duplicates using the Python script.

**Python script name:** 

remove_duplicates.py

Required Modules:

pandas, argparse

If your machine does not have the corresponding module, use **pip install module** to install it successfully. 

**Usage:**

Enter the following command in the terminal to see help on using the program:

```shell
python remove_duplicates.py -h
```

![image-20240201191846460](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201191846460.png)

All parameters and descriptions are listed below:

| Parameters | Descriptions                                                 |
| ---------- | ------------------------------------------------------------ |
| -i         | Setting the path to MS Excel files ending in .xlsx extension |
| -o         | Setting the output file path.                                |

**Practical training:**

```shell
python remove_duplicates.py -i all_database_literatures_data.xlsx -o all_database_literatures_data_single.txt
```

Outputs the contents of the file:

![image-20240201192413535](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201192413535.png)

## Step 3

#### Download literatures

Based on the entirety of the relevant literature obtained earlier, a pdf of each piece of literature was downloaded.

**Note:** In order to get all the above literature as fast as possible, we suggest that a one-time batch download can be realized by tools such as **EndNote**, **crawler**, **scihub2pdf**, and so on. Please note that at all times, **please respect the copyrights of the authors and publishers of the literature. That is, the acquisition of the target literature is carried out through legal channels.**

Here, we provide a crawler script that can batch download pdf format literature. Just for reference.

**Python script name:** 

batch_download_literatures_pdf_alpha_test.py

Required Modules:

pandas, selenium, time, os, random, argparse

If your machine does not have the corresponding module, use **pip install module** to install it successfully. 

**Usage:**

Enter the following command in the terminal to see help on using the program:

```shell
python batch_download_literatures_pdf_alpha_test.py -h
```

![image-20240201193246426](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201193246426.png)

**Note:** This script is for test use by interested parties only, and in order to comply with the publisher's copyright, please download it from the official link of the literature publisher, or purchase the target literature you need.

## Step 4

#### Convert pdf documents to text files

After downloading all the documents (pdf), use the Python script for batch processing to convert all the documents into text files.

**Python script name:** 

batch_pdf_file_to_text_file.py

Required Modules:

os, argparse

If your machine does not have the corresponding module, use **pip install module** to install it successfully. 

**Usage:**

Enter the following command in the terminal to see help on using the program:

```shell
python batch_pdf_file_to_text_file.py -h
```

![image-20240201194134075](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201194134075.png)

All parameters and descriptions are listed below:

| Parameters | Descriptions                                                 |
| ---------- | ------------------------------------------------------------ |
| -m         | The script provides four kinds of pdf files into text files, respectively, numbered 1, 2, 3, 4, the user can set up according to their own preferences. A run, only one of the methods can be set. The purpose of such a design is that when some of the pdf documents can not be converted into text files, you can put these documents into a separate directory, try another method of conversion. |
| -i         | Setting the path to the folder that includes only pdf-formatted literatures. |
| -o         | Setting the path of output folder, all the text files which are converted successfully will be stored in this directory. |

**Practical training:**

```shell
python batch_pdf_file_to_text_file.py -m 4 -i literatures_pdf -o literatures_text
```

View a text-formatted document from the leteratures_text folder as follows:

![image-20240201195232993](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240201195232993.png)

**Note:** The file name of the document is logged in the terminal for failed conversions. Convenient for users to follow up.

#### Access to large language modeling tools

After that, following the process described in our article, the research question is prepared manually and then the text file is copied and pasted into the input box of a big language model such as **ChatGPT**. The goal of capturing information from the literature by big language models instead of manually can be realized.

Finally, I sincerely hope that this pipeline can accelerate your research process and wish the best of luck in research.

