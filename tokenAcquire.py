from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


class TokenAcquire:


    def __init__(self, headless=False):
        options = Options()


        if (headless):
            options.add_argument("--headless")

        self.DEV_PLAYLIST_URL = "https://developer.spotify.com/console/put-playlist/"
        self.XPATH_ACC_COOKIES = "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[1]"

        self.driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
        
    def start(self):
        print("\t[TokenHandler]: Initiating requests...\n")
        self.driver.get(self.DEV_PLAYLIST_URL)
        sleep(1.5)
        banner = self.driver.find_element(By.XPATH, self.XPATH_ACC_COOKIES)
        banner.click()
        sleep(1.5)
        

    def login(self):
        print("\t[TokenHandler]: User not found. Logging in...\n")
        username = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/input")
        username.send_keys("")
        password = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/input")
        password.send_keys("")
        sleep(.3)
        login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[3]/div[2]/button")
        login.click()
        print("\t[TokenHandler]: Successfully logged in!")
        sleep(1)



    def getToken(self): 
        print("\t[TokenHandler]: Requesting token...")
        get_token = self.driver.find_element(By.CLASS_NAME, "btn-green")
        get_token.click()
        public_box = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div/div/div[1]/div/label")
        private_box = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div/div/div[2]/div/label")
        sleep(.5)
        public_box.click()
        sleep(.3)
        private_box.click()
        sleep(.3)
        request_token_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[2]/div/div/div[1]/div/div/div[2]/form/input")
        request_token_btn.click()
        sleep(1)

        if "accounts.spotify.com" in self.driver.current_url:
            self.login()

        sleep(2)
        token = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[2]/div/div/form/div[4]/div/input").get_attribute('value')

        print("\t[TokenHandler]: Recieved token {0:s}".format(token))
        return token


    def uploadCover(self):
        pass


