from lxml import etree
from lxml.builder import E
from data_write import write_file

def generate_comp(ore_values, assembler_efficiency):


	components = E.Components(
		E.Component(
			E.Id(
				E.TypeId("Component"),
				E.SubtypeId("Credit")
			),
			E.DisplayName("Credits"),
			E.Icon("Textures\\GUI\\Icons\\Icon_Credit.dds"),
			E.Size(
				E.X("0.2"),
				E.Y("0.1"),
				E.Z("0.1")
			),
			E.Mass("0.1"),
			E.Volume("0.1"),
			E.Model("Models\\Credit.mwm"),
			E.MaxIntegrity("30"),
			E.DropProbability("0.5")
		)		
	)

	for ore in ore_values:
		

		components.append(E.Component(
			E.Id(
				E.TypeId("Component"),
				E.SubtypeId(ore.canister_id)
			),
			E.DisplayName(ore.name + " Canister"),
			E.Icon("Textures\\GUI\\Icons\\Icon_Canister.dds"),
			E.Size(
				E.X("0.2"),
				E.Y("0.1"),
				E.Z("0.1")
			),
			E.Mass("375"),
			E.Volume("2"),
			E.Model("Models\\Canister_Ag.mwm"),
			E.MaxIntegrity("30"),
			E.DropProbability("0.5")		
		))
	
		

	write_file("Data/Comp.xml", components)
