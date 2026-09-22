import xml.etree.ElementTree as ElementTree


def serialize_to_xml(dictionary, filename):
    root = ElementTree.Element("data")

    for key, value in dictionary.items():
        child = ElementTree.SubElement(root, key)
        child.text = str(value)

    tree = ElementTree.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    try:
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except Exception:
        return None
