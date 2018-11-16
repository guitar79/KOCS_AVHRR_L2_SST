PRO test_ng_map_data

fig_sav = 0

data = HANNING(300, 300)*100
lons = 120+FINDGEN(300)*0.05
lats = 30+FINDGEN(300)*0.05
sz = SIZE(data, /DIM)
w = WINDOW(DIMENSIONS=sz, /NO_TOOLBAR)
i = IMAGE(data, MARGIN=0, RGB_TABLE=74, /CURRENT)

win = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)
limit = [30, 120, 45, 135]
m = MAP('Geographic', LIMIT=limit, ASPECT_RATIO=0, MARGIN=0.1, /CURRENT)
;m = MAP('Geographic', LIMIT=limit, ASPECT_RATIO=0, $
;  POSITION=[0.08, 0.14, 0.92, 0.98], /CURRENT)
;m = MAP('Lambert Conformal Conic', LIMIT=limit, $
;  STANDARD_PAR1=30, STANDARD_PAR2=60, $
;  ASPECT_RATIO=0, POSITION=[0.06, 0.20, 0.94, 0.96], /CURRENT)
;im = IMAGE(data, RGB_TABLE=74, IMAGE_DIMENSIONS=[15, 15], $
;  IMAGE_LOCATION=[120, 30], GRID_UNITS=2, /OVERPLOT)
im = IMAGE(data, lons, lats, RGB_TABLE=74, GRID_UNITS=2, ASPECT_RATIO=0, /OVERPLOT)
conv = [20, 30, 50, 60, 80]
cn = CONTOUR(data, lons, lats, C_VALUE=conv, RGB_TABLE=74, FILL=0, C_THICK=2, $
  C_LABEL_SHOW=1, LABEL_COLOR='black', GRID_UNITS=2, /OVERPLOT)
;cno = CONTOUR(data, lons, lats, C_VALUE=conv, COLOR='black', C_THICK=2, $
;  C_LABEL_SHOW=1, GRID_UNITS=2, /OVERPLOT)
mc = MAPCONTINENTS('data/GSHHS_i_L1.shp', THICK=2)
mg = m.MapGrid
mg.Linestyle = 2
mg.LABEL_POSITION = 0
mg.Font_Size = 12
mg.Clip = 0
;cb = COLORBAR(TARGET=im, TITLE='Value', FONT_SIZE=12, POSITION=[0.2, 0.07, 0.8, 0.10])
IF fig_sav THEN win.Save, 'figures/ng_map_data.png', WIDTH=600

END