from bs4 import BeautifulSoup  # BeautifulSoup is a library for parsing HTML and XML documents
import requests  # requests is a library for making HTTP requests
import time

print('Input four skills you are not familiar with')
unfamiliar_skills = a, b, c, d = input('Enter skills: ').split(',')      # split the input into a list
print(f'Filtering Out  {unfamiliar_skills}')        # print the list of skills


def find_jobs():    # function to find jobs
    html_text = requests.get(    # get the html text from the url
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='
        'Data+Analysis'
        '&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')                                         # create a soup object
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')                 # find all the jobs
    for index, job in enumerate(jobs):                                              # loop through the jobs
        published_date = job.find('span', class_='sim-posted').span.text            # find the published date
        if 'few' in published_date:                                                 # if the job is less than a week old
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('  ', '')    # find the company name
            skills = job.find('span', class_='srp-skills').text.replace('  ', '')   # find the skills
            more_info = job.header.h2.a['href']                                     # find the more info link
            experience = job.find('ul', class_='top-jd-dtl clearfix').li.text.split('l')[1]     # find the experience
            location = job.find('ul', class_='top-jd-dtl clearfix').span.text       # find the location
            for unfamiliar_skill in unfamiliar_skills:                              # loop through the unfamiliar skills
                if unfamiliar_skill not in skills:                                  # if the skill is not in the skills
                    with open(f'posted_jobs/{index}.txt', 'w') as file:             # open the file
                        file.write(f'Company Name: {company_name.strip()} \n')      # write the company name
                        file.write(f'Required Skills: {skills.strip()} \n')         # write the skills
                        file.write(f'Description: {more_info.strip()} \n')          # write the more info link
                        file.write(f'Years of Experience: {experience} \n')         # write the experience
                        file.write(f'Location: {location} \n')                      # write the location
                    print(f'File Saved: {index}')                                   # print the file saved


if __name__ == '__main__':                           # if the file is run directly
    while True:                                      #  loop forever
        find_jobs()                                  #  find jobs
        time_wait = 10                               #  wait 10 seconds
        print(f'Waiting {time_wait} minutes...')     #  print the time
        time.sleep(time_wait * 60)                   #  wait 10 minutes
