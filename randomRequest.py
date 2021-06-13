import requests
import json
from random import choice



class randomAgent:
	def __init__(self,**kwargs):
		with open('useragents.txt') as f:
		    self.agents = [line.rstrip() for line in f]		
		for key, value in kwargs.items():
			if key == 'Browser':
				[self.agents.remove(agent) for agent in self.agents if value not in agent]
			## possibility of an exception when the value of 'Browser' is not matching
	def getRandomAgent(self):
		return choice(self.agents)





class randomProxy:
	def __init__(self,**kwargs):
		self.url = 'https://www.proxy-list.download/api/v1/get'
		self.types = ['http','https','socks4','socks5']
		self.anons = ['transparent','anonymous','elite']
		for key, value in kwargs.items():
			if key == 'Type':
				if value in self.types:
					self.url = self.url + f'?type={value}'
				else:
					raise TypeError(f'''{Type} is Invalid protocol, 
						Valid protocols are {self.types}''')		
			elif key =='Anon':		
				if value in self.anons:
					self.url = self.url+ f'&anon={Anon}'
				else:
					pass
			elif key == 'Country':
				validity,self.code = self.getCodes(value)
				if validity:
					self.url = self.url +f'&country={self.code}'
				else:
					pass

		response = requests.get(self.url)
		if response.status_code != 200:
			raise Exception(f'Request Failed url is : {self.url}')
		self.proxies = response.content.decode('utf-8')
		self.proxies = self.proxies.split('\r\n')
		self.proxies.remove('')

	def getCodes(self, Country):
		with open('country_codes.json') as f:
			country_codes = json.load(f)
		if Country == None:
			return False, None
		for i in country_codes:
			if Country.upper() in i.upper():
				return True,country_codes[i]
	def getRandomProxy(self):
		return choice(self.proxies)




class randomRequest(randomAgent, randomProxy):
	def __init__(self,**kwargs):
		# expected arguments = > header, proxy, User-Agent 
		#super().__init__(**kwargs)
		randomAgent.__init__(self,**kwargs)
		randomProxy.__init__(self,**kwargs)
		self.head = {}
		for key, value in kwargs.items():
			if key =='header' :
				self.head = value
			elif key == 'proxy':
				if type(value)==list:
					self.proxies = value
				elif type(value) == str:
					self.proxies = [value]
				else:
					raise TypeError(f'{type(value)} is not acceptable, give list or string') 
			
				
	def verifty(self, headers, proxies):
		try:
			resp  = requests.get('https://httpbin.org/get',headers = headers, proxies = proxies)
		except:
			return False
		if resp.status_code == 200:
			return True
		else:
			 return False




if __name__ == '__main__':
	randReq = randomRequest(Type = 'https')
	agent = randReq.getRandomAgent()
	proxy = randReq.getRandomProxy()
	print(f'Agent : \n {agent} \n Proxy: \n {proxy}')
	if randReq.verifty(headers = {'User-Agent':agent},proxies = {'https':proxy}):
		print('Request is Valid')
	else:
		print('Request is Invalid')