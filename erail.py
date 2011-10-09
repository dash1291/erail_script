import urllib2,re
def find_trains(stn_from,stn_to):
	request=urllib2.urlopen("http://erail.in/rail/getTrains.aspx?Station_From="+stn_from+"&Station_To="+stn_to+"&DataSource=0&Language=0")
	response=request.read()
	re_train_item=re.compile(r'\^\d+\~[A-Za-z0-9 ]+')
	re_train_name=re.compile(r'~[A-Za-z0-9 ]+')
	re_train_number=re.compile(r'\^\d+')
	trains={}
	train_items=re_train_item.findall(response)
	for train_item in train_items:
		train_number=re_train_number.search(train_item).group()[1:]
		train_name=re_train_name.search(train_item).group()[1:]
		trains[train_number]=train_name
	return trains
a=find_trains("NDLS","GWL")
print a[1]


