# Exemple de code qui récupère le nom et la fonction des batiments dans le fichier xml
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
for building in root.iter('building'):
    name = building.find('name').text
    function = building.find('function').text
    print(name + ' : ' + function)
    print( ) 