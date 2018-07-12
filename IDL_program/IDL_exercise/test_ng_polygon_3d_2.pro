PRO test_ng_polygon_3d_2

MESH_OBJ, 4, vertices, polygons, REPLICATE(1, 37, 19)
HELP, vertices
HELP, polygons
oSphere = OBJ_NEW('IDLgrPolygon', DATA=vertices, POLYGONS=polygons, $
  COLOR=[255, 100, 100], STYLE=2, THICK=2)
XOBJVIEW, oSphere, XSIZE=600, YSIZE=600, SCALE=0.8

END