#! /usr/bin/env python
# encoding: utf-8
# Konstantinos Chatzilygeroudis - 2018

"""
Quick n dirty GLFW 3 detection
"""

import os
from waflib.Configure import conf


def options(opt):
    pass

@conf
def check_glfw(conf):
    includes_check = ['/usr/local/include', '/usr/include']
    libs_check = ['/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu/']

    glfw_include = []
    glfw_lib = []
    try:
        conf.start_msg('Checking for GLFW includes')
        res = conf.find_file('GLFW/glfw3.h', includes_check)
        incl = res[:-len('GLFW/glfw3.h')-1]
        glfw_include = glfw_include + [incl]
        res = conf.find_file('GL/gl.h', includes_check)
        incl = res[:-len('GL/gl.h')-1]
        glfw_include = list(set(glfw_include + [incl]))
        conf.end_msg(glfw_include)
    except:
        conf.end_msg('Not found', 'RED')
        return

    try:
        conf.start_msg('Checking for GLFW libs')
        res = conf.find_file('libglfw.so', libs_check)
        lib = res[:-len('libglfw.so')-1]
        glfw_lib = [lib]
        res = conf.find_file('libGL.so', libs_check)
        lib = res[:-len('libGL.so')-1]
        glfw_lib = list(set(glfw_lib + [lib]))
        conf.end_msg(['glfw', 'GL'])
        conf.get_env()['BUILD_GRAPHIC'] = True
    except:
        conf.end_msg('Not found', 'RED')
        return

    conf.env.INCLUDES_GLFW = glfw_include
    conf.env.LIBPATH_GLFW = glfw_lib
    conf.env.LIB_GLFW = ['glfw', 'GL']
    return 1