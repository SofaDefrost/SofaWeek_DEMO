""" type: SofaContent """
import Sofa
import Sofa.Core
import Sofa.Helper
    
@Sofa.PrefabBuilder
def Sphere(prefab, name="Sphere", radius=1.0, n=5, withRendering=False):
    """Create a Sphere."""
    prefab.addObject("MechanicalObject", name="state")
    prefab.addObject("UniformMass", name="mass")

    for i in range(0, n):
        prefab.addChild("XY"+str(n) )

    if withRendering:
        collis = prefab.addChild("Visual")
        collis.addObject("MeshObjLoader", name="loader", filename="mesh/sphere.obj", scale=radius)
        collis.addObject("OglModel", src="@./loader")

    return prefab
    
