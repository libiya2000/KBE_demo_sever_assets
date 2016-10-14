# -*- coding: utf-8 -*-
import KBEngine
import skills
import GlobalConst
import SCDefine
from KBEDebug import * 

class SkillBox:
	def __init__(self):
		# 如果玩家没有学习技能，默认添加这些技能
		if len(self.skills) == 0:
			if self.roleTypeCell == 2:
				self.skills.append(1)
				self.skills.append(2)
				self.skills.append(3)
			elif  self.roleTypeCell == 1:
				self.skills.append(4)
				self.skills.append(5)
				self.skills.append(6)
			else:
				self.skills.append(0x3001)
				self.skills.append(0x3002)
				self.skills.append(0x3003)				

	def hasSkill(self, skillID):
		"""
		"""
		return skillID in self.skills

	#--------------------------------------------------------------------------------------------
	#                              defined
	#--------------------------------------------------------------------------------------------
	def requestPull(self, exposed):
		"""
		exposed
		"""
		if self.id != exposed:
			return
		
		DEBUG_MSG("SkillBox::requestPull: %i skills=%i" % (self.id, len(self.skills)))
		for skillID in self.skills:
			self.client.onAddSkill(skillID)
			
	def addSkill(self, skillID):
		"""
		defined method.
		"""
		self.skills.append(skillID)

	def removeSkill(self, skillID):
		"""
		defined method.
		"""
		self.skills.remove(skillID)
		
	def useTargetSkill(self, srcEntityID, skillID, targetID):
		"""
		exposed.
		对一个目标entity施放一个技能
		"""
		if srcEntityID != self.id:
			return
		
		self.spellTarget(skillID, targetID)
