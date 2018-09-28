import time

from datetime import datetime as dt 

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.ndtv.com", "ndtv.com", "facebook.com", "www.facebook.com"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
		print("Get back to work!")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write("\n"+redirect+" "+website+"\n")
	else:
		with open(hosts_path, "r+") as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
				file.truncate()
		print("Have fun!")
	time.sleep(5)

