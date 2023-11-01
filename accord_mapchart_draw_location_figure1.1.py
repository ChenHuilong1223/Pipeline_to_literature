import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'Times New Roman'

df = pd.read_csv('Ath.chr.1-5.my.txt',sep='\t',encoding='utf-8',header=None)

chr_len = df[df[0].str.startswith('$')]
chro = chr_len[0].map(lambda x: x.replace('$','')).values.tolist()
#chros = list(range(1,len(chro)+1,1))
chros = []
i = 0
j = 0
while j<len(chro):
	i += 1 #这个1.5好像可以调控两条染色体之间的间隔，但又不是很好以后再说吧，就暂时不增加位置了
	chros.append(i)
	j += 1
#chros = [i+1.5 for i in range(0,len(chro))]
#print(chros)
lens = chr_len[1].values.tolist()
#print(chr_len)
#print(chro)
#print(lens)
#print(df)
fig,ax = plt.subplots(figsize=(14,7))
ax.invert_yaxis()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.xaxis.set_visible(False)
ax.set_ylim(max(lens),0)
ax.text(0.5,max(lens),'Mb',fontsize=13,va='center',ha='right')
ax.bar(chros,lens,width=0.1,color='blue')

num = 0
for fsy in df.values:
	if fsy[0].startswith('$'):
		chrom = fsy[0].replace('$','')
		num += 1 #这个1.5好像可以调控两条染色体之间的间隔，但又不是很好以后再说吧，就暂时不增加位置了
		lastpos = -3 #感觉这个值应该是第42行里的等差值的两倍，但其实中心距离差值就是1.5，因为两个基因所以乘以2
		ax.text(num,0,chrom,fontsize=16,va='bottom',ha='center')
	else:
		if fsy[1]-lastpos > 3:
			ax.annotate(fsy[0],xy=(num+0.035,fsy[1]),xycoords='data',
						xytext=(num+0.2,fsy[1]),textcoords='data',fontsize=10,color='k',
#						bbox=dict(boxstyle='round4',fc='w'),
						arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=0.0',relpos=(0,0.5),color='k'),
						va='center',ha='left')
#			ax.annotate('%.2f' % fsy[1],xy=(num-0.035,fsy[1]),xycoords='data',
#						xytext=(num-0.2,fsy[1]),textcoords='data',fontsize=9,color='k',
#						arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=0.0',relpos=(1,0.5),color='k'),
#						va='center',ha='right')			
			lastexty = fsy[1]		
			lastpos = fsy[1]
		else:
			y0 = lastexty + 1.5
			ax.annotate(fsy[0],xy=(num+0.035,fsy[1]),xycoords='data',
						xytext=(num+0.2,y0),textcoords='data',fontsize=10,color='k',
#						bbox=dict(boxstyle='round4',fc='w'),
						arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=0.0',relpos=(0,0.5),color='k'),
						va='center',ha='left')
#			ax.annotate('%.2f' % fsy[1],xy=(num-0.035,fsy[1]),xycoords='data',
#						xytext=(num-0.2,y0),textcoords='data',fontsize=9,color='k',
#						arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=0.0',relpos=(1,0.5),color='k'),
#						va='center',ha='right')				
			lastexty = y0			
			lastpos = fsy[1]

fig.savefig('gene_located.png',dpi=500,format='png')
# with PdfPages('gene_located.pdf') as pdf:
#     ax.plot([])
#     pdf.savefig()
fig.savefig('gene_located.pdf',format='pdf')
fig.savefig('gene_located.svg',format='svg')
#plt.show()
