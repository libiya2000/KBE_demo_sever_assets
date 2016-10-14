# -*- coding: utf-8 -*-
import KBEngine
import GlobalDefine
import d_entities
from KBEDebug import *
from interfaces.GameObject import GameObject
from interfaces.Combat import Combat
from interfaces.Spell import Spell
from interfaces.Teleport import Teleport
from interfaces.Dialog import Dialog
from interfaces.State import State
from interfaces.Motion import Motion
from interfaces.SkillBox import SkillBox
from interfaces.Trade import Trade

class Avatar(KBEngine.Entity,
				GameObject,
				State,
				Motion, 
				SkillBox,
				Combat, 
				Spell, 
				Teleport,
                                Trade,
				Dialog):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self) 
		State.__init__(self) 
		Motion.__init__(self) 
		SkillBox.__init__(self) 
		Spell.__init__(self) 
		Teleport.__init__(self) 
		Dialog.__init__(self) 
		self.resetPropertys()
		Combat.__init__(self) 
		Trade.__init__(self)
		
		# 设置每秒允许的最快速度, 超速会被拉回去
		self.topSpeed = self.moveSpeed + 5.0
		# self.topSpeedY = 10.0

			
	def isPlayer(self):
		"""
		virtual method.
		"""
		return True

	def dropNotify(self, itemId, UUid, itemCount):
		datas = d_entities.datas.get(40001003)
		
		if datas is None:
			ERROR_MSG("SpawnPoint::spawn:%i not found." % 40001003)
			return
			
		params = {
			"uid" : datas["id"],
			"utype" : datas["etype"],
			"modelID" : datas["modelID"],
			"dialogID" : datas["dialogID"],
			"name" : datas["name"],
			"descr" : datas.get("descr", ''),
			"itemId" : itemId,
			"itemCount" : itemCount,
		}
		
		e = KBEngine.createEntity("DroppedItem", self.spaceID, tuple(self.position), tuple(self.direction), params)
		
		self.client.dropItem_re(itemId, UUid)

	def resetPropertys(self):
		self.attack_Max = self.strength*2
		self.attack_Min = self.strength*1
		self.defence = int(self.dexterity/4)
		self.HP_Max = self.stamina*10

	def equipNotify(self, itemId):
		self.equipWeapon = itemId


	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		GameObject.onTimer(self, tid, userArg)
		Spell.onTimer(self, tid, userArg)
		
	def onGetWitness(self):
		"""
		KBEngine method.
		绑定了一个观察者(客户端)
		"""
		DEBUG_MSG("Avatar::onGetWitness: %i." % self.id)

	def onLoseWitness(self):
		"""
		KBEngine method.
		解绑定了一个观察者(客户端)
		"""
		DEBUG_MSG("Avatar::onLoseWitness: %i." % self.id)
	
	def onDestroy(self):
		"""
		KBEngine method.
		entity销毁
		"""
		DEBUG_MSG("Avatar::onDestroy: %i." % self.id)
		Teleport.onDestroy(self)
		Combat.onDestroy(self)
		
	def relive(self, exposed, type):
		"""
		defined.
		复活
		"""
		if exposed != self.id:
			return
			
		DEBUG_MSG("Avatar::relive: %i, type=%i." % (self.id, type))
		
		# 回城复活
		if type == 0:
			pass
			
		self.fullPower()
		self.changeState(GlobalDefine.ENTITY_STATE_FREE)

		
	