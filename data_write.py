from lxml import etree

def write_file(fname, root):
	cont = ""

	if isinstance(root, list):
		cont = "\n".join(map(lambda x: etree.tostring(x,pretty_print=True), root))
	else:
		cont = etree.tostring(root,pretty_print=True)

	with open(fname, "w") as fw:
		fw.write(
"""<?xml version="1.0"?>
<Definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
""" + cont + "\n</Definitions>")
