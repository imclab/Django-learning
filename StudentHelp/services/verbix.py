__author__ = 'pedro'

from django.db import models
from bs4 import BeautifulSoup
import requests
import bleach


class Verbix(models.Model):
    service_name = "verbix"
    verb = ""
    baseUrl = "http://www.verbix.com/webverbix/"
    url = ""
    language = "Finnish"
    allowed_tags = ['class', 'td', 'tr', 'table', 'p', 'br', 'b', 'th']

    def get_conjugations(self, verb):
        """
        Constructor of the class
        """
        self.verb = verb
        self.url = self.baseUrl + self.language + "/" + verb + ".html"
        return self.parse_html(self.get_html())

    def get_html(self):
        """
        Get the whole HTML response from the service.
        Make it ready to be parsed
        """
        html = requests.get(self.url)
        return html.text

    def parse_html(self, html):
        """
        Given an HTML code parse it and retrieve the results
        """
        results = []
        soup = BeautifulSoup(html)
        tables = soup.find_all("table", class_="verbtable")
        for table in tables:
            table['class'] = 'table'
            sections = table.find_all('tr')
            for section in sections:
                clean_rows = bleach.clean(section, self.allowed_tags, strip=True)
                results.append(clean_rows)
        return results

    def __unicode__(self):
        return self.service_name