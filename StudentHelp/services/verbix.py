__author__ = 'pedro'

from django.db import models
from bs4 import BeautifulSoup
import requests


class Verbix(models.Model):
    service_name = "verbix"
    verb = ""
    baseUrl = "http://www.verbix.com/webverbix/"
    language = "Finnish"

    def get_conjugations(self, verb):
        """
        Constructor of the class
        """
        self.verb = verb
        url = self.baseUrl + self.language + "/" + verb + ".html"
        return self.parse_html(self.get_html(url))

    def get_html(self, url):
        """
        Get the whole HTML response from the service.
        Make it ready to be parsed
        """
        html = requests.get(url)
        return html.text

    def parse_html(self, html):
        """
        Given an HTML code parse it and retrieve the results
        """
        soup = BeautifulSoup(html)
        print(soup)
        tables = soup.find_all("table", class_="verbtable")
        return tables[0]

    def __unicode__(self):
        return self.service_name