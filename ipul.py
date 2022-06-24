#количество зарегистрированных и ликвидированных ип, количество зарегистрированных и ликвидированных юл
import csv
from matplotlib import pyplot as plt
import numpy as np
filename = 'nalog_regions.csv'
years = list(range(2012, 2021))
width = 0.3
x = np.arange(len(years))
registIP, likvidIP, registUL, likvidUL = [], [], [], [] 
def ipul(num, region):#num - код региона(regcode), region - название региона
	with open(filename, encoding = 'utf8') as f:
		reader = csv.reader(f)
		header_row = next(reader)
		for row in reader:
			kod = int(row[1])
			reg = str(row[2])
			regip = int(row[3])
			likip = int(row[4])
			regul = int(row[6])
			likul = int(row[7])
			if kod == num and reg == region:
				registIP.append(regip)
				likvidIP.append(likip)
				registUL.append(regul)
				likvidUL.append(likul)
ipul(39, 'Калининградская область')
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, registIP, width, label = 'Зарегистрированные ИП')
rects2 = ax.bar(x + width/2, likvidIP, width, label = 'Ликвидированные ИП')
ax.set_title("Зарегистрированные и Ликвидированные ИП")
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
plt.show()
