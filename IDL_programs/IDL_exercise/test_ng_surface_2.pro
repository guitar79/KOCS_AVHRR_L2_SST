PRO test_ng_surface_2

zdata = READ_BINARY('data/elevbin.dat', DATA_DIMS=[64, 64])
HELP, zdata
PRINT, MIN(zdata), MAX(zdata)
win = WINDOW(DIMENSIONS=[600, 600])

;sf = SURFACE(zdata, YSTYLE=1, /CURRENT)
;sf.Erase

READ_JPEG, 'data/elev_t.jpg', img
print, img
sf = SURFACE(zdata, TEXTURE_IMAGE=img, YSTYLE=1, /CURRENT)

END