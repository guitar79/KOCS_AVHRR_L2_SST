PRO test_ng_plot_video

video_sav = 0

x = FINDGEN(361)
y = SIN(x*!DTOR)
scx = 600
scy = 600
win = WINDOW(DIMENSIONS=[scx, scy])
p = PLOT(x, y, XRANGE=[0, 360], YRANGE=[-1, 1], XTICKINTERVAL=90, COLOR='green', $
  THICK=3, /CURRENT)

IF video_sav THEN BEGIN
  vfile = 'figures/anim_plot.mp4'
  fps = 30
  oVid = IDLffVideoWrite(vfile)
  vidStream = oVid.AddVideoStream(scx, scy, fps)
ENDIF

amps = [1.0:-1.0:-0.04]
HELP, amps
FOR j = 0, N_ELEMENTS(amps)-1 DO BEGIN
  y = SIN(x*!DTOR)*amps[j]
  p.SetData, x, y
  cap = win.CopyWindow(WIDTH=scx)
  IF video_sav THEN time = oVid.Put(vidStream, cap)
ENDFOR
IF video_sav THEN oVid.CleanUp

END