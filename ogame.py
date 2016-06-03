from game_constants import Ships, Speed, Missions, Buildings, Research, Defense
from bs4 import BeautifulSoup
import requests
import json


class Ogame(object):
    def __init__(self, universe, login, password, domain='org'):
        self.session = requests.session()
        self.domain = domain
        self.universe = universe
        self.server_url = self.get_base_server_url()
        self.username = login
        self.password = password
        print('server url', self.server_url)
        self.login()


    def login(self):
        """Get the ogame session token."""
        payload = {'kid': '',
           'uni':  self.server_url,
           'login': self.username,
           'pass': self.password}
        res = self.session.post(self.get_url('login'), data=payload).content


    def logout(self):
        self.session.get(self.get_url('logout'))

    def get_base_server_url(self):
        url = 's' + self.universe + '-' + self.domain + '.ogame.gameforge.com'
        return url

    def get_url(self, page, planet=None):
        if page == 'login':
            return "https://fr.ogame.gameforge.com/main/login"
            #return '%s/main/login' % self.server_url
        else:
            url = 'https://%s/game/index.php?page=%s' % (self.server_url, page)
            print("URL", url)
        if planet:
            url += '&cp=%s' % planet
        return url

    def fetch_eventbox(self):
        res = self.session.get(self.get_url('fetchEventbox')).content
        obj = {}
        try:
            str_response = res.decode('utf-8')
            obj = json.loads(str_response)
        except ValueError as e:
            print("NOT LOGGED")
            self.login()
        return obj

    def is_under_attack(self):
        json = self.fetch_eventbox()
        return not json.get('hostile', 0) == 0
