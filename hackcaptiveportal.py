import requests
from bs4 import BeautifulSoup
import subprocess


# Assuming 'html_content' contains the HTML content of the webpage
# soup = BeautifulSoup(html_content, 'html.parser')

# Find the first input tag in the HTML
# input_tag = soup.find('input')

CAPTIVE_URL = ""



def is_internet_available():
    try:
        # Use the 'ping' command to check connectivity to Google (8.8.8.8 is Google's DNS server)
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5, shell=True)
        
        if result.returncode == 0:
            return True  # Ping was successful, indicating an internet connection
        else:
            return False  # Ping failed, indicating no internet connection

    except subprocess.CalledProcessError:
        return False  # Ping failed, indicating no internet connection
    except subprocess.TimeoutExpired:
        return False  # Ping timed out, indicating no internet connection

if is_internet_available():
    print("Internet connection is available.")
else:
    print("No internet connection.")
