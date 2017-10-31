taxonID=[]

def get_organized(file):
	file=open(file, 'r')
	for line in file:
		line=line.split()
		taxonID.append(line[0])
	file.close()
	return (taxonID)
get_organized('taxon_list.txt')


check = []
for each in taxonID:
	word = str('"' + each + '" ' )
	check.append(word)

newlist =  ' '.join(check)
print(newlist)