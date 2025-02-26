import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# URL for men’s sneakers, size 10 (may need adjustment)
url = "https://www.macys.com/shop/mens-clothing/shop-all-mens-shoes/mens-sneakers?id=55642"

# Headers to avoid being blocked
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all sneaker products
    # Save the HTML content first
    with open('macys_page.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    # Try different common product container classes
    # First find all product containers
    sneakers = soup.find_all("div", class_="product-description")
    # Filter for only sneakers
    # sneakers = [item for item in sneakers if "sneakers" in item.text.lower() or "shoes" in item.text.lower()]
    sneaker_data = []
    
    for sneaker in sneakers:
        # Get name
        name = sneaker.find("div", class_="product-name")
        name_text = name.text.strip() if name else "Unknown Sneaker"
        
        # Get price
        price = sneaker.find("div", class_="pricing")
        price_text = price.text.strip() if price else "Price not found"
        
        # Store data in lists
        sneaker_data.append([name_text, price_text])
    
    if sneaker_data:
        try:
            headers = ["Sneaker Name", "Price"]
            print("\n" + tabulate(sneaker_data, headers=headers, tablefmt="grid"))
        except ImportError:
            # Fallback if tabulate is not installed
            print("\n{:<50} {:<20}".format("Sneaker Name", "Price"))
            # print("-" * 70)
            for data in sneaker_data:
                print("{:<50} {:<20}".format(data[0], data[1]))
else:
    print(f"Failed to load. Status code: {response.status_code}")