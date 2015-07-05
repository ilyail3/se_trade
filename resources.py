class TradableResource(object):
	item_name = None

	def __init__(self, name, rate, icon, display_name=None):
		self.name = name
		self.rate = rate
		self.icon = icon

		if display_name is None:
			self.display_name = name + " " + self.item_name
		else:
			self.display_name = display_name

	@property
	def canister_name(self):
		can_name = self.name
		
		return can_name + " Canister"

	@property
	def canister_id(self):
		return self.canister_name.replace(" ","_")

class RawOre(TradableResource):
	item_name = "Ore"

class Ingot(TradableResource):
	item_name = "Ingot"
