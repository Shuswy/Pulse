import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from decimal import Decimal
import re

class ScraperService:

    @staticmethod
    def scrape_target(target):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        try:
            response = requests.get(target.url, headers=headers, timeout=15)
            response.raise_for_status()

            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            element = soup.select_one(target.css_selector)

            if not element:
                raise ValueError(f"Selector '{target.css_selector}' not found on page.")

            raw_price = element.get_text(strip=True)
            clean_price = re.sub(r'[^\d.]', '', raw_price)

            return {
                "price": Decimal(clean_price),
                "raw_html": html_content
            }
        except Exception as e:
            print(f"Scrape failed for {target.name}: {str(e)}")
            return None