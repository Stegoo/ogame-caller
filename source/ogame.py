import requests
import json
from bs4 import BeautifulSoup

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

    def fetch_resources(self, planet_id):
        res = self.session.get(self.get_url('fetchResources')).content
        obj = {}
        try:
            str_response = res.decode('utf-8')
            obj = json.loads(str_response)
        except ValueError as e:
            print("NOT LOGGED")
            self.login()
        return obj

    def get_resources(self, planet_id):
        resources = self.fetch_resources(planet_id)
        metal = resources['metal']['resources']['actual']
        crystal = resources['crystal']['resources']['actual']
        deuterium = resources['deuterium']['resources']['actual']
        energy = resources['energy']['resources']['actual']
        darkmatter = resources['darkmatter']['resources']['actual']
        result = {'metal': metal, 'crystal': crystal, 'deuterium': deuterium,
                  'energy': energy, 'darkmatter': darkmatter}
        return result

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

    def send_fleet(self, planet_id, ships, speed, where, mission, resources):
        def get_hidden_fields(html):
            soup = BeautifulSoup(html)
            inputs = soup.findAll('input', {'type': 'hidden'})
            fields = {}
            for input in inputs:
                name = input.get('name')
                value = input.get('value')
                fields[name] = value
            return fields

        url = self.get_url('fleet1', planet_id)

        res = self.session.get(url).content
        payload = {}
        payload.update(get_hidden_fields(res))
        for name, value in ships:
            payload['am%s' % name] = value
        res = self.session.post(self.get_url('fleet2'), data=payload).content

        payload = {}
        payload.update(get_hidden_fields(res))
        payload.update({'speed': speed,
                        'galaxy': where.get('galaxy'),
                        'system': where.get('system'),
                        'position': where.get('position')})
        res = self.session.post(self.get_url('fleet3'), data=payload).content

        payload = {}
        payload.update(get_hidden_fields(res))
        payload.update({'crystal': resources.get('crystal'),
                        'deuterium': resources.get('deuterium'),
                        'metal': resources.get('metal'),
                        'mission': mission})
        res = self.session.post(self.get_url('movement'), data=payload).content
