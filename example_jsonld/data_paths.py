#!/usr/bin/env python
# -*- coding: utf-8 -*-
import example_jsonld
import os
import importlib_metadata
from . import __path__ as ROOT_PATH

PKG_NAME = 'example_jsonld'

VERSION = importlib_metadata.version(PKG_NAME)

print("root path: {}".format(ROOT_PATH))
print("Library version: {}".format(VERSION))
SITE_PATH = os.path.dirname(ROOT_PATH[0])
DISTINFO = os.path.join(SITE_PATH, '{}-{}.dist-info'.format(PKG_NAME, VERSION))
# print(DISTINFO, os.path.isdir(DISTINFO))

RECORD = os.path.join(DISTINFO, 'RECORD')
with open(RECORD) as fp:
    records = fp.readlines()


fullpath = None
for line in records:
    if '.bin' in line:
        filename = line.split(',')[0]
        fullpath = os.path.join(SITE_PATH, filename)
        # print(line)
        print("Your model path: {} (exist={})".format(
            fullpath, os.path.isfile(fullpath)))

if fullpath:
    with open(fullpath) as fp:
        print("The contents of your model:")
        print(fp.read())
