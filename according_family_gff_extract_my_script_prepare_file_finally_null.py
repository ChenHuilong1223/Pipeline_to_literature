chr_file = open('TAIR10_chr_all.fas.chromosome.length.txt') #your chromosome length txt: Si01	42132138
gff_file = open('Ath.gene_cluster_tandem_AP.gff') #your gene_family four column gff file!
out_file = open('Ath.chr.1-5.my.txt','w') #the file needed mapchart!
#i = 0
result1 = ''
for chl in gff_file:
	chl1 = chl.split()
	last_chr = chl1[0]
	break
gff_file.seek(0,0)

for row in chr_file:
	store = row.split()
	number = store[0]
	all_len = str(int(store[1])/1000000)
#	for i in range(9):
#	i = i + 1
#	i_str = "Si" + str(i)
#	file_name = number + ".MAP"
#	out_file = open(file_name, 'w')
	out_file.write('$' + number + "\t" + all_len + "\n")
	out_file.write(result1)
	for line in gff_file:
		fsy1 = line.split()
		chr_name = fsy1[0]
		if chr_name ==  last_chr:
			result = fsy1[1] + "\t" + str(int(fsy1[2])/1000000)
			out_file.write(result + "\n")
			last_chr = chr_name
		else:
#			result = fsy1[1] + "\t" + fsy1[2]
#			out_file.write(result + "\n")
			result1 = fsy1[1] + "\t" + str(int(fsy1[2])/1000000) + "\n"
			last_chr = chr_name
			break
#	out_file.write("segments" + "\n" + "0" + "\t" + all_len + "\t" + "C3" + "\n" + "\n")
	#you can alter last row,such as C3（绿色）
#make by Chen Huilong
#your gene family gff file and chr_file have to be '1,2,3,4,5,6,7,8,9'(order)
#You can start by giving your gene family ID in ascending order using EXCEL, 
#then use previous python script!———according_original_GFF3_extract_gene_family_gff.py
#if your families' gene not on any chromosome, Please delete the chromosome in chr_file!
	
	
	
	
