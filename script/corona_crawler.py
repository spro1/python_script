import urllib.request
import re
from bs4 import BeautifulSoup


url = "http://ncov.mohw.go.kr/"
fp = urllib.request.urlopen(url)
data = fp.read()
fp.close()

#print (source)



def FindInt(string):
    int_string = re.findall("\d", string)
    int_string = "".join(int_string)
    return int(int_string)


#f = open('test.html', 'r', encoding='utf-8')
#data = f.read()

soup = BeautifulSoup(data, 'html.parser')
content = soup.find('div' ,class_='live_left')

update_date = content.find('span',class_='livedate').text
print("������Ʈ ��¥ : %s" % update_date)
live_data = content.find_all('span',class_='num')
confirm = FindInt(live_data[0].text)
recover = FindInt(live_data[1].text)
cure = FindInt(live_data[2].text)
dead = FindInt(live_data[3].text)
examine = FindInt(live_data[4].text)
examine_complete = FindInt(live_data[5].text)

print("Ȯ���� : %s" % confirm)
print("��ġ : %s" % recover)
print("ġ�� �� : %s" % cure)
print("��� : %s" % dead)
print("���� �˻�� : %s" % examine)
print("���� �˻�Ϸ�� : %s" % examine_complete)
print("���� Ȯ���� : %.2f%%" % (confirm/examine_complete*100))

city_data = soup.find('div', class_='live_right').find_all('button')
for cdata in city_data:
    city_num = cdata['data-city']
    city_name = cdata.find('span', class_='name').text
    city_virus = cdata.find('span', class_='num').text
    print ("���� : %s, Ȯ���� : %s" % (city_name, city_virus))



