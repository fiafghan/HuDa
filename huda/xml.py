import pandas as pd
import xml.etree.ElementTree as ET

def openxml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    data = []
    for record in root.findall('record'):
        row = {child.tag: child.text for child in record}
        data.append(row)

    df = pd.DataFrame(data)
    print ("✅ XML loaded successfully!")
    return df


    


