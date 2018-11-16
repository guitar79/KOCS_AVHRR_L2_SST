PRO test_ng_map_draw

what = 6; (1~6)
fig_sav = 0

CASE what OF

1 : BEGIN
win = WINDOW(DIMENSIONS=[800, 450])
m = MAP('Geographic', FILL_COLOR='Light Blue', ASPECT_RATIO=0, MARGIN=0.05, /CURRENT)
mc = MAPCONTINENTS(FILL_COLOR='Gold', THICK=2)
;m.LIMIT = [20, 120, 60, 150]
mg = m.MapGrid
;mg.Linestyle = 2
;mg.LABEL_POSITION = 0
IF fig_sav THEN win.Save, 'output/test_map_draw_01.png', WIDTH=800
END

2 : BEGIN
win = WINDOW(DIMENSIONS=[800, 500])
m = MAP('Mercator', LIMIT=[33, 124, 43, 133], FILL_COLOR='Light Blue', $
  ASPECT_RATIO=1, MARGIN=0.08, /CURRENT)
;mc = MAPCONTINENTS(FILL_COLOR='Gold', THICK=2, /HIRES)
mc = MAPCONTINENTS('data/GSHHS_i_L1.shp', FILL_COLOR='Gold', THICK=2)
mg = m.MapGrid
;mg.Linestyle = 2
;mg.LABEL_POSITION = 0
IF fig_sav THEN win.Save, 'output/test_map_draw_02.png', WIDTH=800
END

3 : BEGIN
win = WINDOW(DIMENSIONS=[800, 500])
m = MAP('Lambert Conformal Conic', LIMIT=[20, 100, 60, 160], $
  ;STANDARD_PAR1=30, STANDARD_PAR2=60, $   ;conic 
  ;FILL_COLOR='Light Blue', ASPECT_RATIO=0, MARGIN=0.1, /CURRENT)
  STANDARD_PAR1=30, STANDARD_PAR2=60, $   ;conic
  FILL_COLOR='Light Blue', ASPECT_RATIO=0, MARGIN=0.1, CLIP=0,/CURRENT)
mc = MAPCONTINENTS(FILL_COLOR='Gold', THICK=2)
mg = m.MapGrid
;mg.Linestyle = 2
mg.LABEL_POSITION = 0
;mg.Grid_Latitude = 5
;mg.Grid_Longitude = 5
IF fig_sav THEN win.Save, 'output/test_map_draw_03.png', WIDTH=800
END

4 : BEGIN
win = WINDOW(DIMENSIONS=[600, 600]*2)
m = MAP('Polar Stereographic', CENTER_LATITUDE=90, $
  FILL_COLOR='Dodger Blue', ASPECT_RATIO=0, MARGIN=0.05, $
  LIMIT=[-90,-180,90,180], /CURRENT)
mc = MAPCONTINENTS(FILL_COLOR='Orange', THICK=2)
mg = m.MapGrid
;mg.Linestyle = 2
IF fig_sav THEN win.Save, 'output/test_map_draw_04.png', WIDTH=600
END

5 : BEGIN
win = WINDOW(DIMENSIONS=[800, 500])
m = MAP('Lambert Conformal Conic', LIMIT=[30, 110, 50, 140], $
  STANDARD_PAR1=30, STANDARD_PAR2=60, $
  FILL_COLOR='Dodger Blue', ASPECT_RATIO=0, MARGIN=0.1,  CLIP=0, /CURRENT)
mc = MAPCONTINENTS(FILL_COLOR='Gold', THICK=2)
mg = m.MapGrid
;mg.Linestyle = 2
mg.LABEL_POSITION = 0
sym = SYMBOL(126.97, 37.57, 'square', /DATA, $
  SYM_COLOR='black', /SYM_FILLED, SYM_FILL_COLOR='crimson')
;tx = TEXT(126.97, 37.57, 'Seoul', /DATA, FONT_STYLE='bold')
tx = TEXT(126.97, 37.90, 'Seoul', /DATA, FONT_STYLE='bold', $
  /FILL_BACKGROUND, FILL_COLOR='white', ALIGNMENT=0.5)
;sym = SYMBOL(116.38, 39.92, 'square', /DATA, $
;  SYM_COLOR='black', /SYM_FILLED, SYM_FILL_COLOR='crimson')
;tx = TEXT(116.38, 40.25, 'Beijing', /DATA, FONT_STYLE='bold', $
;  /FILL_BACKGROUND, FILL_COLOR='white', ALIGNMENT=0.5)
;line = POLYLINE([126.97, 116.38], [37.57, 39.92], /DATA, COLOR='crimson', THICK=2)
IF fig_sav THEN win.Save, 'output/test_map_draw_05.png', WIDTH=800
END

6 : BEGIN
data = HANNING(400, 400)
sz = SIZE(data, /DIM)
w = WINDOW(DIMENSIONS=sz)
i = IMAGE(data, MARGIN=0, RGB_TABLE=74, /CURRENT)
win = WINDOW(DIMENSIONS=[600, 600])
limit = [30, 120, 45, 135]
limit_large = [25, 115, 50, 140]
m = MAP('Geographic', LIMIT=limit, ASPECT_RATIO=0, MARGIN=0.1, /CURRENT)
;m = MAP('Geographic', LIMIT=limit, ASPECT_RATIO=0, $
;  POSITION=[0.08, 0.14, 0.92, 0.98], /CURRENT)
;m = MAP('Lambert Conformal Conic', LIMIT=limit, $
;  STANDARD_PAR1=30, STANDARD_PAR2=60, $
;  ASPECT_RATIO=0, POSITION=[0.06, 0.20, 0.94, 0.96], /CURRENT)
im = IMAGE(data, RGB_TABLE=74, IMAGE_DIMENSIONS=[15, 15], $
  IMAGE_LOCATION=[120, 30], GRID_UNITS=2, /OVERPLOT)
mc = MAPCONTINENTS('data/GSHHS_i_L1.shp', THICK=2)
mg = m.MapGrid
mg.Linestyle = 2
mg.LABEL_POSITION = 0
mg.Font_Size = 12
mg.Clip = 0
;cb = COLORBAR(TARGET=im, TITLE='Value', FONT_SIZE=12, POSITION=[0.2, 0.07, 0.8, 0.10])
IF fig_sav THEN win.Save, 'output/test_map_draw_06.png', WIDTH=600
END

ENDCASE

END