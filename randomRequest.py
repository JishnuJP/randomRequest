from random import choice

proxy_type = ['elite','anonymous','transparent']
with open('useragents.txt') as f:
    agents = [line.rstrip() for line in f]

class randomRequest():
	def __init__(self,**kwargs):
		# expected arguments = > header, proxy, User-Agent 
		self.head = {}
		for key, value in kwargs.items():
			if key =='header' :
				self.head = value
			elif key == 'proxy':
				if type(value)==list:
					self.proxy = value
				elif type(value) == str:
					if value in proxy_type:
						self.proxy = self.getProxy(value)
					else:
						raise Exception('''{} is not a valid proxy_type, 
							Try ({})'''.format(value,proxy_type))
				else:
					raise TypeError('proxy should be list or str, not ',type(value))

			elif key == 'UserAgent':
				if value == 'random':
					self.head['User-Agent'] = self.getUserAgent()
				else:
					self.head['User-Agent'] = value

			else:
				raise Exception('''Invalid parameter - {},
				 accepted parameters are proxy, UserAgent ,header,{},'''.format(value,proxy_type))

	def getProxy(self,value):
		if value not in proxy_type:
			raise Exception('''{} is not a valid proxy_type, 
							Try ({})'''.format(value,proxy_type))
			return
		# random selection of proxy
		return 'random_proxy'
	def getUserAgent(self):
		#include some paramets that can filter the random selection of useragent
		return choice(agents)





if __name__ == '__main__':
	'''url = 'https://httpbin.org/ip'
				response = requeste.get(url,randomRequest())
				print(response.json())'''
	print(randomRequest(UserAgent = 'random').head)
	print(randomRequest(proxy = 'elite').proxy)
