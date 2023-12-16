import random
import string
import time

from behave import *

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def patient_name_generator(size=8, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def patient_email_generator(size=8, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def patient_phone_number_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# ------------- Scenario 1 -------------
@given(u'User opens the Pathology Lab Management web application')
def step_impl(context):
    print("Given User opens the Pathology Lab Management web application")


@when(u'User enters valid Username')
def step_impl(context):
    # Send Keys function for Username
    context.driver.find_element(By.NAME, "email").send_keys("test@kennect.io")

    print("When User enters valid Username")


@when(u'User enters valid Password')
def step_impl(context):
    # Send Keys function for Password
    context.driver.find_element(By.NAME, "password").send_keys("Qwerty@1234")

    print("And User enters valid Password")


@when(u'User clicks on Login button')
def step_impl(context):
    # Click function on Login Button
    context.driver.find_element(By.XPATH, "//span[text()='Login']").click()
    context.driver.implicitly_wait(5)

    print("User clicks on Login button")


@then(u'User will be able to Login into the application')
def step_impl(context):
    element = WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
    )
    print("Then User will be able to Login into the application")


# ------------- Scenario 2 -------------
@when(u'User lands on the home page they can view todos and access the Cost Calculator for blood tests')
def step_impl(context):
    # Validating that todos is present in application
    try:
        context.driver.find_element(By.XPATH, "//div[text()='TODO']").is_displayed()
        assert True, "TODO list is present in application"
    except Exception:
        assert False, "TODO list is not present in application"

    # Scroll Down
    context.driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(0.5)

    # Validating that Cost Calculator is present in application
    try:
        context.driver.find_element(By.XPATH, "//div[text()='Test Cost Calculator']").is_displayed()
        assert True, "Cost Calculator is present in application"
    except Exception:
        assert False, "Cost Calculator is not present in application"
    print("When User lands on the home page they can view todos and access the Cost Calculator for blood tests")


@then(u'User is able to view todos and access the Cost Calculator for blood tests')
def step_impl(context):
    print("Then User is able to view todos and access the Cost Calculator for blood tests")


# ------------- Scenario 3 -------------
@when(u'User selects its desired tests under Test Cost Calculator')
def step_impl(context):
    # Scroll Down
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//a[@href='/dashboard']").send_keys(Keys.PAGE_DOWN)
    # time.sleep(0.5)

    # Clicking on Test Dropdown for selecting Test
    if context.driver.find_element(By.ID, "patient-test").is_displayed():
        context.driver.find_element(By.ID, "patient-test").click()
        print("Clicked on Test Dropdown")
    else:
        print("Not able to click on Test Dropdown")
    time.sleep(0.5)

    # Selecting Test from Dropdown
    if context.driver.find_element(By.XPATH, "//div[text()='VITAMIN B12, SERUM']").is_displayed():
        context.driver.find_element(By.XPATH, "//div[text()='VITAMIN B12, SERUM']").click()
        print("Clicked on Test Dropdown")
    else:
        print("Not able to click on Test Dropdown")
    time.sleep(0.5)

    # context.driver.find_element(By.ID, "patient-test").click()
    #
    # if context.driver.find_element(By.XPATH, "//div[text()='CEA, SERUM (Roche e411)']").is_displayed():
    #     context.driver.find_element(By.XPATH, "//div[text()='CEA, SERUM (Roche e411)']").click()
    #     print("Clicked on Test Dropdown")
    # else:
    #     print("Not able to click on Test Dropdown")

    print("When User selects its desired tests under Test Cost Calculator")


@then(u'User should be able to select desired test under Test Cost Calculator')
def step_impl(context):
    print("Then User should be able to select desired test under Test Cost Calculator")


@when(u'User clicks on Discount dropdown')
def step_impl(context):
    # Clicking on Discount Dropdown
    if context.driver.find_element(By.XPATH, "//div[@aria-haspopup='listbox']").is_displayed():
        context.driver.find_element(By.XPATH, "//div[@aria-haspopup='listbox']").click()
        print("Clicked on Discount Dropdown")
    else:
        print("Not able to click on Discount Dropdown")
    time.sleep(0.5)

    print("When User clicks on Discount dropdown")


@then(u'User should be able to select discount from dropdown which are applicable')
def step_impl(context):
    # Selecting applicable Discount from Dropdown
    if context.driver.find_element(By.XPATH, "//li[@data-value='15']").is_displayed():
        context.driver.find_element(By.XPATH, "//li[@data-value='15']").click()
        print("Clicked on Discount Option from Dropdown")
    else:
        print("Not able to click on Discount Option from Dropdown")
    time.sleep(0.5)

    print("Then User should be able to select discount from dropdown which are applicable")


# ------------- Scenario 4 -------------
@when(u'User clicks on Patients tab')
def step_impl(context):
    # Clicking on Patients tab
    context.driver.find_element(By.XPATH, "//a[@href='/patients']").click()
    time.sleep(0.5)

    print("When User clicks on Patients tab")


@then(u'User navigates to Patients page')
def step_impl(context):
    print("Then User navigates to Patients page")


@when(u'User clicks on Add Patient button')
def step_impl(context):
    # Clicking on Add Patient + button
    if context.driver.find_element(By.XPATH, "//a[@href='/patients/add']").is_displayed():
        context.driver.find_element(By.XPATH, "//a[@href='/patients/add']").click()
        print("Clicked on Add Patient button")
    else:
        print("Not able to click on Add Patient button")
    time.sleep(0.5)

    print("When User clicks on Add Patient button")


@then(u'User navigates to Add Patient form page')
def step_impl(context):
    print("Then User navigates to Add Patient form page")


@when(u'User enters all the required details in Patient Contact Details')
def step_impl(context):
    # Entering Patient Name
    context.driver.find_element(By.NAME, "name").send_keys("Patient " + patient_name_generator())
    # time.sleep(0.5)
    # Entering Patient Email ID
    context.driver.find_element(By.NAME, "email").send_keys(patient_email_generator() + "@gor.com")
    # time.sleep(0.5)
    # Entering Patient Phone Number
    context.driver.find_element(By.NAME, "phone").send_keys([patient_phone_number_generator()])
    # time.sleep(0.5)

    print("When User enters all the required details in Patient Contact Details")

    PatientName = context.driver.find_element(By.NAME, "name").get_attribute('value')
    # open the file for write operation
    f = open('store_data.txt', 'w')
    # writes the new content
    f.write(PatientName)
    # close the file
    f.close()
    # again open the file for read
    f = open('store_data.txt', 'r')
    # reads the file content
    f.read()
    # close the file
    f.close()


@when(u'User successfully enters all the required details in Patient Contact Details')
def step_impl(context):
    print("And User successfully enters all the required details in Patient Contact Details")


@then(u'User clicks on General Details button to move on next page of the form')
def step_impl(context):
    # Clicking on General Details button
    context.driver.find_element(By.XPATH, "//button//span[text()='General Details']").click()
    time.sleep(0.5)

    print("Then User clicks on General Details button to move on next page of the form")


@when(u'User moves to the next page of the form to fill required details in General Details')
def step_impl(context):
    # Entering Patient Height
    context.driver.find_element(By.NAME, "height").send_keys("175")
    # time.sleep(0.5)
    # Entering Patient Weight
    context.driver.find_element(By.NAME, "weight").send_keys("65")
    # time.sleep(0.5)
    # Clicking on Gender Dropdown
    context.driver.find_element(By.ID, "mui-component-select-gender").click()
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, "//li[@data-value='male']").click()
    time.sleep(0.5)
    # Entering Patient Age
    context.driver.find_element(By.NAME, "age").send_keys("25")
    # time.sleep(0.5)

    # Entering Blood Pressure Details - SYSTOLIC mm Hg
    context.driver.find_element(By.NAME, "systolic").send_keys("110")
    # time.sleep(0.5)
    # Entering Blood Pressure Details - DIASTOLIC mm Hg
    context.driver.find_element(By.NAME, "diastolic").send_keys("70")
    # time.sleep(0.5)

    print("When User moves to the next page of the form to fill required details in General Details")


