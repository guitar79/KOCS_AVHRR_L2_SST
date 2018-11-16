PRO test_ng_surface_1

data = HANNING(50, 50)*100
win = WINDOW(DIMENSIONS=[600, 600])
sf = SURFACE(data, COLOR='orange', /CURRENT)

;tx1 = TEXT(0.5, 0.91, 'STYLE = 1', ALIGNMENT=0.5, FONT_SIZE=20, /NORMAL)
;sf.STYLE = 1
;
;tx1.String = 'STYLE = 6'
;sf.STYLE = 6
;
;tx2 = TEXT(0.5, 0.85, 'ASPECT_Z = 1', ALIGNMENT=0.5, FONT_SIZE=20, /NORMAL)
;sf.ASPECT_Z = 1

END