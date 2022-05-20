import sys
import re

print("sys.argv: {}\n".format(sys.argv))

print("sys.path: {}\n".format(sys.path))

print("sys.version: {}\n".format(sys.version))

print("sys.version_info: {}\n".format(sys.version_info))

print("sys.version_info.major: {}".format(sys.version_info.major), end=' ')
print("sys.version_info.minor: {}\n".format(sys.version_info.minor))

print("sys.platform: {}\n".format(sys.platform))

print("sys.prefix: {}\n".format(sys.prefix))
print("sys.executable: {}\n".format(sys.executable))


print("sys.modules['re']: {}\n".format(sys.modules['re']))
print("sys.modules['sys']: {}\n".format(sys.modules['sys']))

# sys.stdin  sys.stdout sys.stderr

print("HELP HELP", file=sys.stderr)

print("dir(sys): {}\n".format(dir(sys)))

import re
print("dir(re): {}\n".format(dir(re)))