@when(u'User successfully enters all the required details in General Details or Secondary Details')
def step_impl(context):
    print("And User successfully enters all the required details in General Details or Secondary Details")


@then(u'User clicks on Add Tests button to move on next page of the form')
def step_impl(context):
    # Clicking on Add Tests button
    context.driver.find_element(By.XPATH, "//button//span[text()='Add Tests']").click()
    time.sleep(0.5)

    print("Then User clicks on Add Tests button to move on next page of the form")


@when(u'User moves to the next page of the form to fill required details in Test Cost Calculator')
def step_impl(context):
    # Clicking on Test Dropdown for selecting Test
    if context.driver.find_element(By.ID, "patient-test").is_displayed():
        context.driver.find_element(By.ID, "patient-test").click()
        print("Clicked on Test Dropdown")
    else:
        print("Not able to click on Test Dropdown")
    time.sleep(0.5)

    # Selecting Test from Dropdown
    if context.driver.find_element(By.XPATH, "//div[text()='VITAMIN B12, SERUM']").is_displayed():
        context.driver.find_element(By.XPATH, "//div[text()='VITAMIN B12, SERUM']").click()
        print("Clicked on Test Dropdown")
    else:
        print("Not able to click on Test Dropdown")
    time.sleep(0.5)

    # Clicking on Discount Dropdown
    context.driver.find_element(By.XPATH, "(//div[@aria-haspopup='listbox'])[1]").click()
    time.sleep(0.5)
    # Selecting applicable Discount from Dropdown
    context.driver.find_element(By.XPATH, "//li[@data-value='10']").click()
    time.sleep(0.5)

    # Clicking on Select Labs from recommendation dropdown
    context.driver.find_element(By.ID, "patient-tests-labs").click()
    time.sleep(0.5)
    # Selecting option from Dropdown
    context.driver.find_element(By.ID, "patient-tests-labs-option-0").click()
    time.sleep(0.5)

    # Clicking on Doctor who recommended this test dropdown
    context.driver.find_element(By.NAME, "doctor_name").click()
    time.sleep(0.5)
    # Selecting option from Dropdown
    context.driver.find_element(By.XPATH, "//li[@data-option-index='0']").click()
    time.sleep(0.5)

    # Clicking on Doctor's Commission Dropdown
    context.driver.find_element(By.XPATH, "(//div[@aria-haspopup='listbox'])[2]").click()
    time.sleep(0.5)
    # Selecting Doctor's Commission from Dropdown
    context.driver.find_element(By.XPATH, "//li[@data-value='10']").click()
    time.sleep(0.5)

    context.driver.find_element(By.XPATH, "//a[@href='/dashboard']").send_keys(Keys.PAGE_DOWN)

    time.sleep(1)

    # Clicking on Add Equipment button
    context.driver.find_element(By.XPATH, "//button[@title='Add equipment']").click()

    # Clicking on Equipment Name dropdown
    context.driver.find_element(By.XPATH, "//div[@aria-label='Eqipment Name']").click()
    time.sleep(0.5)

    # Selecting option from Equipment Name dropdown
    context.driver.find_element(By.XPATH, "//li[@tabindex='0']").click()
    time.sleep(0.5)

    # Clicking on Check Icon or Tick Mark Icon
    context.driver.find_element(By.XPATH, "//span[text()='check']").click()
    time.sleep(0.5)

    print("When User moves to the next page of the form to fill required details in Test Cost Calculator")


