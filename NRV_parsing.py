import urllib2.request
import re

dict_of_all_isotopes = {}


webUrl = urllib.request.urlopen('http://nrv.jinr.ru/nrv/webnrv/map/')
if str(webUrl.getcode())=='200': print ('The main page have been successfully opened')
data = str(webUrl.read())
pattern_links = re.compile('nucleus\.php\?q='+'[A-Za-z]{1,3}[1-9][0-9]{0,2}')
list_of_links = pattern_links.findall(data)
print(len(list_of_links), 'isotopes have been founded.')
#for link in list_of_links: print(link, end='\n')

for link in list_of_links:
    
    webUrl1 = urllib.request.urlopen('http://nrv.jinr.ru/nrv/webnrv/map/' + str(link))
    if str(webUrl1.getcode())=='200':
        print ('The page --', link[14:], '-- have been successfully opened')
    data1 = str(webUrl1.read())
    pattern_links1 = re.compile('class=nuc' + '.*[\d]{1,}.*[\d].*' + str(link[14:-2]) + '.*' + 'T<sub>1\/2<\/sub>=<\/span>' + '.*<br></td>')
    list_of_links1 = pattern_links1.findall(data1)
    list_of_links1 = str(list_of_links1)

    print('list_of_links1', list_of_links1)
    
    pattern_links2 = re.compile('>[\d]{1,}')
    list_of_links2 = pattern_links2.findall(list_of_links1)
    for i in range (len(list_of_links2)):
        x = int(list_of_links2[i][1:])
        list_of_links2[i] = x
    
    print('list_of_links2', list_of_links2)
    
    pattern_links3 = re.compile('T<sub>1/2</sub>=</span>.*<br><\/td>')
    list_of_links3 = pattern_links3.findall(list_of_links1)
    Thalf = str(list_of_links3)
    Thalf = Thalf[25:-11]

    print('list_of_links3', list_of_links3)
    
    dict_of_all_isotopes['Element'] = link[14:-2]
    dict_of_all_isotopes['Mass Number'] = list_of_links2[0]
    dict_of_all_isotopes['Charge Number'] = list_of_links2[1]
    dict_of_all_isotopes['Neutrons Number'] = list_of_links2[2]
    dict_of_all_isotopes['Time Of Half Descence'] = Thalf
    
    print(link[14:-2], 'Done')

print(dict_of_all_isotopes)