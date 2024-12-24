import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import csv
from datetime import datetime
import os
from selenium.webdriver.common.by import By
import random
import requests

# Load configuration from JSON file
def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)



# Function to load JavaScript from an external file
def load_web_script(file_path):
    with open(file_path, 'r') as file:
        return file.read()

  

def notify_ending(message):
    """Send a notification to a Telegram bot."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send Telegram message: {e}")    
class onlinestatescls():
   def __init__(self,phonenumber,status):
      self.phonenumber=phonenumber
      
      self.status=status
def create_objects(target_trackinglist):        
         

    for objectnumber in target_trackinglist:
       name=f"obj{objectnumber}"
       myobjects[name]=myobjects.get(name,onlinestatescls(objectnumber,'offline'))    

cwd=os.getcwd()
config = load_config()
TELEGRAM_BOT_TOKEN = config['TELEGRAM_BOT_TOKEN']
TELEGRAM_CHAT_ID = config['TELEGRAM_CHAT_ID']
with open('trackinglist.txt') as f:
    trackinglist  = [line.rstrip() for line in f]

    



options = webdriver.ChromeOptions() 
options.add_argument(f"user-data-dir={cwd}\\whatsapp")
options.set_capability("goog:loggingPrefs",{ 'browser':'ALL' })
driver = webdriver.Chrome(options=options)
driver.get ("https://web.whatsapp.com")
input("Press Enter after scanning QR code...")
sleep(30)


myobjects={} 
create_objects(trackinglist)
web_script_path = 'web_script_1.js'

# Load the script
web_script_1 = load_web_script(web_script_path)
driver.execute_script(web_script_1)
time_counter=0
while True:
   if  time_counter==60*60:
      print('restarting')
      for contact in trackinglist:
               
                      if myobjects[f'obj{contact}'].status=='offline':
                             
                                 continue
                      else:     
               
                               t = time.localtime()
                               current_time = time.strftime("%d-%m-%Y %H:%M:%S", t)
                               current_time_telegram=time.strftime("%H:%M:%S", t)


                               myobjects[f'obj{contact}'].status='offline'
                               myobjects[f'obj{contact}'].lastofflinetime=datetime.now()
                               myobjects[f'obj{contact}'].offline=current_time
                               differnce=myobjects[f'obj{contact}'].lastofflinetime-myobjects[f'obj{contact}'].lastonlinetime
                               differnce_str=str(differnce).split('.')[0]
                               csvfile=open(f'{contact}.csv','a')
                               filnames=['online','offline','duration']


                               writer=csv.DictWriter(csvfile,fieldnames=filnames)
                               writer.writerow({'online':myobjects[f'obj{contact}'].online,'offline':myobjects[f'obj{contact}'].offline,'duration':differnce_str})
                               file=open(f'{contact}.txt','a')
                               file.write("offline-"+ str(current_time)+ ' duration '+str(differnce_str)+"\n") 
                               print(f"{contact} Offline {current_time} duration= {differnce_str}\n")
                                  
                               notify_ending(f"{contact} Offline {current_time_telegram} \nduration= {differnce_str}\n")
                               csvfile.close()
                               file.close()
                                
      driver.close()          
      options = webdriver.ChromeOptions() 
      options.add_argument(f"user-data-dir={cwd}\\whatsapp")
      options.set_capability("goog:loggingPrefs",{ 'browser':'ALL' })
      driver = webdriver.Chrome(options=options)
      driver.get ("https://web.whatsapp.com")
      sleep(30)    
      web_script_path = 'web_script_1.js'

      # Load the script
      web_script_1 = load_web_script(web_script_path)
      driver.execute_script(web_script_1)
      time_counter=0  
      sleep(2)  
                
   with open('trackinglist.txt') as f:
               temptrackinglist  = [line.rstrip() for line in f if line not in trackinglist] 
               if len(temptrackinglist)>=1:
                       create_objects(temptrackinglist)
                       trackinglist.extend(temptrackinglist)
   try: 
    
            check_con=driver.find_elements(By.XPATH,'//*[@role="listitem"]')
   except:
            driver.close()          
            options = webdriver.ChromeOptions() 
            options.add_argument(f"user-data-dir={cwd}\\whatsapp")
            options.set_capability("goog:loggingPrefs",{ 'browser':'ALL' })
            driver = webdriver.Chrome(options=options)
            
            driver.get ("https://web.whatsapp.com")
            sleep(30)
            web_script_path = 'web_script_1.js'

            # Load the script
            web_script_1 = load_web_script(web_script_path)
            driver.execute_script(web_script_1)
            sleep(2)

   while True:          
                    
       try: 
        
                driver.find_elements(By.XPATH,'//*[@role="listitem"]')[random.randint(0,5)].click()
                break
       except:
                pass
   try:

       el=driver.find_elements(By.XPATH,'//*[@role="textbox"]')[1]
    

    
       senndword='test'
       for l in senndword:
            sleep(0.1)
            el.send_keys(l)
       el.send_keys(4 * Keys.BACKSPACE)  
   except:
      pass        
   
   L=[]
   web_script_path = 'web_script_2.js'

    # Load the script
   web_script_2 = load_web_script(web_script_path)
   driver.execute_script(web_script_2)
   for e in driver.get_log('browser'):
      numberline=e['message']
      
      numberphrase=numberline.split(' ')[2]
      
      modnumberphrase=numberphrase.replace('"','')
      Modnumberphrase=modnumberphrase.replace('"','')
   
      number=Modnumberphrase.split('@')[0]
      
      L.append(number)
      
   for contact in trackinglist:
                  
            if contact in L:
                        if myobjects[f'obj{contact}'].status=='online':
                                  
                                  continue
                        else:
                           t = time.localtime() 
                           current_time = time.strftime("%d-%m-%Y %H:%M:%S", t)
                           current_time_telegram=time.strftime("%H:%M:%S", t)
                           myobjects[f'obj{contact}'].status='online' 
                           myobjects[f'obj{contact}'].lastonlinetime=datetime.now()
                           myobjects[f'obj{contact}'].online=current_time
                           file=open(f'{contact}.txt','a')
                           file.write("Online-"+ str(current_time)+"\n") 
                           print(f"{contact} Online {current_time}\n") 
                            
                           notify_ending(f"{contact} Online {current_time_telegram}\n")
                           file.close()
            else:
                        if myobjects[f'obj{contact}'].status=='offline':
                             
                             continue
                        else:  
                               t = time.localtime()
                               current_time = time.strftime("%d-%m-%Y %H:%M:%S", t)
                               current_time_telegram=time.strftime("%H:%M:%S", t)
                               
                               myobjects[f'obj{contact}'].status='offline'
                               myobjects[f'obj{contact}'].lastofflinetime=datetime.now()
                               myobjects[f'obj{contact}'].offline=current_time
                               differnce=myobjects[f'obj{contact}'].lastofflinetime-myobjects[f'obj{contact}'].lastonlinetime
                               differnce_str=str(differnce).split('.')[0]
                               csvfile=open(f'{contact}.csv','a')
                               filnames=['online','offline','duration']
                              
               
                               writer=csv.DictWriter(csvfile,fieldnames=filnames)
                               writer.writerow({'online':myobjects[f'obj{contact}'].online,'offline':myobjects[f'obj{contact}'].offline,'duration':differnce_str})
                               file=open(f'{contact}.txt','a')
                               file.write("offline-"+ str(current_time)+ ' duration '+str(differnce_str)+"\n") 
                               print(f"{contact} Offline {current_time} duration= {differnce_str}\n")
                               
                               notify_ending(f"{contact} Offline {current_time_telegram} \nduration= {differnce_str}\n")
                               csvfile.close()
                               file.close()
                                 

                     

   
    
   
   sleep(1) 
   time_counter+=1 