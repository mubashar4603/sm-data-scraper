from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities import googleSheet
from utilities.readProperties import ReadConfig
# Initialize the driver (make sure to replace 'your_webdriver_path')
driver = webdriver.Chrome()

# Open the target URL
driver.get(ReadConfig.getAppURL())
driver.maximize_window()

# Infinite scroll function with dynamic wait
def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")
    # print(last_height)

    while True:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            # Wait until new content loads
            WebDriverWait(driver, 10).until(
                lambda driver: driver.execute_script("return document.body.scrollHeight") > last_height)
        except:
            # Break the loop if no new content is loaded after waiting
            break

        last_height = driver.execute_script("return document.body.scrollHeight")

# Execute the scroll function to load all content
scroll_to_bottom()

# Now locate and scrape the desired elements
elements = driver.find_elements(By.CSS_SELECTOR, 'div.X8m.zDA.IZT.CKL.tBJ.dyH.iFc.j1A.H2s')  # Replace with actual element locator
scrapped = []
# Extract and print data from each element
for element in elements:
    scrapped.append(element.text)
print(scrapped)
print(len(scrapped))


#pass the data to google sheet utility
googleSheet.google_sheet(scrapped)



# Close the driver
driver.quit()
