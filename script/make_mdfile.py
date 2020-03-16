import datetime

'''
github blog make default markdown page

---
layout: post
title:  "title name"
date:   2020-03-16
categories: ETC
---

'''

now = datetime.datetime.now()
filename_date = str(now).split(" ")[0]
#file name input
filename = input("input filename : ").replace(" ","-")
filename = "%s-%s.md"%(filename_date,filename)
print("filename : %s"%(filename))

#title input
title = input("input title : ")
print("title : %s"%title)

#categories input
category = input("input category : ")
print ("category : %s"%category)

data = """---
layout: post
title:  "%s"
date:   %s
categories: %s
---
"""%(title, str(now), category)

print(data)
#make file
# path = "C:\test\"
# filename = path+filename
f = open(filename,'w', encoding='utf-8')
f.write(data)
f.close()

