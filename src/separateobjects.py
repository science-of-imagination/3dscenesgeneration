import collada

def main():
	filename = "964"
	opened_file = collada.Collada(filename+".dae")
	#for i,geom in enumerate(opened_file.scene.objects("geometry")):
	for i,geom in enumerate(opened_file.geometries):
		subfile = collada.Collada()
		print geom
		
		# Default material stuff, not necessary.
		#effect = collada.material.Effect("effect0", [], "phong", diffuse=(1,0,0), specular=(0,1,0))
		#mat = collada.material.Material("material0","mymaterial", effect)
		#subfile.effects.append(effect)
		#mesh.material.append(mat)

		# We seem to lose the initial materials
		subfile.geometries.append(geom)
		
		geomnode = collada.scene.GeometryNode(geom,[])
		node = collada.scene.Node("node0",children=[geomnode])
		scene = collada.scene.Scene("scene0", [node])
		subfile.scenes.append(collada.scene.Scene("scene0", [node]))
		subfile.scene = scene
		subfile.write(filename+"_"+str(i)+".dae")

main()