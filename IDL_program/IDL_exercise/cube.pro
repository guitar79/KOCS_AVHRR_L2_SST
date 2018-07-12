; NAME:
;   CUBE
;
; PURPOSE:
;   This function creates a cube shaped 3D polygon
;     and returns its object reference
;   This function can be used in Object Graphics and New Graphics
;
; AUTHOR:
;   Sangwoo Lee, Ph.D.
;   SELab, Inc.
;   Seoul, Korea
;   Phone: 82-10-3727-1172
;   E-mail: lee@spweather.com
;
; USAGE:
;   obj = CUBE()
;   p = PLOT3D(~~~, SYM_OBJECT=CUBE(), ~~~)
;
; RETURN VALUE:
;   object reference to a cube polygon
;
; ARGUMENTS:
;   None
;
; Keywords:
;   None
;
; MODIFICATION HISTORY:
;   First written on Feb 13, 2017.
;
;******************************************************************************************
;  Copyright (c) 2017, by Sangwoo Lee and SELab, Inc.               ;
;  All rights reserved.
;******************************************************************************************

FUNCTION CUBE

arr = [[0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
MESH_OBJ, 5, vertices, polygons, TRANSPOSE(arr), P2=[0, 0, 1]
polygons = [polygons, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8]
oPolygon = OBJ_NEW('IDLgrPolygon', DATA=vertices, POLYGONS=polygons)

RETURN, oPolygon

END