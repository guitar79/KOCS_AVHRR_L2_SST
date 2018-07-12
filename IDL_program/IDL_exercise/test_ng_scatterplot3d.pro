PRO test_ng_scatterplot3d

fig_sav = 0

n = 20
x = RANDOMU(seed, n)*10
y = RANDOMU(seed, n)*10
z = RANDOMU(seed, n)*10
value = RANDOMU(seed, n)*100
PRINT, MIN(value), MAX(value)

win1 = WINDOW(DIMENSIONS=[600, 500])
pl1 = SCATTERPLOT3D(x, y, z, CLIP=0, AXIS_STYLE=2, $
  XRANGE=[0, 10], YRANGE=[0, 10], ZRANGE=[0, 10], $
  SYM_SIZE=2, SYM_OBJECT=ORB(), SYM_COLOR='crimson', MARGIN=0.2, /CURRENT)
IF fig_sav THEN win1.Save, 'figures/ng_scatterplot3d_1.png', WIDTH=600

win2 = WINDOW(DIMENSIONS=[600, 500])
pl2 = SCATTERPLOT3D(x, y, z, CLIP=0, AXIS_STYLE=2, $
  XRANGE=[0, 10], YRANGE=[0, 10], ZRANGE=[0, 10], $
  SYM_SIZE=2, SYM_OBJECT=ORB(), RGB_TABLE=67, $
  MAGNITUDE=BYTSCL(value, MIN=0, MAX=100), $
  MARGIN=0.2, /CURRENT)
IF fig_sav THEN win2.Save, 'figures/ng_scatterplot3d_2.png', WIDTH=600

win3 = WINDOW(DIMENSIONS=[600, 600])
pl3 = SCATTERPLOT3D(x, y, z, CLIP=0, AXIS_STYLE=2, $
  XRANGE=[0, 10], YRANGE=[0, 10], ZRANGE=[0, 10], $
  SYM_SIZE=2, SYM_OBJECT=ORB(), RGB_TABLE=67, $
  MAGNITUDE=BYTSCL(value, MIN=0, MAX=100), $
  MARGIN=[0.2, 0.3, 0.2, 0.2], /CURRENT)
cb = COLORBAR(TARGET=pl3, TITLE='Value', RANGE=[0, 100], FONT_SIZE=10, $
  POSITION=[0.2, 0.07, 0.8, 0.10], /BORDER)
IF fig_sav THEN win3.Save, 'figures/ng_scatterplot3d_3.png', WIDTH=600

END