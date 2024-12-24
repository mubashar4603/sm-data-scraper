from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the driver (make sure to replace 'your_webdriver_path')
driver = webdriver.Chrome()

# Open the target URL
driver.get("https://www.pinterest.com/ideas/")
driver.maximize_window()

# Infinite scroll function to load all content
def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)

    while True:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new data to load
        time.sleep(5)

        # Check if the scroll height has increased
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(new_height)
        if new_height == last_height:
            break
        last_height = new_height


# Execute the scroll function to load all content
scroll_to_bottom()

# Now locate and scrape the desired elements
elements = driver.find_elements(By.CSS_SELECTOR, 'div.X8m.zDA.IZT.CKL.tBJ.dyH.iFc.j1A.H2s')  # Replace with actual element locator

scrappedData = []
# Extract and print data from each element
for element in elements:
    scrappedData.append(element.text)

print(scrappedData)
print(len(scrappedData))
# Close the driver
driver.quit()
