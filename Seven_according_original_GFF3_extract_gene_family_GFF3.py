your_file = open('TAIR10_GFF3_genes.gff') #your original GFF3 txt
ID_file = open('gene_cluster_ID.txt') #your gene id, AT2G28220.1
out_file = open('gene_cluster_tandem_AP.Structure.GFF3.txt', 'w') #out file

for line in ID_file:
	fsy = line.split()
	gene = fsy[0]
	for row in your_file:
		if False == row.startswith('#'):
			rowList = row.strip('\n').split('\t')
			if [''] != rowList:
				if gene in rowList[8]:
					result = row
					out_file.write(result)
	your_file.seek(0,0)

# Created by Huilong Chen.
#The script can be used to do more!
