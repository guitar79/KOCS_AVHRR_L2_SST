PRO test_ng_volume

fig_sav = 0

file = FILEPATH('head.dat', SUBDIRECTORY=['examples', 'data'])
data = READ_BINARY(file, DATA_DIMS=[80, 100, 57])
;file = FILEPATH('jet.dat', SUBDIR=['examples', 'data'])
;data = READ_BINARY(file, DATA_DIMS=[81, 40, 101])
HELP, data
PRINT, MIN(data), MAX(data)

win = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)
opa = BINDGEN(256)>255
vol = VOLUME(data, ASPECT_RATIO=1, /CURRENT)
vol.RGB_TABLE0 = 34
;vol.HINTS = 2
;vol.RENDER_QUALITY = 2
;vol.COMPOSITE_FUNCTION = 2

indz = 30; z index to be sliced
slice = data[*, *, indz]
sz = SIZE(slice, /DIM)
win_im = WINDOW(DIMENSIONS=sz*5, /NO_TOOLBAR)
im = IMAGE(slice, MARGIN=0, RGB_TABLE=34, /CURRENT)

IF fig_sav THEN win.Save, 'figures/ng_volume.png', WIDTH=600

END