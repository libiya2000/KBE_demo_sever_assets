# -*- coding: utf-8 -*-
import KBEngine
import GlobalDefine
from KBEDebug import *

class SeverData(KBEngine.Base):

	def __init__(self):
		KBEngine.Base.__init__(self)
		
		
		self.Allmoney = 0
		self.addTimer( 3, 10, 0 )
		KBEngine.globalData["SeverData"] = self
	  

	def onTimer( self, id, userArg ):		
		 self.SeverAllMoney += self.Allmoney
		 self.Allmoney = 0
		 DEBUG_MSG("we are had %i Gold" % (self.SeverAllMoney ))

		 		
	def addMoney(self,money):
		self.Allmoney += money
		DEBUG_MSG("we are had add %i Gold,all get %i " % (money,self.Allmoney))
	def onReqGetMoney(self,ID,TYPE):
		pass
	         