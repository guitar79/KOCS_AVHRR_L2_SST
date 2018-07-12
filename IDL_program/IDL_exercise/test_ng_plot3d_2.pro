PRO test_ng_plot3d_2

fig_sav = 0

t = [0:360:5.]
px = COS(2*t*!DTOR)*4 & PRINT, MIN(px), MAX(px)
py = SIN(2*t*!DTOR)*4 & PRINT, MIN(py), MAX(py)
pz = t/50-3.6 & PRINT, MIN(pz), MAX(pz)
win = WINDOW(DIMENSIONS=[600, 600])
scp = PLOT3D(px, py, pz, AXIS_STYLE=2, THICK=2, COLOR='green', $
  XRANGE=[-5, 5], YRANGE=[-5, 5], ZRANGE=[-5, 5], $
  SYM_OBJECT=CUBE(), SYM_SIZE=3, SYM_COLOR='magenta', $
  XTICKINTERVAL=1, YTICKINTERVAL=1, ZTICKINTERVAL=1, $
  XMINOR=0, YMINOR=0, ZMINOR=0, $
  XTICKLEN=0.02, YTICKLEN=0.02, ZTICKLEN=0.02, $
  ;XY_SHADOW=1, XZ_SHADOW=1, YZ_SHADOW=1, SHADOW_COLOR='light blue', $
  ASPECT_RATIO=1, ASPECT_Z=1, LINESTYLE=6, CLIP=0, $;/PERSPECTIVE, $
  MARGIN=[0.1, 0.1, 0.1, 0.1]*2, /CURRENT)
;scp.AXES[2].HIDE = 1
;scp.AXES[6].HIDE = 1
;scp.AXES[7].HIDE = 1
;scp.AXES[8].SHOWTEXT = 1
;scp.AXES[8].TICKFONT_SIZE = 9

;scpo = PLOT3D(px, py, pz*0-5, LINESTYLE='none', CLIP=0, /OVERPLOT, $
;  SYMBOL='square', SYM_COLOR='gray', /SYM_FILLED, SYM_SIZE=1)

IF fig_sav THEN win.Save, 'figures/ng_plot3d_2.png', WIDTH=600

END