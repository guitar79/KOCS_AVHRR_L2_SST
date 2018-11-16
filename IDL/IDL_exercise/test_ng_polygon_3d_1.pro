PRO test_ng_polygon_3d_1

; rendering a cube polygon

arr = [[0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
MESH_OBJ, 5, vertices, polygons, TRANSPOSE(arr), P2=[0, 0, 1]
HELP, vertices
HELP, polygons
;PRINT, polygons
polygons = [polygons, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8]

oPolygon = OBJ_NEW('IDLgrPolygon', DATA=vertices, POLYGONS=polygons)
oPolygon -> SetProperty, COLOR=[255, 0, 255]
XOBJVIEW, oPolygon, XSIZE=600, YSIZE=600

END