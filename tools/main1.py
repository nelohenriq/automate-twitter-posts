import os
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()


class BrowserTools:
    def __init__(self):
        self.model_name = os.getenv("SUMMARY_MODEL")
        print(f"Model name from env: {self.model_name}")
        if not self.model_name:
            raise ValueError("SUMMARY_MODEL environment variable is not set.")

        try:
            self.summarizer = pipeline("summarization", model=self.model_name)
        except Exception as e:
            print(f"Error loading the summarization pipeline: {e}")
            self.summarizer = None

    # @tool("Scrape website content")
    def scrape_and_summarize_website(self, url):
        """Scrapes and summarizes the content on the given website. Just pass a string with
        only the full url, without slash `/` at the end, eg: https://google.com or https://clearbit.com/about-us.

        Parameters:
            url (str): website url to be scraped. Cannot be empty or None.
        """
        if not self.summarizer:
            return "Summarizer pipeline is not set up."

        website = url
        html_content = self.fetch_website_html(website)
        if html_content:
            text = self.extract_text(html_content)
            print(f"Number of characters: {len(text)}")
            chunk_size = 1000
            chunks = [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]
            print(f"Number of chunks: {len(chunks)}")

            summaries = []
            for chunk in chunks:
                summary = self.summarizer(
                    chunk, max_length=70, min_length=40, do_sample=False
                )
                summaries.append(summary[0]["summary_text"])

            content = "\n\n".join(summaries)
            print(f"Number of characters: {len(content)}")
            return "Scrapped content: " + content
        else:
            return "Failed to fetch content."

    @staticmethod
    def fetch_website_html(url):
        try:
            response = requests.get(url)
            print(f"Status code: {response.status_code}")
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching the website: {e}")
            return None

    @staticmethod
    def extract_text(html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        text = " ".join(soup.stripped_strings)
        return text


# Usage example
url = "https://www.artificialintelligence-news.com/artificial-intelligence-news/"
browser_tools = BrowserTools()
content = browser_tools.scrape_and_summarize_website(url)
print(content)
