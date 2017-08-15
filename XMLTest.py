import xml.etree.ElementTree as ET
tree = ET.parse('Levels.xml')
root = tree.getroot()
children = root.getchildren()

# XML Parsing Test
# Should read level descriptions from the levels.xml file, then print them.
# Build a command for short and long descriptions.
area = 'altar'

#for child in children:
    #print(child.tag, child.attrib)

for child in children:
    attributes = str(child.attrib)
    # print attributes
    if area in attributes:
        print (root[1][0].text)
    else:
        continue
