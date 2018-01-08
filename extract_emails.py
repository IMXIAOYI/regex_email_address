import os,sys,re

#read webpages line by line
def read_input(filename):
	webpage=[]
	with open(filename) as f:
		for line in f:
			webpage.append(line)
	return webpage

#write output
def write_output(filename, res):
	i=0
	length=len(res)
	thefile=open(filename, 'w')
	for item in res:
		if i<length-1:
			thefile.write("%s\n"%item)
			i=i+1
		else: 
			thefile.write("%s"%item)


#extract regular expression and cantonize them 
def get_emails(webpage):
	r_expression=re.compile("[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:((\s)*\.(\s)*|[^a-zA-Z0-9]+dot[^a-zA-Z0-9]+)[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*((\s)*@(\s)*|[^a-z0-9]+at[^a-z0-9]+)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?((\s)*\.(\s)*|[^a-zA-Z0-9]+dot[^a-zA-Z0-9]+))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
	r_at=re.compile("[^a-zA-Z0-9]+at[^a-zA-Z0-9]+")
	r_dot=re.compile("[^a-zA-Z0-9]+dot[^a-zA-Z0-9]+")
	res=[]
	for page in webpage:
		tmp=re.search(r_expression, page)
		if tmp:
			temp=tmp.group()
			at_search=re.search(r_at, temp)
			if at_search:
				temp=temp.replace(at_search.group(),'@')
			dot_search=re.search(r_dot, temp)
			if dot_search:
				temp=temp.replace(dot_search.group(),'.')
			res.append(temp.replace(' ',''))
		else:
			res.append('None')
	return res

if __name__ =='__main__':
	if len(sys.argv)!=3:
		print("please type in python file, input file and output file in order")
	write_output(sys.argv[2], get_emails(read_input(sys.argv[1])))
