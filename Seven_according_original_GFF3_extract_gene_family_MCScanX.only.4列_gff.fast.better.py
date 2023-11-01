import pandas as pd

IdFileDf = pd.read_csv('gene_cluster_ID.txt',encoding='utf-8',header=None,sep='\n',index_col=None) #your gene id, AT2G28220.1
gff3File = open('TAIR10_GFF3_genes.gff',encoding='utf-8') #your gff file
outFile = open('Ath.gene_cluster_tandem_AP.gff', 'w',encoding='utf-8') #out file

IdList = IdFileDf[0].tolist()
print(len(IdList))
i = 0
for row in gff3File:
	if False == row.startswith('#'):
		rowList = row.split('\t')
		geneName = rowList[8].split(';')[0].replace('ID=','')
		# print(geneName)
		if 'mRNA' in row and geneName in IdList:
			print(geneName)
			result = rowList[0]+'\t'+geneName+'\t'+rowList[3]+'\t'+rowList[4]+'\n'
			outFile.write(result)
			IdList.remove(geneName)
			i += 1
print(i)

#Created by Huilong Chen.
#The script can be used to do more!		
