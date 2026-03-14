import requests
import json
import os
import csv
from datetime import datetime
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv


#apikey stored in a variable as this will make it easier to repalce if required
load_dotenv()
apikey = os.getenv('apikey')
webhook_url = os.getenv('webhook_url')

url_list = ['https://cuskelly.net']

#provide the function with the URL you wish to test, this and the API key into the API URL
def page_speed(url):
    base_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={apikey}"
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fieldnames = ["site", "performance_score", "scan_time"]
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            test_results = response.json()
            site_id = test_results['id']
            performance = test_results["lighthouseResult"]["categories"]["performance"]
            performance_score = performance.get("score") * 100
            row = {"site": url, "performance_score": performance_score, "scan_time": now}
            if performance_score < 75:
                    #discord integration for warnings
                low_score_alert = DiscordWebhook(url=webhook_url, content=f"{url} has a performance score of {performance_score}, this may be unavailable")
                response = low_score_alert.execute()
                file_path = 'sitewarnings.csv'  

                if os.path.exists(file_path) == False:
                    with open('sitewarnings.csv', mode='w', newline="") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()

                with open('sitewarnings.csv', mode='a', newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(row)

            print(site_id, f"The performance score is {performance_score}")

                 
         
            return test_results
        else:
            print(f"Failed to retrieve data {response.status_code}")

    except:
         print("Network is down, skipping this step...")

    

for sites in url_list:


    page_speed(sites)




