from selenium import webdriver


def before_scenario(context, driver):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://gor-pathology.web.app/")
    context.driver.implicitly_wait(5)
    print(" ------------------ BEFORE SCENARIO ------------------ ")


def after_scenario(context, driver):
    context.driver.quit()
    print(" ------------------ AFTER SCENARIO ------------------ ")
