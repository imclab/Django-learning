__author__ = 'pedro'

from django.db import models
from bs4 import BeautifulSoup
import requests
import bleach


class Verbix():
    service_name = "verbix"
    baseUrl = "http://www.verbix.com/webverbix/"
    language = "Finnish"
    allowed_tags = ['class', 'td', 'tr', 'table', 'p', 'br', 'b', 'th']
    allowed_attr = {
        'table': ['class']
    }

    def __init__(self, verb):
        """
        Constructor of the class
        """
        self.verb = verb
        self.url = self.baseUrl + self.language + "/" + verb + ".html"

    def get_conjugations(self):
        """
        Return verb conjugations
        """
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
        if self.is_a_verb(soup):
            tables = soup.find_all("table", class_="verbtable")
            # We take the first table tables[0] since is the one with all needed information
            sections = tables[0].find_all('tr')  # We look inside for 'tr' tags
            # We look first for Personal and Nominal forms, they are in sections[2]
            # inside 2 'td' tags and inside a table each
            tr_block = sections[2].find_all('td', class_="verbtable")
            for td in tr_block:
                table = td.find('table')
                table['class'] = 'table'  # add class="table" to the table tag for CSS purposes
                results.append(bleach.clean(table, self.allowed_tags, self.allowed_attr, strip=True))
                # Now we have in results 0 and 1 the first tables
            # Next is same for the other two blocks
            # They are inside sections 14, to see why, debug and check values on sections values
            tr_block = sections[14].find_all('td', class_="verbtable")
            for td in tr_block:
                table = td.find('table')
                table['class'] = 'table'  # add class="table" to the table tag for CSS purposes
                results.append(bleach.clean(table, self.allowed_tags, self.allowed_attr, strip=True))

        return results

    def is_a_verb(self, html):
        """
        Given an html output will look for verbnotexits class
        returning False if is it NOT a verb, other wise True
        """
        results = html.find_all('div', class_="verbnotexist")
        if not results:
            return True
        else:
            return False

    def parse_to_json(self):
        """
        Given a table, parse it into a JSON form
        """
        # http://stackoverflow.com/questions/18544634/convert-a-html-table-to-json

    def __unicode__(self):
        return self.service_name