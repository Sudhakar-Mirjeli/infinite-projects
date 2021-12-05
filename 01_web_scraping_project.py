from bs4 import BeautifulSoup
import requests
import json
import pandas as pd


# for i in range(1,3):
#     page=requests.get('https://www.careerjet.com/software-engineer-jobs.html?p='+str(i)+'/')


page=requests.get('https://www.careerjet.com/software-engineer-jobs.html?p=1')
soup=BeautifulSoup(page.content,'html.parser')
job=soup.find('ul', class_='jobs')

job_details=job.find_all('article',class_='job clicky')

job_role=[job.find('a').get_text() for job in job_details]
company_name=[job.find(class_='company').get_text() for job in job_details]
job_location=[job.find(class_='location').get_text() for job in job_details]
job_posted=[job.find(class_='badge badge-r badge-s badge-icon').get_text() for job in job_details]


all_job_details=pd.DataFrame(
    [{
    
    'Job_designation': job_role,
    'Company_name': company_name,
    'Location': job_location,
    'Post_history': job_posted,
    }]
    
)

# adding all data into JSON file
all_job_details.to_json('caererjet_jobs.json')


# adding all data into CSV file
all_job_details.to_csv('caererjet_jobs.CSV')