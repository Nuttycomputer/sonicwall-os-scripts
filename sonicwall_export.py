#!/usr/bin/env python3

import xml.etree.ElementTree as ET

import tablib

__author__ = 'Jay Shepherd'

file = 'sonicwall_xml.xml'
sonicwall_tree = ET.parse(file)

rules = sonicwall_tree.findall('submode')
excel_headers = ('ID',
                 'Action',
                 'Source Zone',
                 'Destination Zone',
                 'Source Address',
                 'Source Port',
                 'Destination Address',
                 'Service',
                 'Comment')
ruleset_table = tablib.Dataset(headers=excel_headers)

for rule in rules:
    id = rule.find('id')
    action = rule.find('action')
    source_zone = rule.find('from')
    destination_zone = rule.find('to')
    source_address = rule.find('source/address')
    source_port = rule.find('source/port')
    destination_address = rule.find('destination/address')
    service = rule.find('service')
    comment = rule.find('comment')
    element_list = [id,
                    action,
                    source_zone,
                    destination_zone,
                    source_address,
                    source_port,
                    destination_address,
                    service,
                    comment]
    rule_output = []
    for element in element_list:
        # Make sure element actually exists, if not just write out an empty string
        if element is None:
            rule_output.append('')
        else:
            # Find any children
            children = list(element)
            # Check the last child (ie. last parameter) for text
            child = children[-1]
            if child.text is None:
                # Write out the element tag.
                # This is because SonicWall uses elements for things like 'any'
                # consistency is really hard for network vendors...
                rule_output.append(child.tag)
            else:
                # Lets see if we are about to write out the ID param
                # If so lets convert to integer for Excel's sake
                if element.tag == 'id':
                    rule_output.append(int((child.text)))
                else:
                    rule_output.append(''.join(child.text))
    ruleset_table.append(rule_output)

open('sonicwall_ruleset.xls', 'wb').write(ruleset_table.xls)
print('The sonicwall ruleset has been written out as sonicwall_ruleset.xls')
