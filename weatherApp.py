import xml.etree.ElementTree as ET
import urllib2

class WeatherApp:
	def __init__(self):
		self.getAppid()
		self.output = ['temperature ','conditions ','relative humidity ','wind speed ']
		self.result = {}
		self.url = "http://api.wolframalpha.com/v2/query?input=weather&appid=%s"%self.appid		
		self.getContent()
		self.parseXml()	
		self.printOutput()

	def getAppid(self):
		file = open("appId","r")
		self.appid = file.read()[:-1]
			
	def getContent(self):
		response = urllib2.urlopen(self.url)
		self.xml = response.read()

	def parseXml(self):
		root = ET.fromstring(self.xml)
		for pod in root.findall('pod'):
			self.title =  pod.get('title')
			if self.title == "Latest recorded weather near Kochi, Kerala, India":
				content = pod.find('subpod').find('plaintext')
				self.extractFields(content)
				return

	def extractFields(self,content):
		for line in  content.text.split('\n'):
			split = line.split('|')	
			if split[0] in self.output:
				self.result[split[0]] =  split[1]
		self.location=""
		self.location = self.location.join(line.split()[-3:])
		self.location = self.location.replace(')','')

	def printOutput(self):	
		for key in self.result:
			print key, self.result[key]
		print "Location",self.location


weatherApp = WeatherApp()
