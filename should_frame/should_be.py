




def should_framework(element, *cond, desc=None):
    element = element
    conditions = cond
    desc = desc

    if conditions[0].__str__() == 'displayed':
        element.is_displayed()

