""" type: SofaContent """
import sys
import os
# all Paths
sys.path.append('prefab')
# all Modules:
from repeat.py import *


def createScene(root):
    root.addObject('DefaultAnimationLoop', name='defaultAnimationLoop')
    root.addObject('DefaultVisualManagerLoop', name='defaultVisualManagerLoop')
    ####################### Prefab: Repeat #########################
    root.addChild(Repeat(name='Repeat', filename='mesh/sphere.obj', n=5, spacing=2.0))

