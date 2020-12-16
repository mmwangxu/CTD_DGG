# -*- coding: utf-8 -*-
import xlrd
import sys

if __name__ == '__main__':

	path1= xlrd.open_workbook(r'GO.xlsx')
	#path2= xlrd.open_workbook(r'F:\Python\GO\Data\Lysosome_CC.xlsx')
	
	doc1 = open('cancer_num.txt','w',encoding='utf-8')
	doc2 = open('_no-cancer_num.txt','w',encoding='utf-8')
	doc = open('lectin_vector.txt','w',encoding='utf-8')
	#doc_result = open('_result.txt','w',encoding='utf-8')
	
	output=sys.stdout
	type = sys.getfilesystemencoding()
	outputfile=open('_result.txt','a',encoding='utf-8')
	sys.stdout=outputfile
	
	print('doc_name：',path1.sheet_names())
	
	
	sheet1 = path1.sheet_by_name('cancer')  
	sheet2 = path1.sheet_by_name('no-cancer')
	
	a = print('doc_name：',sheet1.name, 'rows：',sheet1.nrows, 'columns：',sheet1.ncols)
	b = print('doc_name：',sheet2.name, 'rows：',sheet2.nrows, 'columns：',sheet2.ncols)
	
	DD = []
	for i in range(1,sheet1.nrows):

		rows = sheet1.row_values(i)

		while '' in rows:
			 rows.remove('')

		rerows = rows[2:]
		#print(len(rerows))

		CC = []
		for col in rerows:
			str3 = col.split(':')
			str = str3.pop()
			#print(str,end = ' ')
			print(str,end = ' ',file = doc1)
			CC.append(str)
		#print(len(CC))
		#print(CC)
		#print('*********************')
		#print()
		print(file = doc1)
		DD.append(CC)
	doc1.close()
	#print(DD)
	
	
	for i in range(1,sheet2.nrows):

		rows = sheet2.row_values(i)

		while '' in rows:
			 rows.remove('')

		rerows = rows[2:]
		#print(len(rerows))

		CC = []
		for col in rerows:
			str3 = col.split(':')
			str = str3.pop()
			#print(str,end = ' ')
			print(str,end = ' ',file = doc2)
			CC.append(str)
		#print(len(CC))
		#print(CC)
		#print('*********************')
		#print()
		print(file = doc2)
		DD.append(CC)
	doc2.close()
	
	
	print('#######################')
	EE = [a for item in DD for a in item]
	#print(EE)
	print('GO_number:',len(EE))
	FF = []
	for j in EE:
		if not j in FF:
			FF.append(j)
	#print(FF)
	print(len(FF))
	print(len(DD))
	for k in range(1,len(DD)+1):
		#print(k)
		print(k,end = ' ',file = doc)
		GG = []
		for h in FF:
			if h in DD[k-1]:
				GG.append(1)
				print(1,end = ' ',file = doc)
			else:
				GG.append(0)
				print(0,end = ' ',file = doc)
		#print(GG)
		print(file = doc)
	doc.close()