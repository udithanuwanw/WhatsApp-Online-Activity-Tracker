from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import csv
from datetime import datetime
import os
import telegram
from selenium.webdriver.common.by import By
import random
webscript1='''



const moduleRaid = function () {
  moduleRaid.mID  = Math.random().toString(36).substring(7);
  moduleRaid.mObj = {};

  fillModuleArray = function() {
    (window.webpackChunkbuild || window.webpackChunkwhatsapp_web_client).push([
      [moduleRaid.mID], {}, function(e) {
        Object.keys(e.m).forEach(function(mod) {
          moduleRaid.mObj[mod] = e(mod);
        })
      }
    ]);
  }

  fillModuleArray();

  get = function get (id) {
    return moduleRaid.mObj[id]
  }

  findModule = function findModule (query) {
    results = [];
    modules = Object.keys(moduleRaid.mObj);

    modules.forEach(function(mKey) {
      mod = moduleRaid.mObj[mKey];

      if (typeof mod !== 'undefined') {
        if (typeof query === 'string') {
          if (typeof mod.default === 'object') {
            for (key in mod.default) {
              if (key == query) results.push(mod);
            }
          }

          for (key in mod) {
            if (key == query) results.push(mod);
          }
        } else if (typeof query === 'function') { 
          if (query(mod)) {
            results.push(mod);
          }
        } else {
          throw new TypeError('findModule can only find via string and function, ' + (typeof query) + ' was passed');
        }
        
      }
    })

    return results;
  }

  return {
    modules: moduleRaid.mObj,
    constructors: moduleRaid.cArr,
    findModule: findModule,
    get: get
  }
}

if (typeof module === 'object' && module.exports) {
  module.exports = moduleRaid;
} else {
  window.mR = moduleRaid();
}
window.mR = moduleRaid();
window.Store = Object.assign({}, window.mR.findModule(m => m.default && m.default.Chat)[0].default);

function startnew(){
var online = {};
var parentWindow ;

window.Store.Presence.toArray().forEach(function(c) {
if (!c || !c.id)
return;

if (!c.isSubscribed) {
c.subscribe();
				}
if (!c.chatActive) {
c.chatActive=true;
				}	
if (!c.hasData) {
c.hasData=true;
				}							


if (c.isOnline == undefined)
return;


if (c.isOnline==true){
	console.log(c.id+ '');
	
} 

	});		
		
	}		

			












'''
webscript2='''

function startnew(){
var online = {};
var parentWindow ;

window.Store.Presence.toArray().forEach(function(c) {
if (!c || !c.id)
return;

if (!c.isSubscribed) {
c.subscribe();
				}
if (!c.chatActive) {
c.chatActive=true;
				}	
if (!c.hasData) {
c.hasData=true;
				}							


if (c.isOnline == undefined)
return;


if (c.isOnline==true){
	console.log(c.id+ '');
	
} 

	});		
		
	}		
startnew();
			
            



'''
def notify_ending(message):
    
    token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'#your telegram bot token
    chat_id = '5214061330'#your telegram chat id
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)
class onlinestatescls():
   def __init__(self,phonenumber,status):
      self.phonenumber=phonenumber
      
      self.status=status
def create_objects(target_trackinglist):        
         

    for objectnumber in target_trackinglist:
       name=f"obj{objectnumber}"
       myobjects[name]=myobjects.get(name,onlinestatescls(objectnumber,'offline'))    

cwd=os.getcwd()
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

driver.execute_script(webscript1)
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
      driver.execute_script(webscript1)
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
            driver.execute_script(webscript1)
            sleep(2)
                    
   try: 
    
            driver.find_elements(By.XPATH,'//*[@role="listitem"]')[random.randint(0,5)].click()
   except:
            pass
   
   el=driver.find_elements(By.XPATH,'//*[@role="textbox"]')[1]
    
   senndword='test'
   for l in senndword:
        sleep(0.1)
        el.send_keys(l)
   el.send_keys(4 * Keys.BACKSPACE)    
   
   L=[]
   driver.execute_script(webscript2)
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