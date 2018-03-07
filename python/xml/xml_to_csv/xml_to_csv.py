import xmltodict
import csv

if __name__ == "__main__":
    dict = {}
    # xml to dict
    with open('test.xml') as fd:
        doc = xmltodict.parse(fd.read())
        dict.update({"data": {
            "user1": doc["data"]["user1"],
            "user2": doc["data"]["user2"],
        }})

#    print(dict)
 
    # dict to csv
    with open('test.csv', 'w') as f:
        w = csv.DictWriter(f, dict.keys())
        w.writeheader()
        w.writerow(dict)
