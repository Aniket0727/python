import os
import requests
from bs4 import BeautifulSoup
import csv
import time

# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# Specify the file path for the CSV file
csv_file_path = os.path.abspath("C:/pd_data/python/extended_amazon_products.csv")
# Check if the file exists and delete it if it does
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Existing file '{csv_file_path}' deleted.")
# Open the original CSV file for reading
with open("amazon_products.csv", "r", newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    
    
    # Open a new CSV file for writing the extended data
    with open("extended_amazon_products.csv", "w", newline="", encoding="utf-8") as extended_csv_file:
        csv_writer = csv.writer(extended_csv_file)
        
        # Write headers to the new CSV
        csv_writer.writerow(["Product URL", "Description", "Product Description", "Manufacturer","ASIN"])
        
        # Loop through each row in the original CSV
        i=1
        for row in csv_reader:
            des="";manufacturer="";asin="";pd_final="";
            product_url = row[0]  # Get the product URL
            
            if product_url == "N/A":
                # If URL is N/A, write all values as N/A and move to the next row
                csv_writer.writerow(["N/A", "N/A", "N/A", "N/A", "N/A"])
                continue
            
            # Fetch the product page
            response = requests.get(product_url, headers=headers)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                products = soup.find_all("div", class_="celwidget")
                for product in products:
                    
                    
                    description_tag = product.find("div", class_="a-section a-spacing-medium a-spacing-top-small", id="feature-bullets")
                    if description_tag:
                        description_list = description_tag.find("ul", class_="a-unordered-list a-vertical a-spacing-mini")
                        if description_list:
                            description_items = description_list.find_all("li")
                            for item in description_items:
                                des=item.get_text().strip()
                                #print(item.get_text().strip())
                        
                    ASIN_tag = product.find("div", class_="a-section feature detail-bullets-wrapper bucket")
                    if ASIN_tag:
                        ASIN_tag_list = ASIN_tag.find("ul", class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list")
                        if ASIN_tag_list:
                            ASIN_items = ASIN_tag_list.find_all("li")
                            for item in ASIN_items:
                                item_list = item.get_text().split(':')
                                cleaned_list = [item5.replace('\u200f\n', '').replace('\n', '') for item5 in item_list]

                                item_list1=cleaned_list[0].strip()
                                item_list2=cleaned_list[1].strip()
                                if item_list1.lower().startswith("manufacturer"):
                                    manufacturer=item_list2.replace("â€Ž","")
                                    #print(manufacturer)
                                
                                if item_list1.lower().startswith("asin"):
                                    asin=item_list2.replace("â€Ž","")
                                    #print(asin)
                                
                                
                    pd = product.find("div", class_="a-row feature")
                    if pd:
                        pd2 = pd.find("div", class_="a-section a-spacing-small")
                        if pd2:
                            pd_final=pd2.get_text().strip()
                            #print(pd_final)
                        
                
                            
             
                
                # Write the extended information to the new CSV
                csv_writer.writerow([product_url,des,pd_final,manufacturer,asin])
                
                print(f"Processed of Product {i}: {product_url}")
            else:
                print(f"Failed to fetch: {product_url}. Status code: {response.status_code}")
            i=i+1

print("Extended scraping completed and data exported to extended_amazon_products.csv")
