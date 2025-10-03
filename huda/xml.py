import polars as pl
import xml.etree.ElementTree as ET

def open_xml(file_path):
    """
    Open XML file easily and convert it into a Polars DataFrame.

    Parameters:
        - file_path: path to your XML file

    Example usage:
    -----------------------
    Suppose you have a file "testdata.xml" with this content:
    
        <data>
            <record>
                <id>1</id>
                <name>Ali</name>
                <need>Food</need>
            </record>
            <record>
                <id>2</id>
                <name>Sara</name>
                <need>Water</need>
            </record>
        </data>

    You can load it like this:
    
        df = open_xml("testdata.xml")
        print(df)

    Output:
    ┌─────┬───────┬───────┐
    │ id  ┆ name  ┆ need  │
    │ --- ┆ ---   ┆ ---   │
    │ str ┆ str   ┆ str   │
    ╞═════╪═══════╪═══════╡
    │ 1   ┆ Ali   ┆ Food  │
    │ 2   ┆ Sara  ┆ Water │
    └─────┴───────┴───────┘
    """

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = []
        for record in root.findall('record'):
            row = {child.tag: child.text for child in record}
            data.append(row)

        # Convert list of dicts to Polars DataFrame
        df = pl.DataFrame(data)
        print("✅ XML file loaded successfully!")
        print(f"Rows: {df.height}, Columns: {df.width}")
        return df

    except FileNotFoundError:
        print("⚠️ File not found. Please check the file name and path.")
        return None
    except Exception as e:
        print("⚠️ Something went wrong while opening the XML file.")
        print("Error:", e)
        return None
