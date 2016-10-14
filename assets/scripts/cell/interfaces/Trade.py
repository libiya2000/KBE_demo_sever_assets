# -*- coding: utf-8 -*-
import KBEngine
import GlobalDefine
import random
from KBEDebug import * 
from Inventory import InventoryMgr


class Trade:
	"""
	关于交易的一些功能
	"""
	def __init__(self):
		#self.TradeItemList ={}
		#self.TradeMoney =0
		#self.TradeTargetID=0
		pass
		
	def reqBeginTrade(self,exposed,TargetID ): #主动交易
		"""
		exposed
		"""
		if self.id != exposed:
			return		
		
		if TargetID==0:
			return
		self.TradeTargetID=TargetID
		self.Tradelock=False
		#self.client.IsTradeing(TargetID)
		#目标实体，客户端和服务器分别通知
		Tar=KBEngine.entities.get(TargetID)
		DEBUG_MSG("testdebug1   BeCallToTrade " )
		Tar.BeCallToTrade(self.id)
		#Tar.client.IsTradeing(self.ENTITY_ID)
		DEBUG_MSG("testdebug2   reqBeginTrade " )

	def BeCallToTrade(self,TargetID ): #被动交易响应
		if TargetID==0:
			return
		self.Tradelock=False
		DEBUG_MSG("testdebug3  BeCallToTrade " )
		self.TradeTargetID=TargetID
		self.client.IsTradeing(TargetID)
		DEBUG_MSG("testdebug4  BeCallToTrade " )
	
		
				
	def reqLockTradeItem(self ,exposed,MyItemList,MyMoney):	
		"""
		exposed
		"""
		if self.id != exposed:
			return	
		
		self.TradeItemList=MyItemList
		self.TradeMoney=MyMoney
		Tar=KBEngine.entities.get(self.TradeTargetID)
		Tar.client.OnreqTradeItemList(MyItemList,MyMoney)
		self.client.OnreqTradeItemList(Tar.TradeItemList,Tar.TradeMoney)
		
	def reqLockTradeItem2(self ,exposed,MyMoney):	
			"""
			exposed
			"""
			if self.id != exposed:
				return	
			
			#self.TradeItemList=MyItemList
			self.TradeMoney=MyMoney
			Tar=KBEngine.entities.get(self.TradeTargetID)
			Tar.client.OnreqTradeItemList2(MyMoney)
			self.client.OnreqTradeItemList2(Tar.TradeMoney)
				
	def reqTrade(self,exposed):	#正式交易
		"""
		exposed
		"""
		if self.id != exposed:
			return			
		self.Tradelock=True
		Tar=KBEngine.entities.get(self.TradeTargetID)
		if(Tar.Tradelock==False):
		        return
		"""
		selfInventory = InventoryMgr(self)
		TarInventory = InventoryMgr(Tar)
		
		#物品交换
		selfInventory.addItemList(Tar.TradeItemList)
		TarInventory.addItemList(self.TradeItemList)
		
		selfInventory.removeItemList(Tar.TradeItemList)
		TarInventory.removeItemList(self.TradeItemList)	
		"""
		#金币交换
		Tar.money  += self.TradeMoney
		self.money += Tar.TradeMoney
		Tar.money  -= Tar.TradeMoney
		self.money -= self.TradeMoney

		
		Tar.client.OnreqTradeDone()		
		self.client.OnreqTradeDone()
	