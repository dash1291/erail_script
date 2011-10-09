
Find trains-->

request URL:http://erail.in/rail/getTrains.aspx?Station_From=GWL&Station_To=NDLS&DataSource=0&Language=0
---trains pattern

---Train items
reg=re.compile(r'\^\d+\~[A-Za-z0-9 ]+')

	---train numbers from train items
		reg=re.compile(r'\d+')
	---train names from train items
		reg=re.compile(r'[A-Za-z0-9 ]+')

Find Availability-->

request URL : http://indiatrain.in/Rail/getAvailabilityMMT2.aspx?Train_No=11077&Station_From=GWL&Station_To=NDLS&mDay=10&mMonth=10&mYear=2011&mClass=3A&mQuota=GN&temp=1318195420696









