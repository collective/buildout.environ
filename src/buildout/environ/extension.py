# -*- coding: utf-8 -*-
import os


def install(buildout):
    for key in os.environ:
        buildout['__environ__'] = os.environ[key]
