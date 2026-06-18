# Import the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"


# launch browser and open target website
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
# driver.maximize_window()


# Lists to store scrape laptop information
names = []
processors = []
rams = []
ssds = []
systems = []
displays = []
prices = []


# Iterate through multiple pages and collect laptop data
for page in range(2):
    print(f"Scraping Page {page+1} ")
    
    product_cards = driver.find_elements(By.CLASS_NAME, value="jIjQ8S")
    
    
    # Extract laptop specification from each product card
    for card in product_cards:
        try:
            name = card.find_element(By.CLASS_NAME, value="RG5Slk").text
        except:
            name = None
        names.append(name)
       
       
        
        # Handle missing specification to mantain data consistency
        try:
            processor = card.find_element(By.XPATH, value='.//li[@class="DTBslk" and contains(text(), "Processor")]').text
        except:
            processor=None
        processors.append(processor)
        
        
        
        try:
            ram = card.find_element(By.XPATH, value='.//li[@class="DTBslk" and contains(text(), "RAM")]').text
        except:
            ram = None
        rams.append(ram)
        
        
        
        try:
            ssd = card.find_element(By.XPATH, value='.//li[@class="DTBslk" and contains(text(), "SSD")]').text
        except:
            ssd = None
        ssds.append(ssd)
       
        
        
        try:
            system = card.find_element(By.XPATH, value='.//li[@class="DTBslk" and contains(text(), "System")]').text
        except:
            system = None
        systems.append(system)     
       
        
        
        try:
            display = card.find_element(By.XPATH, value='.//li[@class="DTBslk" and contains(text(), "Display")]').text
        except:
            display = None
        displays.append(display)
        
        
        
        try:
            price = card.find_element(By.CSS_SELECTOR, value=".hZ3P6w.DeU9vF").text
        except:
            price = None
        prices.append(price)
        
      
    
    # Navigate to next the page
    next_button = driver.find_element(By.CLASS_NAME, value="jgg0SZ")
    
    
    # Scroll to button
    driver.execute_script("arguments[0].scrollIntoView();", next_button)
    time.sleep(1)

    # Click safely
    driver.execute_script("arguments[0].click();", next_button)
    time.sleep(5)


# Store the extracted data lists in a dictionary form
data = {
    "Name":names,
    "Price":prices,
    "Ram":rams,
    "System":systems,
    "SSD":ssds,
    "Processor":processors,
    "Display":displays
}



# Make a dataframe from a dictionary 
df = pd.DataFrame(data)



# Save the dataframe as a csv file
df.to_csv("Data/raw_data.csv", index=False)


# Close the browser
driver.quit()

print(f"Total Records Collected : {len(df)}")
        
        
        