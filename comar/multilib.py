#!/usr/bin/env python
import os
import os.path

kver = "4.7.6"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system("/usr/bin/gl-driver-switch set-link nvidia")
    except Exception, e:
        print "Post-install error: %s" % e

def postRemove():
    try:
        os.system("/usr/bin/gl-driver-switch set-link default")
    except Exception, e:
        print "Post-remove error: %s" % e
