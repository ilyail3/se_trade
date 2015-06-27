from lxml import etree
from lxml.builder import E
from data_write import write_file

def generate_bpc(ore_values, assembler_efficiency):


	classes = E.BlueprintClasses(
		E.Class(
			E.Id(
				E.TypeId("BlueprintClassDefinition"),
				E.SubtypeId("Canister_BPC")
			),
			E.DisplayName("Canisters"),
			E.Icon("Textures\\GUI\\Icons\\Icon_Canister.dds"),
			E.HighlightIcon("Textures\\GUI\\Icons\\buttons\\component_highlight.dds"),
			E.InputConstraintIcon("Textures\\GUI\\Icons\\filter_ingot.dds")
		),
		E.Class(
			E.Id(                   
				E.TypeId("BlueprintClassDefinition"),
				E.SubtypeId("Credit_BPC"),
			),
			E.DisplayName("Credits"),
			E.Icon("Textures\\GUI\\Icons\\Icon_Credit.dds"),
			E.HighlightIcon("Textures\\GUI\\Icons\\buttons\\large_block_highlight.dds"),
			E.InputConstraintIcon("Textures\\GUI\\Icons\\filter_ore.dds"),
			E.OutputConstraintIcon("Textures\\GUI\\Icons\\filter_ingot.dds")
		)
		
	)

	entries = E.BlueprintClassEntries()

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
		

		entries.append(E.Entry(Class="Credit_BPC", BlueprintSubtypeId=ore.canister_id + "_Buy"))
		entries.append(E.Entry(Class="Credit_BPC", BlueprintSubtypeId=ore.canister_id + "_Sell"))
		entries.append(E.Entry(Class="Canister_BPC", BlueprintSubtypeId=ore.canister_id + "_Compress"))
	
		

	write_file("Data/BPC.sbc", [classes, entries])
