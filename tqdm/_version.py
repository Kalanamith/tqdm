# Definition of the version number
version_info = 2, 0, 0, 'dev0'  # major, minor, patch, extra

# Nice string for the version (mimic how IPython composes its version str)
__version__ = '-'.join(map(str, version_info)).replace('-', '.').strip('-')
