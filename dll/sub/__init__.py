import ctypes
import logging
import os.path

# with os.add_dll_directory(os.path.dirname(os.path.dirname(__file__))):
#     try:
#         from ._sub import factorial_ext
#         import_location = "os.add_dll_directory()"
#     except ImportError:
#         lib_dll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib.dll"))
#         from ._sub import factorial_ext
#         import_location = "explicit dll path"

dll_dir = os.add_dll_directory(os.path.dirname(os.path.dirname(__file__)))
try:
    from ._sub import factorial_ext
    import_location = "os.add_dll_directory()"
except ImportError:
    lib_dll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib.dll"))
    from ._sub import factorial_ext
    import_location = "explicit dll path"
dll_dir.close()


def my_factorial(val):
    logging.info(f"factorial_ext() imported via {import_location}")
    return factorial_ext(val)
