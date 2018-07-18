PRO test_ng_surface

data = HANNING(50, 50)*100
win = WINDOW(DIMENSIONS=[800, 800], /NO_TOOLBAR)
sf = SURFACE(data, COLOR='crimson', /CURRENT)
sf.style = 2
;sf.aspect_z=1
END