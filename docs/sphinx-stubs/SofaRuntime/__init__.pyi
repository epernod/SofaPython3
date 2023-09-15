"""
SofaRuntime package
-----------------------

"""
import SofaRuntime
import typing
import Sofa
import Sofa.Helper.System
import SofaRuntime.SofaRuntime.Timer
import importlib
import inspect
import os
import sys
import traceback

__all__ = [
    "DataRepository",
    "PluginRepository",
    "Sofa",
    "SofaRuntime",
    "Timer",
    "formatStackForSofa",
    "getPythonCallingPoint",
    "getPythonCallingPointAsString",
    "getSofaFormattedStringFromException",
    "getStackForSofa",
    "importPlugin",
    "importlib",
    "init",
    "inspect",
    "os",
    "sendMessageFromException",
    "sofaExceptHandler",
    "sofaFormatHandler",
    "sys",
    "traceback",
    "unloadModules"
]


def importPlugin(arg0: str) -> bool:
    """
    import a sofa plugin into the current environment
    """
def init() -> None:
    pass
DataRepository: Sofa.Helper.System.FileRepository
PluginRepository: Sofa.Helper.System.FileRepository
__SofaPythonEnvironment_importedModules__: dict # value = {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, 'posix': <module 'posix' (built-in)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' from '/usr/lib64/python3.9/codecs.py'>, 'encodings.aliases': <module 'encodings.aliases' from '/usr/lib64/python3.9/encodings/aliases.py'>, 'encodings': <module 'encodings' from '/usr/lib64/python3.9/encodings/__init__.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/usr/lib64/python3.9/encodings/utf_8.py'>, '_signal': <module '_signal' (built-in)>, 'encodings.latin_1': <module 'encodings.latin_1' from '/usr/lib64/python3.9/encodings/latin_1.py'>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' from '/usr/lib64/python3.9/abc.py'>, 'io': <module 'io' from '/usr/lib64/python3.9/io.py'>, '__main__': <module '__main__' from '/home/jnbrunet/.local/bin/pybind11-stubgen'>, '_stat': <module '_stat' (built-in)>, 'stat': <module 'stat' from '/usr/lib64/python3.9/stat.py'>, '_collections_abc': <module '_collections_abc' from '/usr/lib64/python3.9/_collections_abc.py'>, 'genericpath': <module 'genericpath' from '/usr/lib64/python3.9/genericpath.py'>, 'posixpath': <module 'posixpath' from '/usr/lib64/python3.9/posixpath.py'>, 'os.path': <module 'posixpath' from '/usr/lib64/python3.9/posixpath.py'>, 'os': <module 'os' from '/usr/lib64/python3.9/os.py'>, '_sitebuiltins': <module '_sitebuiltins' from '/usr/lib64/python3.9/_sitebuiltins.py'>, '_locale': <module '_locale' (built-in)>, '_bootlocale': <module '_bootlocale' from '/usr/lib64/python3.9/_bootlocale.py'>, 'types': <module 'types' from '/usr/lib64/python3.9/types.py'>, 'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>, 'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>, 'warnings': <module 'warnings' from '/usr/lib64/python3.9/warnings.py'>, 'importlib': <module 'importlib' from '/usr/lib64/python3.9/importlib/__init__.py'>, 'importlib.machinery': <module 'importlib.machinery' from '/usr/lib64/python3.9/importlib/machinery.py'>, '_heapq': <module '_heapq' from '/usr/lib64/python3.9/lib-dynload/_heapq.cpython-39-x86_64-linux-gnu.so'>, 'heapq': <module 'heapq' from '/usr/lib64/python3.9/heapq.py'>, 'itertools': <module 'itertools' (built-in)>, 'keyword': <module 'keyword' from '/usr/lib64/python3.9/keyword.py'>, '_operator': <module '_operator' (built-in)>, 'operator': <module 'operator' from '/usr/lib64/python3.9/operator.py'>, 'reprlib': <module 'reprlib' from '/usr/lib64/python3.9/reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'collections': <module 'collections' from '/usr/lib64/python3.9/collections/__init__.py'>, 'collections.abc': <module 'collections.abc' from '/usr/lib64/python3.9/collections/abc.py'>, '_functools': <module '_functools' (built-in)>, 'functools': <module 'functools' from '/usr/lib64/python3.9/functools.py'>, 'contextlib': <module 'contextlib' from '/usr/lib64/python3.9/contextlib.py'>, 'enum': <module 'enum' from '/usr/lib64/python3.9/enum.py'>, '_sre': <module '_sre' (built-in)>, 'sre_constants': <module 'sre_constants' from '/usr/lib64/python3.9/sre_constants.py'>, 'sre_parse': <module 'sre_parse' from '/usr/lib64/python3.9/sre_parse.py'>, 'sre_compile': <module 'sre_compile' from '/usr/lib64/python3.9/sre_compile.py'>, 'copyreg': <module 'copyreg' from '/usr/lib64/python3.9/copyreg.py'>, 're': <module 're' from '/usr/lib64/python3.9/re.py'>, 'typing.io': <class 'typing.io'>, 'typing.re': <class 'typing.re'>, 'typing': <module 'typing' from '/usr/lib64/python3.9/typing.py'>, 'importlib.abc': <module 'importlib.abc' from '/usr/lib64/python3.9/importlib/abc.py'>, 'importlib.util': <module 'importlib.util' from '/usr/lib64/python3.9/importlib/util.py'>, 'mpl_toolkits': <module 'mpl_toolkits' (namespace)>, 'sphinxcontrib': <module 'sphinxcontrib' (namespace)>, 'zope': <module 'zope' (namespace)>, 'paste': <module 'paste' (namespace)>, 'abrt_exception_handler3': <module 'abrt_exception_handler3' from '/usr/lib/python3.9/site-packages/abrt_exception_handler3.py'>, 'site': <module 'site' from '/usr/lib64/python3.9/site.py'>, '_csv': <module '_csv' from '/usr/lib64/python3.9/lib-dynload/_csv.cpython-39-x86_64-linux-gnu.so'>, 'csv': <module 'csv' from '/usr/lib64/python3.9/csv.py'>, 'email': <module 'email' from '/usr/lib64/python3.9/email/__init__.py'>, 'fnmatch': <module 'fnmatch' from '/usr/lib64/python3.9/fnmatch.py'>, 'ntpath': <module 'ntpath' from '/usr/lib64/python3.9/ntpath.py'>, 'errno': <module 'errno' (built-in)>, 'urllib': <module 'urllib' from '/usr/lib64/python3.9/urllib/__init__.py'>, 'urllib.parse': <module 'urllib.parse' from '/usr/lib64/python3.9/urllib/parse.py'>, 'pathlib': <module 'pathlib' from '/usr/lib64/python3.9/pathlib.py'>, 'binascii': <module 'binascii' from '/usr/lib64/python3.9/lib-dynload/binascii.cpython-39-x86_64-linux-gnu.so'>, 'zlib': <module 'zlib' from '/usr/lib64/python3.9/lib-dynload/zlib.cpython-39-x86_64-linux-gnu.so'>, '_compression': <module '_compression' from '/usr/lib64/python3.9/_compression.py'>, '_weakrefset': <module '_weakrefset' from '/usr/lib64/python3.9/_weakrefset.py'>, 'threading': <module 'threading' from '/usr/lib64/python3.9/threading.py'>, '_bz2': <module '_bz2' from '/usr/lib64/python3.9/lib-dynload/_bz2.cpython-39-x86_64-linux-gnu.so'>, 'bz2': <module 'bz2' from '/usr/lib64/python3.9/bz2.py'>, '_lzma': <module '_lzma' from '/usr/lib64/python3.9/lib-dynload/_lzma.cpython-39-x86_64-linux-gnu.so'>, 'lzma': <module 'lzma' from '/usr/lib64/python3.9/lzma.py'>, 'pwd': <module 'pwd' (built-in)>, 'grp': <module 'grp' from '/usr/lib64/python3.9/lib-dynload/grp.cpython-39-x86_64-linux-gnu.so'>, 'shutil': <module 'shutil' from '/usr/lib64/python3.9/shutil.py'>, '_struct': <module '_struct' from '/usr/lib64/python3.9/lib-dynload/_struct.cpython-39-x86_64-linux-gnu.so'>, 'struct': <module 'struct' from '/usr/lib64/python3.9/struct.py'>, 'zipfile': <module 'zipfile' from '/usr/lib64/python3.9/zipfile.py'>, 'configparser': <module 'configparser' from '/usr/lib64/python3.9/configparser.py'>, 'importlib.metadata': <module 'importlib.metadata' from '/usr/lib64/python3.9/importlib/metadata.py'>, '_ast': <module '_ast' (built-in)>, 'ast': <module 'ast' from '/usr/lib64/python3.9/ast.py'>, '_opcode': <module '_opcode' from '/usr/lib64/python3.9/lib-dynload/_opcode.cpython-39-x86_64-linux-gnu.so'>, 'opcode': <module 'opcode' from '/usr/lib64/python3.9/opcode.py'>, 'dis': <module 'dis' from '/usr/lib64/python3.9/dis.py'>, 'token': <module 'token' from '/usr/lib64/python3.9/token.py'>, 'tokenize': <module 'tokenize' from '/usr/lib64/python3.9/tokenize.py'>, 'linecache': <module 'linecache' from '/usr/lib64/python3.9/linecache.py'>, 'inspect': <module 'inspect' from '/usr/lib64/python3.9/inspect.py'>, 'traceback': <module 'traceback' from '/usr/lib64/python3.9/traceback.py'>, 'weakref': <module 'weakref' from '/usr/lib64/python3.9/weakref.py'>, '_string': <module '_string' (built-in)>, 'string': <module 'string' from '/usr/lib64/python3.9/string.py'>, 'atexit': <module 'atexit' (built-in)>, 'logging': <module 'logging' from '/usr/lib64/python3.9/logging/__init__.py'>, 'gettext': <module 'gettext' from '/usr/lib64/python3.9/gettext.py'>, 'argparse': <module 'argparse' from '/usr/lib64/python3.9/argparse.py'>, 'pybind11_stubgen': <module 'pybind11_stubgen' from '/home/jnbrunet/.local/lib/python3.9/site-packages/pybind11_stubgen/__init__.py'>, 'pybind11_stubgen.__init__': <module 'pybind11_stubgen.__init__' from '/home/jnbrunet/.local/lib/python3.9/site-packages/pybind11_stubgen/__init__.py'>, 'locale': <module 'locale' from '/usr/lib64/python3.9/locale.py'>, 'SofaRuntime': <module 'SofaRuntime' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/SofaRuntime/__init__.py'>, 'Sofa.Helper.System': <module 'Sofa.Helper.System'>, 'Sofa.Helper': <module 'Sofa.Helper' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/Sofa/Helper.cpython-39-x86_64-linux-gnu.so'>, 'Sofa.Core': <module 'Sofa.Core' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/Sofa/Core.cpython-39-x86_64-linux-gnu.so'>, 'Sofa.Simulation': <module 'Sofa.Simulation' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/Sofa/Simulation.cpython-39-x86_64-linux-gnu.so'>, 'Sofa.Types': <module 'Sofa.Types' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/Sofa/Types.cpython-39-x86_64-linux-gnu.so'>, 'SofaTypes.SofaTypes': <module 'SofaTypes.SofaTypes' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/SofaTypes/SofaTypes.cpython-39-x86_64-linux-gnu.so'>, 'SofaTypes': <module 'SofaTypes' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/SofaTypes/__init__.py'>, 'Sofa.prefab': <module 'Sofa.prefab' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/Sofa/prefab.py'>, 'Sofa': <module 'Sofa' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/Sofa/__init__.py'>, 'SofaRuntime.SofaRuntime.Timer': <module 'SofaRuntime.SofaRuntime.Timer'>, 'SofaRuntime.SofaRuntime': <module 'SofaRuntime.SofaRuntime' from '/home/jnbrunet/sources/sofa/build/install/plugins/SofaPython3/lib/python3/site-packages/SofaRuntime/SofaRuntime.cpython-39-x86_64-linux-gnu.so'>}
__SofaPythonEnvironment_modulesExcludedFromReload = []