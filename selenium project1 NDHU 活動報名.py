#import selenium 模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
# 設定 chrome driver 的執行檔路徑
options = Options()
options.chrome_executable_path=r"C:\Users\user\OneDrive\桌面\python vscode\chromedriver.exe"
#建立 Driver 物件實體 用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx")

titles=[]
times=[]
whens=[]
cansigns=[]

j=2
while(1): #while is used to change page

    for i in range(10): #for is used to get the data

        id_name = "BodyContent_gvActs_lblGv_act_name_"+str(i)
        try:# use "try" becase there are some page are not have 10 activities!!
            bool_time = driver.find_element(By.ID,"BodyContent_gvActs_lblGv_xsl_check_"+str(i))
            if(bool_time.text.find("不可")==-1):
                how_many_time = driver.find_element(By.ID,"BodyContent_gvActs_lblGv_xsl_check_"+str(i))
                how_many_time_text = how_many_time.text[how_many_time.text.find("/")+1:]
                times.append(how_many_time_text)
                title = driver.find_element(By.ID,id_name)
                titles.append(title.text)
                when = driver.find_element(By.ID,"BodyContent_gvActs_lblGv_act_dt_"+str(i))
                whens.append(when.text)
                cansign = driver.find_element(By.ID,"BodyContent_gvActs_lblGv_participant_"+str(i))
                cansigns.append(cansign.text)

            else:continue
        except Exception:
            break
    try:# try wheather there are still have page or not
        page = driver.find_element(By.LINK_TEXT,str(j))
        page.click()
        j+=1
    except:
        break

for i in range(len(times)):
    print(f"活動名稱:{titles[i]}")
    print(f"時數:{times[i]}")
    print(f"時間:{whens[i]}")
    print(f"誰可以參加:{cansigns[i]}\n")

print("Do you want to sign any activity?(yes / no)")
ans = str(input())

if(ans == "yes"):
    print("Please enter the activity's name:")
    n = str(input())

    time.sleep(5)
    #在視窗輸入活動名稱
    driver.find_element(By.ID,"BodyContent_txtActName").send_keys(n)

    #在按鈕按下enter
    driver.find_element(By.ID,"BodyContent_btnSearchAct").send_keys(Keys.ENTER)

    #按下"報名"
    driver.find_element(By.ID,"BodyContent_gvActs_lbtGridApply_0").click()

    student_id = ""
    password = "" 

    win_student_id = driver.find_element(By.ID,"BodyContent_txtAccount")
    win_password = driver.find_element(By.ID,"BodyContent_txtPassword")

    #輸入帳密
    win_student_id.send_keys(student_id)
    win_password.send_keys(password)

    #按下enter
    driver.find_element(By.ID,"BodyContent_btnLogin").send_keys(Keys.ENTER)

    driver.find_element(By.ID,"BodyContent_btnContinueApply").click()

    driver.find_element(By.ID,"BodyContent_btnApplyAct").click()

else:
    driver.close()

time.sleep(5)
driver.close()

print("sign sucessful!")