@when(u'User successfully enters all the required details in Test Cost Calculator')
def step_impl(context):
    print("And User successfully enters all the required details in Test Cost Calculator")


@then(u'User clicks on Add Patient button')
def step_impl(context):
    # Clicking on Add Patient button
    context.driver.find_element(By.XPATH, "//button//span[text()='Add Patient']").click()
    # time.sleep(10)

    print("Then User clicks on Add Patient button")


@when(u'After adding a test it will be reflected in the list of todos on the home page')
def step_impl(context):
    element = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Patients']"))
    )
    time.sleep(1)

    print("When After adding a test it will be reflected in the list of todos on the home page")


@then(u'Validating that test is added in the list of todos on the home page')
def step_impl(context):
    # Click on Dashboard tab
    context.driver.find_element(By.XPATH, "//span[text()='Dashboard']").click()
    time.sleep(1)

    # Validating Patient Name on Home Page of the application from store_data.txt file
    # open the file for read
    f = open('store_data.txt', 'r')
    # reads the file content
    PatientName = f.read()

    # Retrieving text from Application
    PatientName_from_Web = context.driver.find_elements(By.XPATH, "//li//div[@tabindex='0']//span")

    for i in PatientName_from_Web:
        if PatientName in i.text:
            print(PatientName)
            print(i.text)
            assert True, "New Patient added and reflected on Home Page"
        else:
            print(PatientName)
            print(i.text)
            print("New Patient not added and not reflected on Home Page")
            continue

    # close the file
    f.close()

    print("Then Validating that test is added in the list of todos on the home page")
