PRO MODIS_L2_AOD_READ_FILE
;--PRO MODIS_L2_AOD_READ_FILE, file=file, aod=aod, lat=lat, lon=lon

modispath	= 'C:\KH_data\Github\MODIS_AOD\IDL_program\data\'
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

    set_plot,'x'
    loadct,39
    device,decomposed=0
    locidx = where(lat gt 20 and lat le 50 and lon gt 100 and lon le 145, locnum)
    imagemap, aod(locidx), lat(locidx), lon(locidx), range=[0,2]
    map_continents,/countries,/continents,color=0
    map_grid,/box,latdel=5,londel=5

  endelse 

END
