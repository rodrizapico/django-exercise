def recursive_xml_parse(element):
    result = {}
    if len(element) == 0:
        result[element.tag] = element.text or ''
    else:
        result[element.tag] = []
        for child in element:
            child_result = recursive_xml_parse(child)
            result[element.tag].append(child_result)
    return result