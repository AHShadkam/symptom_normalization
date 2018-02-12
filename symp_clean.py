def to_str_udf(mystr):
	""" convert the input to string, works on float and bad characters, useful specially for Excel file inputs """
	try:
		mystr_converted = str(mystr)
	except:
		mystr = ''.join([x for x in mystr if ord(x) < 128])
		#mystr = mystr.encode('utf-8')
		mystr_converted = str(mystr)
	return mystr_converted


def clean_symp(line):
	""" use to_str_udf function to convert input to str before using this function""" 
	import re
	Cleaned_line = line.strip()
	Cleaned_line = Cleaned_line.upper()
	Cleaned_line = re.sub('^(DCS|NDCS|CWNT)','',Cleaned_line)
	Cleaned_line = Cleaned_line.replace('/',' ')
	Cleaned_line = Cleaned_line.replace('\\',' ')
	
    
	Cleaned_line = re.sub(r'NDCS','',Cleaned_line)
	Cleaned_line = re.sub(r'CWNT','',Cleaned_line)
	Cleaned_line = re.sub(r'CNWT','',Cleaned_line)

	Cleaned_line = re.sub('\s+',' ',Cleaned_line)   # convert all multi whitespaces to single whitespace
	Cleaned_line = re.sub(r'(DED|APV) \$(\d+)[.](\d+)',' ',Cleaned_line)
	Cleaned_line = re.sub('\s+',' ',Cleaned_line)
	Cleaned_line = re.sub(r'SO..?(\d+)',' ',Cleaned_line)
	Cleaned_line = re.sub('\s+',' ',Cleaned_line)
    
	# last modifications
	Cleaned_line = re.sub(r'\b(APV|DED)\b',' ',Cleaned_line)  # remove "APV" or "DED", not from a word
	Cleaned_line = re.sub('\s+',' ',Cleaned_line)
	regex1 = re.compile('^[^A-Z0-9]+')   # remove initial non-alphanumeric
	Cleaned_line = regex1.sub('',Cleaned_line) 
	regex2 = re.compile('[^A-Z0-9]+$')   # remove trailing non-alphanumeric
	Cleaned_line = regex2.sub('',Cleaned_line)
	Cleaned_line = Cleaned_line.strip()

	# Travis suggestions
	Cleaned_line = re.sub('[\']','',Cleaned_line) # remove apostrophe
	Cleaned_line = re.sub('[^\w\-&]',' ',Cleaned_line) # remove special chars except '-' '&'
	Cleaned_line = re.sub('(\d{3,30})',' ',Cleaned_line) # remove numbers with 3+ digits
	Cleaned_line = re.sub('\s+',' ',Cleaned_line)
	Cleaned_line = Cleaned_line.strip()

	return Cleaned_line