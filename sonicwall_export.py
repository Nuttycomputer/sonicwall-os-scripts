__author__ = 'Jay Shepherd'

import tablib
import xml.etree.ElementTree as ET

file = 'sonicwall_xml.xml'
sonicwall_tree = ET.parse(file)

rules = sonicwall_tree.findall('submode')
headers = ('id',
           'action',
           'source_zone',
           'destination_zone',
           'source_address',
           'source_port',
           'destination_address',
           'service',
           'comment')
ruleset_table = tablib.Dataset(headers=headers)

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
        try:
            rule_output.append(''.join(element.itertext()))
        except:
            rule_output.append('')
    ruleset_table.append(rule_output)

open('sonicwall_ruleset.xls', 'wb').write(ruleset_table.xls)
