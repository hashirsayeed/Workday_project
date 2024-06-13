from urllib import request
import json
from datetime import datetime

def get_data():
    try:
        link = "https://hs-recruiting-test-resume-data.s3.amazonaws.com/allcands-full-api_hub_b1f6-acde48001122.json"

        #getting data from the link through the object of urllib
        with request.urlopen(link) as url:
            data = json.load(url)
        return data
    except Exception as e:
        print("Error while accessing the link!!", e)

def retrieve_info(data):
    try:
        for ind, candidate in enumerate(data):
            if "contact_info" in candidate:
                #getting candidate name
                candidate_name = candidate['contact_info']['name']['formatted_name']
                print(f"############################## Candidate No. {ind+1} #################################")
                print(f"Hello {candidate_name}!")
            else:
                raise Exception
            if "experience" in candidate:
                #getting info about experience
                exp = candidate['experience']
                if not exp:
                    print("Non Experienced Candidate!")
                else:    
                    for ind, company in enumerate(exp):
                        if ind == 0:
                            company_name = company['company_name']
                            title = company['title']
                            start_date = company['start_date']
                            end_date = company['end_date']
                            location = company['location']['short_display_address']
                            print(f"Worked as: {title}, From {start_date} To {end_date} in {company_name} {location}.")
                        else:
                            company_name = company['company_name']
                            title = company['title']
                            old_date = start_date
                            start_date = company['start_date']
                            end_date = company['end_date']
                            location = company['location']['short_display_address']
                            gap = (datetime.strptime(old_date, "%b/%d/%Y") - datetime.strptime(end_date, "%b/%d/%Y")).days
                            print(f"Gap in CV for {gap} days")
                            print(f"Worked as: {title}, From {start_date} To {end_date} in {company_name} {location}.")
            else:
                raise Exception
            
    except Exception as e:
        print("Error while retrieving the infor from the data!", e)

if __name__ == "__main__":
    #get data from the link
    data = get_data()
    #get information of candidates
    retrieve_info(data)