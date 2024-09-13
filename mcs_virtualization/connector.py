from . import vmware, xcpng, default


DEFAULT_CLASS = default

NAME_TO_CLASS = {
    'vmware': vmware,
    'xcpng': xcpng
}

def Connection(name: str):
    name = name.lower()

    if name in NAME_TO_CLASS:
        module = NAME_TO_CLASS[name]
    else:
        module = DEFAULT_CLASS

    return module


