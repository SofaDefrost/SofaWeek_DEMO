""" type: SofaContent """
import Sofa
import Sofa.Core
import Sofa.Helper
    
@Sofa.PrefabBuilder
def Repeat(prefab, name="Sphere", filename="mesh/sphere.obj", n=5, spacing=2.0, scale=1.0):
    """Create a Sphere."""
    for i in range(0, n):
        c = prefab.addChild("Sphere"+str(n) )
        c.addObject("MechanicalObject", name="state")
        c.addObject("UniformMass", name="mass")

        v = c.addChild("Visual")
        v.addObject("MeshObjLoader", name="loader", filename=filename, scale=scale, translation=[spacing*i,0,0])
        v.addObject("OglModel", src="@./loader")

    return prefab
    
