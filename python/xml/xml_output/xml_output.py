import xml.etree.ElementTree as et

def dict_to_xml(dict):
    data = et.Element("data")
    for key in dict.keys():
        user = et.SubElement(data, key)
        id = et.SubElement(user, "id")
        id.text = str(dict[key]["id"])

        name = et.SubElement(user, "name")
        name.text = dict[key]["name"]

    return data
    

if __name__ == "__main__":
    dict = {
        "user1": {
            "id": 1,
            "name": "test1",
        },
        "user2": {
            "id": 2,
            "name": "test2",
        }
    }

    r = dict_to_xml(dict)
    tree = et.ElementTree(r)
    tree.write("test.xml")
