PRO test_ng_surface_video

video_sav = 0

data = HANNING(400, 400)*0
scx = 600
scy = 600
win = WINDOW(DIMENSIONS=[scx, scy])
s = SURFACE(data, COLOR='crimson', ZRANGE=[-1, 1], ASPECT_Z=300, $
  AXIS_STYLE=0, /CURRENT)
s.Scale, 1.5, 1.5, 1.5
nstep = 60
theta = -FINDGEN(nstep+1)*360./nstep

IF video_sav THEN BEGIN
  vfile = 'figures/anim_surface.mp4'
  fps = 60
  oVid = IDLffVideoWrite(vfile)
  vidStream = oVid.AddVideoStream(scx, scy, fps)
ENDIF

FOR j = 0, nstep/2-1 DO BEGIN
  tmp = HANNING(400, 400)*SIN(theta[j]*!DTOR)
  s.SetData, tmp
  IF video_sav THEN time = oVid.Put(vidStream, win.CopyWindow(WIDTH=scx))
ENDFOR
FOR j = nstep/2, nstep DO BEGIN
  tmp = HANNING(400, 400)*SIN(theta[j]*!DTOR)
  s.SetData, tmp
  IF video_sav THEN time = oVid.Put(vidStream, win.CopyWindow(WIDTH=scx))
ENDFOR
IF video_sav THEN oVid.CleanUp

END