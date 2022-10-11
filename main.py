import requests
import re

from requests import Session
from bs4 import BeautifulSoup

class Crawly:
    
    def __init__(self) -> None:
        super().__init__()
        self.url = 'http://applicant-test.us-east-1.elasticbeanstalk.com/'
        self.token = None
        self.answer = None
        self.s = None
        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://applicant-test.us-east-1.elasticbeanstalk.com',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'http://applicant-test.us-east-1.elasticbeanstalk.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    
    def get_session(self):
        self.s = Session()
        self.s.headers.update(self.headers)
        return self.s.get(self.url, allow_redirects=True)
        
    def get_token(self):
        init_page = self.get_session()
        soup = BeautifulSoup(init_page.content, 'html.parser')
        self.token = soup.find('input', {'name': 'token'})['value']
        if self.token:
            return 'Token found'
        else:
            raise Exception('Token not found')
    
    def replace_function(self):
        replacements = {
                'a': '\x7a',
                'b': '\x79',
                'c': '\x78',
                'd': '\x77',
                'e': '\x76',
                'f': '\x75',
                'g': '\x74',
                'h': '\x73',
                'i': '\x72',
                'j': '\x71',
                'k': '\x70',
                'l': '\x6f',
                'm': '\x6e',
                'n': '\x6d',
                'o': '\x6c',
                'p': '\x6b',
                'q': '\x6a',
                'r': '\x69',
                's': '\x68',
                't': '\x67',
                'u': '\x66',
                'v': '\x65',
                'w': '\x64',
                'x': '\x63',
                'y': '\x62',
                'z': '\x61',
                '0': '\x39',
                '1': '\x38',
                '2': '\x37',
                '3': '\x36',
                '4': '\x35',
                '5': '\x34',
                '6': '\x33',
                '7': '\x32',
                '8': '\x31',
                '9': '\x30'
            }
        token = [re.sub(r'\b\w+\b', lambda m: replacements.get(m.group(), m.group()), s) for s in self.token]
        return ''.join(token)
    
    def get_answer(self):
        self.get_token()
        if self.token:
            token = self.replace_function()
            cookie = {'PHPSESSID': requests.utils.dict_from_cookiejar(self.s.cookies)['PHPSESSID']}
            answer_page = self.s.post('http://applicant-test.us-east-1.elasticbeanstalk.com/', data={'token': token}, allow_redirects=True, cookies=cookie)
            soup = BeautifulSoup(answer_page.content, 'html.parser')
            self.answer = soup.find(attrs={"id" : "answer"}).text
            if self.answer:
                return f'A resposta do desafio é: {self.answer}'
            else:
                raise Exception('Answer not found')
        else:
            raise Exception('Token not found')

crawly = Crawly()
print(crawly.get_answer())