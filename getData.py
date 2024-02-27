import os
import requests
from bs4 import BeautifulSoup
import csv
import time

# Define the base URL
base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"

# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# Specify the file path for the CSV file
csv_file_path = os.path.abspath("F:/amazon_products.csv")

# Check if the file exists and delete it if it does
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Existing file '{csv_file_path}' deleted.")
# Open a CSV file for writing
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write headers to CSV
    csv_writer.writerow(["Product URL", "Product Name", "Product Price", "Rating", "Number of Reviews"])

    # Loop through at least 20 pages
    for page_num in range(1, 31):
        url = base_url + str(page_num)
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            products = soup.find_all("div", class_="s-result-item")

            for product in products:
                
                product_url_tag = product.find("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
                if product_url_tag:
                    if product_url_tag["href"].startswith("http"):
                        product_url = product_url_tag["href"]
                    else:
                        url_pro = "https://www.amazon.in/" + product_url_tag["href"]
                        product_url = url_pro
                else:
                    product_url = "N/A"

                product_name_tag = product.find("span", class_="a-size-base-plus a-color-base a-text-normal")
                if not product_name_tag:
                    product_name_tag = product.find("span", class_="a-size-medium a-color-base a-text-normal") 

                if product_name_tag:
                    product_name = product_name_tag.text.strip()
                else:
                    product_name = "N/A"

                price_tag = product.find("span", class_="a-price-whole")
                if price_tag:
                    product_price = price_tag.text.strip()
                else:
                    product_price = "N/A"

                rating_tag = product.find("div", class_="a-section a-spacing-none a-spacing-top-micro")
                rating_tag1 = product.find("div", class_="a-section a-spacing-none a-spacing-top-micro faceout-product-review")
                if rating_tag:
                    try:
                        rating = rating_tag.find("span", class_="a-icon-alt").text.split()[0]
                    except AttributeError:
                        rating = "N/A"
                elif rating_tag1:
                    try:
                        rating = rating_tag1.find("span", class_="a-icon-alt").text.split()[0]
                    except AttributeError:
                        rating = "N/A"
                else:
                    rating = "N/A"

                review_count_tag = product.find("span", class_="a-size-base s-underline-text")
                if review_count_tag:
                    review_count = review_count_tag.text.replace(",", "").strip()
                else:
                    review_count = "N/A"

                csv_writer.writerow([product_url, product_name, product_price, rating, review_count])

            print(f"Page {page_num} scraped successfully.")
        else:
            print(f"Failed to fetch page {page_num}. Status code: {response.status_code if response else 'N/A'}")
            if response and response.status_code == 503:
                print("Retrying after a delay...")
                time.sleep(5)  # Wait for 5 seconds before retrying
                response = requests.get(url, headers=headers)  # Retry the request
                if response and response.status_code == 200:
                    print(f"Page {page_num} scraped successfully after retry.")
                else:
                    print(f"Failed again after retry. Status code: {response.status_code if response else 'N/A'}")

print("Scraping completed and data exported to amazon_products.csv")
