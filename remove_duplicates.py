import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Remove duplicate literature')
parser.add_argument('-i', '--inputFilePath', metavar='targeExcelFile', required=True, help='Input the path to an excel file with a .xlsx extension')
parser.add_argument('-o', '--outputFilePath', metavar='outputFile', required=True, help='Output file path')
args = parser.parse_args()

file_path = args.inputFilePath

df = pd.read_excel(file_path)

df = df.dropna(subset=['DOI'])

df = df.drop_duplicates(subset=['DOI'])

output_file = args.outputFilePath

df.to_csv(output_file, index=False, sep='\t', encoding='utf-8')

# Made by Huilong Chen.

