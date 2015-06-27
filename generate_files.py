from resources import RawOre, Ingot
from generate_bp import generate_bp
from generate_bpc import generate_bpc
from generate_comp import generate_comp

ore_values = [
	RawOre("Ice", 280, "Ice"),
	#RawOre("Stone", 310),
	#RawOre("Iron", 500),
	#RawOre("Nickel Ore", 20),
	#RawOre("Cobal Ore", 22),
	#RawOre("Magnesium Ore", 24),
	#RawOre("Silicon Ore", 22),
	#RawOre("Silver Ore", 20),
	#RawOre("Gold Ore", 20),
	#RawOre("Platinum Ore", 20),
	#RawOre("Uranium Ore", 44)

	Ingot("Stone", 279, "Gravel"),
	Ingot("Iron", 350),
	Ingot("Nickel", 8),
	Ingot("Cobalt", 6.6),
	Ingot("Magnesium", 0.168, "Magnesium Powder"),
	Ingot("Silicon", 15.4, "Silicon Wafer"),
	Ingot("Silver", 2.2),
	Ingot("Gold", 0.2),
	Ingot("Platinum", 0.1),
	Ingot("Uranium", 0.308)
]

assembler_efficiency = 1

generate_bp(ore_values, assembler_efficiency)
generate_bpc(ore_values, assembler_efficiency)
generate_comp(ore_values, assembler_efficiency)

