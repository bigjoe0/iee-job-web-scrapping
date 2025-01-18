import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import os

titles=[]
locations=[]
field=[]
links=[]
requirements=[]

page=1
while page<=3:
    # 2nd step: use request to fetch the url
    result=requests.get(f"https://iee-sensing.com/iee-jobs/page/{page}/")

    # 3rd step: save page content/markup
    src=result.content
    #print(src)

    # 4th step: create soup object to parse content
    soup=BeautifulSoup(src,"lxml")
    #print(soup)

    # 5th step: find the elements containing info i need
    # job title , location, field => output is a list
    job_titles=soup.find_all("h1",{"class":"jobs_item__title"})
    job_locations=soup.find_all("p",{"class":"jobs_item__location"})
    job_field=soup.find_all("p",{"class":"jobs_item__profession"})
    job_links=soup.find_all("a",{"class","jobs_item__link"})
    #print(job_field)

    

    #6th step: loop over returned lists to extract needed info into other lists
    for i in range(len(job_titles)):
        titles.append(job_titles[i].text)
        locations.append(job_locations[i].text)
        field.append(job_field[i].text)
        links.append(job_links[i].attrs['href'])

    #print(f"page {page}")
    page+=1
    

#6.1th step: loop over returned links to extract inner data
# for link in links:
#     print(f"####{link}####")
#     result=requests.get(link)
#     src=result.content
#     soup=BeautifulSoup(src,"lxml")
#     job_requirements=soup.find("div",{"id":"mainRight"}).ul
#     if job_requirements==None:
#         job_requirements=soup.find("section",{"class":"single__content content"})
#     # print(job_requirements)
#     requirements_text=""
#     for li in job_requirements.find_all("li"):
#         requirements_text+=li.text
# print(requirements_text)

# 7th step:
file_list=[titles,locations,field,links]
exported=zip_longest(*file_list)

# 8th step: create csv file and fill it with values

# Get the user's Downloads folder
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Define the file name
file_name = "youssef_iee_excel.csv"

# Full file path
file_path = os.path.join(downloads_path, file_name)

with open(file_path,"w",newline="") as myfile: #aliasing to this name to deal with it
    wr=csv.writer(myfile)
    wr.writerow(["job title","location","field","links"])
    wr.writerows(exported)

print("\n1.This Python application get job listings from the 'iee' Careers website")
print("2.Then saves them into an Excel file with details like job title, fieled, location, and links.")
print("3.It provide an organized and updated view of opportunities which is updated automatically\n")
print("4.File is downloaded in your Downloads\n")
input("### Done by Youssef Elsawy for 'iee' ###")