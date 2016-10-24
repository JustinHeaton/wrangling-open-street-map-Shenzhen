
import xml.etree.cElementTree as ET
import pprint
import re

def get_user(users, element):
    if element.get('uid'):
        users.add(element.get('uid'))
        return users
    else:
        pass


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        get_user(users, element)
    return users


def test():

    users = process_map('shenzhen_china.osm')
    pprint.pprint(users)




if __name__ == "__main__":
    test()