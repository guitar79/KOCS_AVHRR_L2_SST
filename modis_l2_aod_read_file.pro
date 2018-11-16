PRO MODIS_L2_AOD_READ_FILE
;--PRO MODIS_L2_AOD_READ_FILE, file=file, aod=aod, lat=lat, lon=lon

modispath	= 'C:\KH_data\Github\MODIS_AOD\IDL_program\AOD_hdf\'
modisname	= 'MOD04_3K.A2015001.0045.006.2015032234339.hdf'
file 		= file_search(modispath+modisname, count = modisfilen)

if modisfilen lt 1 then begin

print,'====================================='
print,'Cannot find MODIS L2 file:'+modisname
print,'====================================='

endif else begin

	hdfid = hdf_sd_start(file(0))
	hdf_sd_readonly,hdfid,'Optical_Depth_Land_And_Ocean',aod
	hdf_sd_readonly,hdfid,'Longitude',lon
	hdf_sd_readonly,hdfid,'Latitude',lat
	
	scale_factor = hdf_sd_attinfo(hdfid,'Optical_Depth_Land_And_Ocean','scale_factor')
	offset = hdf_sd_attinfo(hdfid,'Optical_Depth_Land_And_Ocean','add_offset')
	hdf_sd_end,hdfid
	
	aod = (aod + offset.data(0))*scale_factor.data(0)
	nan = where(aod le 0. or aod ge 5.,nanc)
	
	if nanc gt 0 then aod(nan) = !values.f_nan

  what = 3; (1~3)
  CASE what OF
    1 : BEGIN
  
      set_plot,'ps'
      loadct,39
      device,decomposed=0
      locidx = where(lat gt 20 and lat le 50 and lon gt 100 and lon le 145, locnum)
      imagemap, aod(locidx), lat(locidx), lon(locidx), range=[0,2]
      map_continents,/countries,/continents,color=0
      map_grid,/box,latdel=5,londel=5

    END
    
     2 : BEGIN
        ;data = HANNING(400, 400)
        data = aod
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
        ;im = IMAGE(data, RGB_TABLE=74, IMAGE_DIMENSIONS=[15, 15], $
        ;  IMAGE_LOCATION=[120, 30], GRID_UNITS=2, /OVERPLOT)
        mc = MAPCONTINENTS('data/GSHHS_i_L1.shp', THICK=2)
        mg = m.MapGrid
        mg.Linestyle = 2
        mg.LABEL_POSITION = 0
        mg.Font_Size = 12
        mg.Clip = 0
        ;cb = COLORBAR(TARGET=im, TITLE='Value', FONT_SIZE=12, POSITION=[0.2, 0.07, 0.8, 0.10])
        IF fig_sav THEN win.Save, 'output/test_map_draw_06.png', WIDTH=600
    END

    3 : BEGIN
      
      fig_sav = 0

    ;    data = HANNING(300, 300)*100
    ;    lons = 120+FINDGEN(300)*0.05
    ;    lats = 30+FINDGEN(300)*0.05
        data = aod
        lons = lon
        lats = lat
        sz = SIZE(data, /DIM)
        w = WINDOW(DIMENSIONS=sz, /NO_TOOLBAR)
        i = IMAGE(data, MARGIN=0, RGB_TABLE=74, /CURRENT)
    
        win = WINDOW(DIMENSIONS=[1200, 1200], /NO_TOOLBAR)
        limit = [20, 100, 65, 150]
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
        cno = CONTOUR(data, lons, lats, C_VALUE=conv, COLOR='black', C_THICK=2, $
          C_LABEL_SHOW=1, GRID_UNITS=2, /OVERPLOT)
        mc = MAPCONTINENTS('data/GSHHS_i_L1.shp', THICK=2)
        mg = m.MapGrid
        mg.Linestyle = 2
        mg.LABEL_POSITION = 0
        mg.Font_Size = 12
        mg.Clip = 0
        cb = COLORBAR(TARGET=im, TITLE='Value', FONT_SIZE=12, $
          POSITION=[0.2, 0.07, 0.8, 0.10])
        ;IF fig_sav eq 0 THEN win.Save, 'figures/ng_map_data.png', WIDTH=600
        IF fig_sav eq 0 THEN win.Save, 'figures/ng_map_data.eps'

      END
    
    ENDCASE
  
endelse 

END
