import urllib2,urllib,re,xml.dom.minidom,zlib
from BeautifulSoup import BeautifulSoup
bs=BeautifulSoup
DOM=xml.dom.minidom
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

def find_availablity(args):
	post_data={'lccp_day':args['day'],'lccp_month':args['month'],'lccp_year':args['year'],'lccp_class1':args['class'],'lccp_quota':args['quota'],'lccp_trndtl':args['train_n']+args['stn_from']+ " "+args['stn_to'],
	'lccp_classopt':'ZZ',
	'lccp_class2':'ZZ',
	'lccp_class3':'ZZ',
	'lccp_class4':'ZZ',
	'lccp_class5':'ZZ',
	'lccp_class6':'ZZ',
	'lccp_class7':'ZZ',
	'lccp_class8':'ZZ',
	'lccp_class9':'ZZ',
	'lccp_cls10':'ZZ',
	'lccp_age':'ADULT_AGE',
	'lccp_conc':'ZZZZZZ'}
	post_data=urllib.urlencode(post_data)
	headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Language':'en-US,en;q=0.8',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	'Host':'www.indianrail.gov.in',
	'Origin':'http://indiatrain.in',
	'Referer':'http://indiatrain.in/Rail/getAvailabilityMMT2.aspx?Train_No='+args['train_n']+'&Station_From='+args['stn_from']+'&Station_To='+args['stn_to']+'&mDay='+args['day']+'&mMonth='+args['month']+'&mYear='+args['year']+'&mClass='+args['class']+'&mQuota='+args['quota']+'&temp=1318195420696',
	'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1'}
	request=urllib2.Request("http://www.indianrail.gov.in/cgi_bin/inet_accavl_cgi1.cgi",post_data,headers)
	response=urllib2.urlopen(request).read()
	##decompressed_data=zlib.decompress(response, 16+zlib.MAX_WBITS)
	soup=BeautifulSoup(response)
	date=str(int(args['day'])+1)+"-"+args['month']+"-"+args['year']
	tds=soup.find(text=re.compile('S.No.'))
	try:
		td_text=tds.parent.parent.parent.find(text=re.compile(date)).next.next.next
	except:
		return
	re_avail_text=re.compile(r'\w+')
	re_avail_n=re.compile(r'\d+')
	avail_text=td_text

	avail_stat=re_avail_text.search(avail_text).group()
	if(avail_stat=='AVAILABLE'):
		avail_n=re_avail_n.search(avail_text).group()
		print args['train_n']+" "+avail_n
	return

def lookup(trains,args):
	for train_n in trains.iterkeys():
		args['train_n']=train_n
		find_availablity(args)
	return

trains=find_trains('GWL','MTJ')
args={'stn_from':'KYN','stn_to':'GWL','day':'14','month':'10','year':'2011','class':'3A','quota':'CK'}
lookup(trains,args)
