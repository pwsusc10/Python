site = "http : //naver.com"
site_temp = site.replace("http : //", "")
print(site_temp)
site_temp = site_temp[:site_temp.index(".")]
print(site_temp)