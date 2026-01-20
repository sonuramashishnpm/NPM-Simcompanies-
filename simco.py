##############################################################SSSSSSSSSSSSTTTTTTTTTTAAAAAAAAAARRRRRRRRTTTTTTTTTTTTTTTTT#############################################################################
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import subprocess

def get_chrome_major_version():
    out = subprocess.check_output(
        r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'
    ).decode()
    version = re.search(r"(\d+)\.", out).group(1)
    return int(version)


store_xpath=["/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[7]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[8]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[3]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[4]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[1]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[2]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[6]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[5]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[10]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[9]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[14]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[13]/div[2]",
        "/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[15]/div[2]",
        ]

user_email=input("Enter your simco account email")
user_password=input(f"Enter your simco account {user_email} password")

realm=input("which realm you want to run the code")
if realm=="R1":
    gni=input("Enter no of gloves you want to sell in stores of R1")
    ams1=int(gni)
    amount=ams1*13
    sli=input("Enter price on which you will sell gloves in store of R1")
else:
    gni2=input("Enter no of gloves you want to sell in stores of R2")
    ams12=int(gni2)
    amount2=ams12*14
    sli2=input("Enter price on which you will sell gloves in stores of R2")


class Simco:
    def __init__(self):
        self.options = uc.ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument("--no-first-run")
        self.options.add_argument("--no-service-autorun")
        self.options.add_argument("--password-store=basic")
        self.options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = uc.Chrome(
            options=self.options,
            headless=False,
            version_main=get_chrome_major_version()
            )
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"
            })
   
    def start(self):
        self.url="https://simcompanies.com"
        self.driver.get(self.url)

        self.driver.maximize_window()
       
        time.sleep(2)

        self.cookie=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[3]/div[4]/form/div/div/button[1]")))
        self.cookie.click()
        time.sleep(2)

    def authentication(self,user_email:str,user_password:str):
        self.signin=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[3]/div[3]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/form/div/a")))
        self.signin.click()
        time.sleep(3)
       
        self.email=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.NAME,"email")))
        time.sleep(0.8)
        self.email.send_keys(user_email)
        time.sleep(8)

        self.password=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.NAME,"password")))
        self.password.send_keys(user_password)
        time.sleep(3.5)
        self.password.send_keys(Keys.RETURN)
        time.sleep(3.5)

       

    def buy(self,realm,amount=None,amount2=None):
        if realm=="R2":
            self.r2=WebDriverWait(self.driver,45).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[1]/nav/div/div/div[1]/div[1]/div/div/img")))
            self.r2.click()
            time.sleep(4.5)
           
        self.exchange=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.ID,"menu-exchange")))
        self.exchange.click()
        time.sleep(6)

        self.gloves=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='page']/div/div/div/div[1]/div/div/div[2]/div[4]/div/a[4]")))
        self.gloves.click()                         
        time.sleep(4)

        self.quantity=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.NAME,"quantity")))
        if realm=="R1":
            self.quantity.send_keys(amount)
        else:
            self.quantity.send_keys(amount2)
        time.sleep(2)

        self.buyf=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='page']/div/div/div/div[2]/div/div/div[1]/div[2]/div/form/div/div[3]/button")))
        self.buyf.click()
        time.sleep(2.7)

        self.maap=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.ID,"menu-map")))
        self.maap.click()
        time.sleep(3)
   
    def sell(self,realm,store_xpath,gni=None,sli=None,gni2=None,sli2=None):
        if realm=="R1":
            self.npmstore=WebDriverWait(self.driver,45).until(
                EC.presence_of_element_located((By.XPATH,store_xpath)))
            self.npmstore.click()
            time.sleep(3)
           
            self.gn=WebDriverWait(self.driver,45).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[2]/form/div/div[1]/p/input")))
            self.gn.send_keys(gni)
            time.sleep(1.4)
                                           
            self.sel=WebDriverWait(self.driver,45).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[2]/form/div/div[2]/p/input")))
            self.sel.send_keys(sli)
            self.sel.send_keys(Keys.RETURN)
            time.sleep(7)
                                           
            
           
        else:
            self.npmstore2=WebDriverWait(self.driver,45).until(
                EC.presence_of_element_located((By.XPATH,store_xpath)))
            self.npmstore2.click()
            time.sleep(3)
           
            self.gn2=WebDriverWait(self.driver,45).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[2]/form/div/div[1]/p/input")))
            self.gn2.send_keys(gni2)
            time.sleep(1.4)
           
            self.sel2=WebDriverWait(self.driver,45).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[2]/form/div/div[2]/p/input")))
            self.sel2.send_keys(sli2)
            self.sel2.send_keys(Keys.RETURN)
            time.sleep(8)
           
    def extra(self,gni2,sli2):
        #store14
        store14=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[11]/div[2]")))
        store14.click()
        time.sleep(3)

        gn=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[2]/form/div/div[1]/p/input")))
        gn.send_keys(gni2)              
        time.sleep(1.3)

        sell=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[2]/form/div/div[2]/p/input")))
        sell.send_keys(sli2)
        sell.send_keys(Keys.RETURN)
        time.sleep(8)

        #store15
        store15=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div[1]/div/div/a[16]/div[2]")))
        store15.click()
        sleep(3.7)

        gn=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[2]/form/div/div[1]/p/input")))
        gn.send_keys(gni2)
        time.sleep(1.3)

        sell=WebDriverWait(self.driver,45).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[2]/form/div/div[2]/p/input")))
        sell.send_keys(sli2)
        sell.send_keys(Keys.RETURN)
        time.sleep(8)

##############################################################EEEEEEEEEEEEEEENNNNNNNNNNNNNNNNNNNDDDDDDDDDDDDDDDDDDDDDDD#############################################################################

bot=Simco()
bot.start()
bot.authentication(user_email,user_password)
if realm=="R1":
   bot.buy(realm,amount=amount)
else:
    bot.buy(realm,amount2=amount2)
for store in store_xpath:
    if realm=="R1":
        bot.sell(realm,store,gni=gni,sli=sli)
    else:
        bot.sell(realm,store,gni2=gni2,sli2=sli2)
bot.extra(gni2,sli2)



