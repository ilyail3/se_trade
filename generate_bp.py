from lxml import etree
from lxml.builder import E
from data_write import write_file

def generate_bp(ore_values, assembler_efficiency):
	root = etree.Element("Blueprints")

	# Compress blueprints

	#<Id>
	#  <TypeId>BlueprintDefinition</TypeId>
	#  <SubtypeId>Canister_Ag</SubtypeId>
	#</Id>
	#<DisplayName>Silver Canister</DisplayName>
	#<Icon>Textures\GUI\Icons\Icon_Canister.dds</Icon>
	#<Prerequisites>
	#  <Item Amount="500" TypeId="Ingot" SubtypeId="Silver" />
	#</Prerequisites>
	#<Result Amount="1" TypeId="Component" SubtypeId="Canister_Ag_R" />
	#<BaseProductionTimeInSeconds>10</BaseProductionTimeInSeconds>
	#</Blueprint>

	for ore in ore_values:
		bp = E.Blueprint(
			E.Id(
				E.TypeId("BlueprintDefinition"),
				E.SubtypeId(ore.canister_id + "_Compress")
			),
			E.DisplayName(ore.canister_name),
			E.Icon("Textures\\GUI\\Icons\\Icon_Canister.dds"),
			E.Prerequisites(
				E.Item(Amount="500", TypeId=ore.item_name, SubtypeId=ore.name)
			),
			E.Result(Amount="1", TypeId="Component", SubtypeId=ore.canister_id),
			E.BaseProductionTimeInSeconds("10")
		)

		root.append(bp)

		# Decompression not required since it's nativly provided by the game, doh!

	# Change for Credit
	#<Blueprint>
	#      <Id>
	#        <TypeId>BlueprintDefinition</TypeId>
	#        <SubtypeId>Canister_Ag2</SubtypeId>
	#      </Id>
	#      <DisplayName>Silver Canister</DisplayName>
	#      <Icon>Textures\GUI\Icons\Icon_Canister.dds</Icon>
	#      <Prerequisites>
	#        <Item Amount="10" TypeId="Component" SubtypeId="Credit" />
	#      </Prerequisites>
	#      <Result Amount="3" TypeId="Component" SubtypeId="Canister_Ag_R" />
	#      <BaseProductionTimeInSeconds>0.1</BaseProductionTimeInSeconds>
	#    </Blueprint>
	for ore in ore_values:
		# Calculate sell ratio, so that 10 credits = 3 cans for silver
		# Silver rate is 2.2

		buy_rate = ore.rate * 1.5

		# All results are gurantied to be biger than 20
		min_dist = 20
		min_div = 0
		for i in range(1, 11):
			dist = (buy_rate * i) - int(buy_rate * i)

			if(dist < min_dist):
				min_dist = dist
				min_div = i

		credits = str(min_div)
		cans = str(int(min_div * buy_rate))

		bp = E.Blueprint(
			E.Id(
				E.TypeId("BlueprintDefinition"),
				E.SubtypeId(ore.canister_id + "_Buy")
			),
			E.DisplayName(ore.canister_name),
			E.Icon("Textures\\GUI\\Icons\\Icon_Canister.dds"),
			E.Prerequisites(
				E.Item(Amount=credits, TypeId="Component", SubtypeId="Credit")
			),
			E.Result(Amount=cans, TypeId="Component", SubtypeId=ore.canister_id),
			E.BaseProductionTimeInSeconds("0.5")
		)

		root.append(bp)

		bp = E.Blueprint(
			E.Id(
				E.TypeId("BlueprintDefinition"),
				E.SubtypeId(ore.canister_id + "_Sell")
			),
			E.DisplayName(ore.canister_name),
			E.Icon("Textures\\GUI\\Icons\\Icon_Canister.dds"),
			E.Prerequisites(
				E.Item(Amount=cans, TypeId="Component", SubtypeId=ore.canister_id)
			),
			E.Result(Amount=credits, TypeId="Component", SubtypeId="Credit"),
			E.BaseProductionTimeInSeconds("0.5")
		)

		root.append(bp)
	
		

	write_file("Data/BP.xml", root)
