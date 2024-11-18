import xml.dom.minidom as minidom

file_path = "currency.xml"
xml_file = open(file_path, 'r', encoding='windows-1251')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

valutes = dom.getElementsByTagName('Valute')
names = []

for valute in valutes:
    nominal_node = valute.getElementsByTagName('Nominal')[0]
    name_node = valute.getElementsByTagName('Name')[0]
    if int(nominal_node.firstChild.nodeValue) == 1:
        names.append(name_node.firstChild.nodeValue)

xml_file.close()

for name in names:
    print(name)
