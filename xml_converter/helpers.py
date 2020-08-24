def xml_to_json(element):
    result = {}
    if len(element) == 0:
        result[element.tag] = element.text or ''
    else:
        result[element.tag] = []
        for child in element:
            child_result = xml_to_json(child)
            result[element.tag].append(child_result)
    return result