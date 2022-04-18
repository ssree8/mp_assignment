import xml.etree.ElementTree as ET
from datetime import timedelta, date

def paser_xml(path, out, x, y):     
	mytree = ET.parse(path)
	myroot = mytree.getroot()
	roots = myroot.findall(".//food")
	for root in roots:
		for i in root:
			if i.tag == "depart":
				depart = date.today()+timedelta(days=x)
				i.text = depart.strftime("%d-%m-%y")
			elif i.tag == "returns":
				returns = date.today()+timedelta(days=y)
				i.text = returns.strftime("%d-%m-%y")
	tree = ET.ElementTree(myroot)
	with open(out, "wb") as fl:
		tree.write(fl)

if __name__ == "__main__":
	path = r"./test_data/test.xml"
	out = r"./output_data/output.xml"
	x = 5
	y = 6
	paser_xml(path, out, x, y)