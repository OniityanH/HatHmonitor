import config
from robobrowser import RoboBrowser
import re

br = RoboBrowser()
br.open(r"https://e-hentai.org/bounce_login.php")
form = br.get_form()
form ['UserName'] = config.DATACOUP_NAME
form ['PassWord'] = config.DATACOUP_PASS
br.submit_form(form)
br.open("https://e-hentai.org/hentaiathome.php")
src = str(br.parsed()) #store all the htmlpage into src

StatusStart = '<td style="font-weight:bold; color:green">'
StatusEnd = '</td>'
Status = re.search('%s(.*)%s' % (StatusStart, StatusEnd), src).group(1)
print(Status)

LastSeenStart = '</td>\n<td>2016-10-16</td>\n<td>'
LastSeenEnd = '</td>'
LastSeen = re.search('%s(.*)%s' % (LastSeenStart, LastSeenEnd), src).group(1)
print(LastSeen)

FilesServedStart = '</td>\n<td>'
FilesServedEnd = '</td>\n<td style="text-align:left; padding-left:7px">'
FilesServed = re.search(LastSeen + '%s(.*)%s' % (FilesServedStart, FilesServedEnd), src).group(1)
print(FilesServed)
for element in FilesServed:
    if FilesServed[element] is ',':
        print('this is a ,')
    else:
        FilesServedstr = FilesServedstr + FilesServed[element]
print(FilesServedstr)
print(int(FilesServedstr))

ClientIPStart = '</td>\n<td style="text-align:left; padding-left:7px">'
ClientIPEnd = '</td>'
ClientIP = re.search('%s(.*)%s' % (ClientIPStart, ClientIPEnd), src).group(1)
print(ClientIP)




#Your IP address has been temporarily banned for excessive pageloads which indicates that you are using automated mirroring/harvesting software. The ban expires in 33 minutes and 26 seconds
