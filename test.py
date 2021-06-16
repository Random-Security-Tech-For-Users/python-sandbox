import importlib
def importer(name, *args):
    M = importlib.__import__(name, *args)
    if name == 'os':
        del M.system
    return M
__builtins__.__dict__['__import__'] = importer
