import re
import requests
from bs4 import BeautifulSoup
import pprint
import json

# read html

# 국내 동향
# f = open('korea.html', 'r', encoding='utf-8')
# data = f.read()
# f.close()
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11"
fp = requests.get(url)
data = fp.text
fp.close()

corona_data = {}

soup = BeautifulSoup(data, 'html.parser')
confirm_status = soup.find("div", class_="data_table mgt16 mini")
confirm_status = confirm_status.find_all("td")
confirm_status_dict = {}
# 격리 중
isolation = confirm_status[0].text
# 격리 해제
cure = confirm_status[1].text
# 사망
death = confirm_status[2].text
# 누적 확진 환자
confirm = confirm_status[3].text
# 음성
negative = confirm_status[4].text
# 검사 완료
complete = confirm_status[5].text
# 검사 중
testing = confirm_status[6].text

confirm_status_dict["confirm"] = confirm
confirm_status_dict["isolation"] = isolation
confirm_status_dict["cure"] = cure
confirm_status_dict["death"] = death
confirm_status_dict["negative"] = negative
confirm_status_dict["complete"] = complete
confirm_status_dict["testing"] = testing

# 시도별 확진자
# f = open('city.html', 'r', encoding='utf-8')
# data = f.read()
# f.close()
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13"
fp = requests.get(url)
data = fp.text
fp.close()


soup = BeautifulSoup(data, 'html.parser')
city_status = soup.find("div", class_="data_table midd mgt24")
city_status = city_status.select("tbody>tr")
city_status_list = []
for i in city_status:
    city_info = []
    city_dict = {}
    for l in i:
        city_info.append(l.text)
    city = city_info[0]
    new_confirm_f_d = city_info[2]
    new_confirm_f_o = city_info[3]
    city_confirm = city_info[4]
    city_isolation = city_info[5]
    city_cure = city_info[6]
    city_death = city_info[7]

    city_dict["city"] = city
    city_dict["new_confirm_f_d"] = new_confirm_f_d
    city_dict["new_confirm_f_o"] = new_confirm_f_o
    city_dict["confirm"] = city_confirm
    city_dict["isolation"] = city_isolation
    city_dict["cure"] = city_cure
    city_dict["death"] = city_death
    city_status_list.append(city_dict)

#
corona_data["confirm_status"] = confirm_status_dict
corona_data["city_status"] = city_status_list

pprint.pprint(corona_data)
with open("corona.json", "w", encoding='utf-8') as f:
    json.dump(corona_data, f, indent="\t")
