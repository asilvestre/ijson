from ctypes import util, cdll

class YAJLImportError(ImportError):
    pass

def find_yajl(required):
    so_name = util.find_library('yajl')
    if so_name is None:
        raise YAJLImportError('YAJL shared object not found.')
    yajl = cdll.LoadLibrary(so_name)
    if hasattr(yajl, 'yajl_version'):
        major, rest = divmod(yajl.yajl_version(), 10000)
    else:
        major, rest = 0, 0
    minor, micro = divmod(rest, 100)
    if major != required:
        raise YAJLImportError('YAJL version %s.x required, found %s.%s.%s' % (required, major, minor, micro))
    return yajl
