import bpy, bmesh


def star_connect():
    
#   Stores current select object.
    obj = bpy.context.object
    
#   Starts new Bmesh instance from current edit mode mesh.
    bm = bmesh.from_edit_mesh(obj.data)
    
    vertices = bm.verts
    
    selected = []
    
#   Appends all selected (Not active) verts to selected list.
    for i in range(len(vertices)):
        if vertices[i].select == True and not bm.select_history.active.index == i: 
            selected.append(i)

#   Deselects all selected verts based on selected list while keeping active vert.        
    for i in range(len(selected)):
        vertices[selected[i]].select = False

#   Iterates over each vert indavidually and applies vertex join operation.
    for i in range(len(selected)):
        vertices[selected[i]].select = True
        bpy.ops.mesh.vert_connect_path()
        vertices[selected[i]].select = False

#   Sellect all desellected verts.
    for i in range(len(selected)):
        vertices[selected[i]].select = True

#   Applies changes from Bmesh instance to current edit mode mesh.
    bmesh.update_edit_mesh(obj.data)
    

star_connect()
