import xml.etree.ElementTree as ET
from collections import defaultdict


class ComponentFinder:
    def components_in(self, netlist: str) -> dict:
        result = defaultdict(set)
        root = ET.fromstring(netlist)
        nets = root.findall('net')
        for net in nets:
            for connector in net.findall('connector'):
                part = connector.find('part')
                result[part.get('title')].add(part.get('id'))
        return result
