### AutoLogin Bot for IITKGP ERP System ###


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui
driver = webdriver.Firefox()

def login(url, userDivId, username, passDivId, passwrd, ansDivId, ansLabelId, answer, submit):
	driver.get(url);

	driver.find_element_by_id(userDivId).send_keys(username)
	driver.find_element_by_id(passDivId).send_keys(passwrd)
	wait = ui.WebDriverWait(driver, 10)
	wait.until(ec.visibility_of(driver.find_element_by_id(ansDivId)))
	question = driver.find_element_by_id(ansLabelId).text
	if(question == "Q1"):
		driver.find_element_by_id(ansDivId).send_keys(answer['Q1'])
	elif(question == "Q2"):
		driver.find_element_by_id(ansDivId).send_keys(answer['Q2'])
	elif(question == "Q3"):
		driver.find_element_by_id(ansDivId).send_keys(answer['Q3'])
	driver.find_element_by_id(submit).click();
	wait.until(ec.visibility_of(driver.find_element_by_id("headerDIV")))
	print(driver.find_elements_by_css_selector("#moduleUL li")[0].text)
	driver.find_elements_by_css_selector("#moduleUL li")[0].click()
	driver.find_elements_by_class_name("panel-heading accordian-toggle collapsed")[8].click()
	driver.find_element_by_css_selector("#collapse16555 a")[0].click()


url = "https://erp.iitkgp.ac.in"
userDivId = "user_id"
username = ""#yourUserName
passDivId = "password"
passwrd = ""#yourPassword
ansLabelId = "question"
ansDivId = "answer"
answer = {"Q1":"A1", "Q2":"A2", "Q3":"A3"}#your question and answer string
submit = "loginFormSubmitButton"
login(url,userDivId,username,passDivId,passwrd,ansDivId,ansLabelId,answer,submit)