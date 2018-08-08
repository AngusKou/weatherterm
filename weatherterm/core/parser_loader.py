import os
import re
import inspect


def _get_parser_list(dirname):
    files = [os.path.splitext(f)[0]
             for f in os.listdir(dirname)
             if not f.startswith("__")]
    return files


def _import_parsers(parserfiles):
    m = re.compile('.+parser$', re.I)
    _modules = __import__('weatherterm.parsers',
                          globals(),
                          locals(),
                          parserfiles,
                          0)
    _parsers = [(k, v) for k, v in inspect.getmembers(_modules)
                if inspect.ismodule(v) and m.match(k)]
    _class = dict()
    for k, v in _parsers:
        _class.update({k: v for k, v in inspect.getmembers(v)
                       if inspect.isclass(v) and m.match(k)})
    return _class


def load(dirname):
    parserfiles = _get_parser_list(dirname)
    return _import_parsers(parserfiles)
