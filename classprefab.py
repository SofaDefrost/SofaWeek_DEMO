"""type: SofaContent"""
import sys
import os
import Sofa.Core
# all Paths
# all Modules:

class MyPrefab(Sofa.Prefab):
    def __init__(self, *args, **kwargs):
        Sofa.Prefab.__init__(self, *args, **kwargs)

    def doReInit(self):
        self.addPrefabParameter("toto", value=0.0, help="DOC", type="float")
        self.addObject("MeshVTKLoader", name="loader", filename="mesh/Armadillo_Tetra_4406.vtu")
        self.addObject("TetrahedronSetTopologyContainer", src="@loader")
        self.addObject("MechanicalObject", src="@loader")
        self.addObject("TetrahedronFEMForceField")
