import config
from robobrowser import RoboBrowser
import re
import time
from datetime import datetime


fw = open('DATA.csv', 'a')
br = RoboBrowser()
br.open(r"https://e-hentai.org/bounce_login.php")
form = br.get_form()
form['UserName'] = config.DATACOUP_NAME
form['PassWord'] = config.DATACOUP_PASS
br.submit_form(form)
br.open("https://e-hentai.org/hentaiathome.php")
now =datetime.now()
time.sleep(10)
src = str(br.parsed()) #store all the htmlpage into src

#get status
StatusStart = '<td style="font-weight:bold; color:green">'
StatusEnd = '</td>'
Status = re.search('%s(.*)%s' % (StatusStart, StatusEnd), src).group(1)
print('Status:\t'+Status)
fw.write(Status + ',')

#get Created
CreatedStart = '</td>\n<td>'
CreatedEnd = '</td>\n<td>'
Created = re.search('%s(.*)%s' % (CreatedStart, CreatedEnd), src).group(1)
print('Created:\t'+Created)
fw.write(Created + ',')

#get last seen time
LastSeenStart = '</td>\n<td>' + Created + '</td>\n<td>'
LastSeenEnd = '</td>'
LastSeen = re.search('%s(.*)%s' % (LastSeenStart, LastSeenEnd), src).group(1)
print('LastSeen:\t'+LastSeen)
fw.write('"' + LastSeen + '"' + ',')

#get file served number
FilesServedStart = '</td>\n<td>'
FilesServedEnd = '</td>\n<td style="text-align:left; padding-left:7px">'
FilesServed = re.search(LastSeen + '%s(.*)%s' % (FilesServedStart, FilesServedEnd), src).group(1)
print('FileServed:\t')
print(int(FilesServed.replace(',', '')))
fw.write(FilesServed.replace(',', '') + ',')

#get ip
ClientIPStart = '</td>\n<td style="text-align:left; padding-left:7px">'
ClientIPEnd = '</td>'
ClientIP = re.search('%s(.*)%s' % (ClientIPStart, ClientIPEnd), src).group(1)
print('ClientIP:\t')
print(ClientIP)
fw.write(ClientIP + ',')

#get maxspeed
Max_SpeedStart = '</td>\n<td>1.4.2 Stable</td>\n<td>'
Max_SpeedEnd = ' KB/s</td>\n<td style="color:green">'
Max_Speed = re.search('%s(.*)%s' % (Max_SpeedStart, Max_SpeedEnd), src).group(1)
print('Max_Speed:KB/s\t')
print(int(Max_Speed))
fw.write(Max_Speed + ',')

#get trust
TrustStart = 'KB/s</td>\n<td style="color:green">'
TrustEnd = '</td>'
Trust = re.search('%s(.*)%s' % (TrustStart, TrustEnd), src).group(1)
print('Trust:\t')
print(int(Trust))
fw.write(Trust + ',')

#get Hitrate
HitrateStart = '</td>\n<td>'
HitrateEnd = ' / min</td>\n<td>'
Hitrate = re.search('%s(.*)%s' % (HitrateStart, HitrateEnd), src).group(1)


#get Quality
QualityStart = '</td>\n<td>'
QualityEnd = '</td>\n<td>' + Hitrate + ' / min</td>'
Quality = re.search('%s(.*)%s' % (QualityStart, QualityEnd), src).group(1)
print('Quality:\t')
print(Quality)
fw.write(Quality+ ',')
print('Hitrate:/ min\t')
print(float(Hitrate))
fw.write(Hitrate + ',')

#get Hathrate
HathrateStart = ' / min</td>\n<td>'
HathrateEnd = ' / day</td>\n<td>'
Hathrate = re.search('%s(.*)%s' % (HathrateStart, HathrateEnd), src).group(1)
print('Hathrate:/ day\t')
print(float(Hathrate))
fw.write(Hathrate + ',')

#get Country
CountryStart = ' / day</td>\n<td>'
CountryEnd = '</td></tr>'
Country = re.search('%s(.*)%s' % (CountryStart, CountryEnd), src).group(1)
print('Country:\t'+Country)
fw.write(Country + ',')
fw.write(str(now) + '\n')
fw.close()
#Your IP Max_Speed has been temporarily banned for excessive pageloads which indicates that you are using automated mirroring/harvesting software. The ban expires in 33 minutes and 26 seconds
#Your IP address has been temporarily banned for excessive pageloads which indicates that you are using automated mirroring/harvesting software. The ban expires in 23 hours and 16 minutes