from selenium import webdriver
import time

geckodriver_path = r"C:\Users\anous\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe"

#
firefox_options = webdriver.FirefoxOptions()


from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_element_present(driver, by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False


url = 'https://www.amazon.in/American-Tourister-AMT-SCH-02/product-reviews/B07CJCGM1M/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'


def pagescraping(driver, stars, titles, reviews):

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    review_boxes = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.review.aok-relative[data-hook="review"]')
    for review_box in review_boxes:
        star1 = review_box.find_element(By.CSS_SELECTOR, 'div.a-row i span.a-icon-alt')
        star=star1.get_attribute('outerHTML')[25:26]
        title_row = review_box.find_elements(By.CSS_SELECTOR, 'div.a-row')[2]
        title = title_row.find_elements(By.TAG_NAME, 'span')[-1].text
        review_text = review_box.find_element(By.CSS_SELECTOR, 'span.a-size-base.review-text.review-text-content').text
        stars.append(star)
        titles.append(title)
        reviews.append(review_text)

# Example usage:
stars = []
titles = []
reviews = []

def tenpagescarper(driver, stars, titles, reviews):
    for x in range(10):
        time.sleep(5)
        pagescraping(driver, stars, titles, reviews)

        if is_element_present(driver, By.XPATH, r'//ul[@class="a-pagination"]/li[@class="a-last"]/a'):
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, r'//ul[@class="a-pagination"]/li[@class="a-last"]/a')))

            # Scroll to the button to bring it into view
            driver.execute_script("arguments[0].scrollIntoView(true);", button)

            # Wait until the button is visible and clickable
            WebDriverWait(driver, 20).until(
                EC.visibility_of(button)
            )

            # Click the button
            button.click()

            login_email_present = is_element_present(driver, By.XPATH, r'//input[@id="ap_email"]')
            if login_email_present:
                login_email = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, r'//input[@id="ap_email"]'))
                )
                login_email.send_keys("anoushkagarg003@gmail.com")
                continue_btn = driver.find_element(By.XPATH, r'//input[@id="continue"]')
                continue_btn.click()
                login_password = driver.find_element(By.XPATH, r'//input[@id="ap_password"]')
                login_password.send_keys("abeer1234")
                submit_btn = driver.find_element(By.XPATH, r'//input[@id="signInSubmit"]')
                submit_btn.click()
def scraping(link):
    driver = webdriver.Firefox()
    driver.get(link)
    tenpagescarper(driver, stars, titles, reviews)
    _5starlink= driver.find_element(By.XPATH, '//a[@class="a-link-normal 5star"]')
    _5starlink.click()
    tenpagescarper(driver, stars, titles, reviews)
    _4starlink= driver.find_element(By.XPATH, '//a[@class="a-link-normal 4star"]')
    _4starlink.click()
    tenpagescarper(driver, stars, titles, reviews)
    _3starlink = driver.find_element(By.XPATH, '//a[@class="a-link-normal 3star"]')
    _3starlink.click()
    tenpagescarper(driver, stars, titles, reviews)
    _2starlink = driver.find_element(By.XPATH, '//a[@class="a-link-normal 2star"]')
    _2starlink.click()
    tenpagescarper(driver, stars, titles, reviews)
    _1starlink = driver.find_element(By.XPATH, '//a[@class="a-link-normal 1star"]')
    _1starlink.click()
    tenpagescarper(driver, stars, titles, reviews)
    driver.quit()


links=['https://www.amazon.in/American-Tourister-AMT-SCH-02/product-reviews/B07CJCGM1M/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/FATMUG-Laptop-Bag-Men-Convertible/product-reviews/B084LF4RT5/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/ADISA-BP004-Weight-Casual-Backpack/product-reviews/B07G3CG9FC/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/Arctic-Fox-Backpack-Charging-Laptop/product-reviews/B089QB6D7B/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/ELECTRONIC-PORTABLE-DIGITAL-LUGGAGE-WEIGHING/product-reviews/B07PK41FL4/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/WildHorn%C2%AE-Protected-Genuine-Quality-Leather/product-reviews/B07QBQ127Y/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/GoTrippin-Machine-Luggage-Weighing-Portable/product-reviews/B07Q822CWX/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/MEDLER-Nylon-Expandable-Duffel-Trolley/product-reviews/B07MWD4D4W/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/Skybags-Trooper-Hardsided-Spinner-Suitcase/product-reviews/B0C8ZFXCB6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/WildHorn-Brown-Wallet-WH2052-Crackle/product-reviews/B07C3VH84K/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/Storite-Vertical-Leather-Card-Holder/product-reviews/B082SKY3CT/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/Nivia-6853-Polyester-Basic-Duffle/product-reviews/B07FWQ9HRV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/Billebon-Neck-Pillow-Eye-Mask/product-reviews/B083YXBDZ3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
       'https://www.amazon.in/ShineXPro-Microfiber-Car-Cleaning-Cloth/product-reviews/B09RWTYMCF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
]
for link in links:
    scraping(link)
print(len(stars))
print(len(titles))
print(len(reviews))

import pandas as pd
df = pd.DataFrame({'Stars': stars, 'Titles': titles, 'Reviews': reviews})
# Save the DataFrame to a CSV file with headers
df.to_csv('output_new.csv', index=False, header=True)
