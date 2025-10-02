#!/usr/bin/env
"""
this function shows serialization and deserialization
using XML as an alternative format to JSON
"""

import xml.etree.ElementTree as ET
import json


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)   # make <key></key>
        child.text = str(value)            # put the value inside

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        key = child.tag        # e.g. "name"
        value = child.text     # e.g. "Carla"
        dictionary[key] = value

    return dictionary
