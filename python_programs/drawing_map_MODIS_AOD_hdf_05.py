#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:47:09 2018

@author: guitar79
"""

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Created on Sat Nov  3 20:34:47 2018
@author: guitar79
created by Kevin 

#Open hdf file
NameError: name 'SD' is not defined
conda install -c conda-forge pyhdf=0.9.0
#basemap
conda install -c conda-forge basemap-data-hires
conda install -c conda-forge basemap
'''

from glob import glob
import numpy as np
from datetime import datetime
import calendar
import os
from pyhdf.SD import SD, SDC
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cht_start_time=datetime.now()

# some variables for downloading (site, file, perid and time gap, etc.)
proc_start_date = '20160101' #start date
proc_end_date = '20160101' #end date
start_date = datetime(int(proc_start_date[:4]), int(proc_start_date[4:6]), int(proc_start_date[6:8])) #convert startdate to date type
end_date = datetime(int(proc_end_date[:4]), int(proc_end_date[4:6]), int(proc_end_date[6:8])) #convert startdate to date type
duration = (end_date - start_date).days + 1 #total days for working

dir_name = 'DAAC_MOD04_3K/all/'
save_dir_name = 'DAAC_MOD04_3K/save/'
if not os.path.exists(save_dir_name):
    os.makedirs(save_dir_name)
    print ('*'*80)
    print (save_dir_name, 'is created')
else :
    print ('*'*80)
    print (save_dir_name, 'is exist')
#f_name = 'MYD04_3K.A2016366.0440.006.2017010010311.hdf'

#write log file
add_log = open(save_dir_name + proc_start_date + '_' + proc_end_date + '.log', 'a')

#JulianDate_to_date(2018, 131) -- '20180511'
def JulianDate_to_date(y, jd):
    month = 1
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month += 1
    #return datetime(y, month, jd).strftime('%Y%m%d')
    return datetime(y, month, jd)

#date_to_JulianDate('20180201', '%Y%m%d') -- 2018032
def date_to_JulianDate(dt, fmt):
    dt = datetime.strptime(dt, fmt)
    tt = dt.timetuple()
    return int('%d%03d' % (tt.tm_year, tt.tm_yday))

#for modis hdf file
#filename = 'DAAC_MOD04_3K/H28V05/MOD04_3K.A2014003.0105.006.2015072123557.hdf'
def filename_to_datetime(filename):
    fileinfo = filename.split('.')
    #print('fileinfo', fileinfo)
    return JulianDate_to_date(int(fileinfo[1][1:5]), int(fileinfo[1][5:8]))

#Set lon, lat, resolution
Llon, Rlon = 90, 150
Slat, Nlat = 10, 60
resolution = 0.05
fac = 1./resolution

#Make Grid
print('='*80)
print(datetime.now(), proc_start_date, '-', proc_end_date, 'Start making grid arrays...')
add_log.write('%s: %s-%s Start making grid arrays...\n' % (datetime.now(), proc_start_date, proc_end_date))

ni = np.int((Rlon-Llon)/resolution+1.00)
nj = np.int((Nlat-Slat)/resolution+1.00)

lon_array = []
lat_array = []
data_array = []   
mean_array = [] 
cnt_array = [] 
for i in range(ni):
    lon_line = []
    lat_line = []
    data_line = []
    mean_line = [] 
    cnt_line = [] 
    for j in range(nj):
        lon_line.append(Llon+resolution*i)
        lat_line.append(Nlat-resolution*j)
        data_line.append([])
        mean_line.append([])
        cnt_line.append([])
    lon_array.append(lon_line)
    lat_array.append(lat_line)
    data_array.append(data_line)
    mean_array.append(mean_line)
    cnt_array.append(cnt_line)
lat_array = np.array(lat_array)
lon_array = np.array(lon_array)
print('grid arrays are created')

#data_array = np.array(data_array)
print('='*80)
print(datetime.now(), proc_start_date, '-', proc_end_date, 'Finish making grid array...')
working_time = (datetime.now() - cht_start_time) #total days for downloading
print(datetime.now(), 'working time (sec) :', working_time)
print('='*80) 


    
cnt = 0
kk=0

for k in sorted(glob(os.path.join(dir_name, '*.hdf'))):

    result_array = data_array
    file_date = filename_to_datetime(k)
    #print('fileinfo', file_date)
    
    if file_date >= start_date \
        and file_date <= end_date : \
        
        print('='*80)
        print(datetime.now(), proc_start_date, '-', proc_end_date, 'Start reading HDF file and extract Longitude, Latitude and AOD value', k)
        add_log.write('%s: %s-%s %s...\n              Start reading HDF file and extract Longitude, Latitude and AOD value\n' % (datetime.now(), proc_start_date, proc_end_date, k))
        hdf = SD(k, SDC.READ)
                
        # Read AOD dataset.
        DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'
        hdf_raw = hdf.select(DATAFIELD_NAME)
        aod_data = hdf_raw[:,:]
        scale_factor = hdf_raw.attributes()['scale_factor']
        add_offset = hdf_raw.attributes()['add_offset']
        aod = aod_data * scale_factor + add_offset
        aod[aod < 0] = np.nan
        aod = np.asarray(aod)
        
        # Read geolocation dataset.
        lat = hdf.select('Latitude')
        latitude = lat[:,:]
        lon = hdf.select('Longitude')
        longitude = lon[:,:]
        
        print('='*80)
        print(datetime.now(), proc_start_date, '-', proc_end_date, longitude.min(), longitude.max(), latitude.min(), latitude.max())

        print('Finish reading HDF file and extract Longitude, Latitude and AOD value')    
        print('='*80)
        
        print('='*80)
        print('Longitude, Latitude and AOD values will be insert to the grid', k)
        add_log.write('%s: %s-%s %s...\n              Longitude, Latitude and AOD values will be insert to the grid..\n' % (datetime.now(), proc_start_date, proc_end_date, k))
        if np.shape(longitude) != np.shape(latitude) or np.shape(latitude) != np.shape(aod) :
            print('data shape is different!!')
            print('='*80)
        else : 
            lon_cood = np.array(((longitude-Llon)/resolution*100//100), dtype=np.uint16)
            lat_cood = np.array(((Nlat-latitude)/resolution*100//100), dtype=np.uint16)
        
            for i in range(np.shape(lon_cood)[0]) :
                for j in range(np.shape(lon_cood)[1]) :
                    if int(lon_cood[i][j]) < np.shape(lon_array)[0] \
                        and int(lat_cood[i][j]) < np.shape(lon_array)[1] \
                        and not np.isnan(aod[i][j]) :
                        cnt += 1 #for debug
                        #print('file : ', kk, 'cnt1 :' , cnt)
                        result_array[int(lon_cood[i][j])][int(lat_cood[i][j])].append(aod[i][j])
            print('='*80)
            print(datetime.now(), proc_start_date, '-', proc_end_date, 'Finish inserting Longitude, Latitude and AOD values to the grid')
            print('='*80)
            kk += 1
        print('file : ', kk, 'cnt1 :' , cnt)
        #if kk == 10 : break

    
working_time = (datetime.now() - cht_start_time) #total days for downloading
print(datetime.now(), 'working time (sec) :', working_time)
print('='*80)   
  

print('='*80)
print(datetime.now(), proc_start_date, '-', proc_end_date, 'Calculating mean value at each pixel is being started ')
add_log.write('%s: %s-%s Calculating mean value at each pixel is being started ...\n' % (datetime.now(), proc_start_date, proc_end_date))
cnt2 = 0 #for debug
for i in range(np.shape(result_array)[0]):
    for j in range(np.shape(result_array)[1]):
        cnt2 += 1 #for debug
        if len(result_array[i][j])>0: mean_array[i][j] = np.mean(result_array[i][j])
        else : mean_array[i][j] = np.nan
        cnt_array[i][j] = len(result_array[i][j])
    print('cnt2 :' , cnt2)
    
mean_array = np.array(mean_array)
cnt_array = np.array(cnt_array)
print(np.shape(mean_array))

print('='*80)
print(datetime.now(), proc_start_date, '-', proc_end_date, 'Calculating mean value at each pixel is finished ')
print('='*80)
add_log.write('%s: %s-%s Calculating mean value at each pixel is finished ...\n' % (datetime.now(), proc_start_date, proc_end_date))


working_time = (datetime.now() - cht_start_time) #total days for downloading
print(datetime.now(), 'working time (sec) :', working_time)
print('='*80)   

#Plot data on the map
print('='*80)
print(datetime.now(), proc_start_date, '-', proc_end_date, 'Plotting data on the map')
plt.figure(figsize=(10, 10))

# sylender map
m = Basemap(projection='cyl', resolution='h', \
            llcrnrlat = Slat, urcrnrlat = Nlat, \
            llcrnrlon = Llon, urcrnrlon = Rlon)
m.drawcoastlines(linewidth=0.25)
m.drawcountries(linewidth=0.25)
#m.fillcontinents(color='coral',lake_color='aqua')
#m.drawmapboundary(fill_color='aqua')

m.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 15.), labels=[0, 0, 0, 1])

x, y = m(lon_array, lat_array) # convert to projection map

plt.pcolormesh(x, y, mean_array)
plt.colorbar(cmap='bwr', fraction=0.038, pad=0.04)

plt.title('MODIS AOD', fontsize=20)
plt.savefig(save_dir_name+'_'+proc_start_date+'-'+proc_end_date+'.png', bbox_inches='tight', dpi = 300)

working_time = (datetime.now() - cht_start_time) #total days for downloading
print(datetime.now(), proc_start_date, '-', proc_end_date, 'Map(image) is created ')
add_log.write('%s: %s-%s Map(image) is created...\n' % (datetime.now(), proc_start_date, proc_end_date))
print(datetime.now(), 'working time (sec) :', working_time)
print('='*80) 

plt.show()

'''
# Create an HDF file
#https://hdfeos.org/software/pyhdf.php
sd = SD(save_dir_name+"hello.hdf", SDC.WRITE | SDC.CREATE)

# Create a dataset
sds = sd.create('AOD_mean', SDC.INT16, np.shape(mean_array))

# Fill the dataset with a fill value
sds.setfillvalue(0)

# Set dimension names
dim1 = sds.dim(0)
dim1.setname("row")
dim2 = sds.dim(1)
dim2.setname("col")

# Assign an attribute to the dataset
sds.units = "Degree"

# Write data
sds = mean_array

# Close the dataset
sds.endaccess()

# Flush and close the HDF file
sd.end()
---------------------------------------------
;PRO MODIS_make_daily

@MODIS_L2_AOD_READ

;; ============================================
;; * Time Domain

    smonth  = 01
    sday    = 01
    syear   = 2015
    sjul    = julday(smonth, sday, syear)

    emonth  = 12
    eday    = 31 
    eyear   = 2016
    ejul    = julday(emonth, eday, eyear)

;; ============================================
;; * PATH

	modispath   = '/media/guitar79/8T/RS_data/MODIS/DAAC_MOD04_3K/all/'
	workpath	= '/media/guitar79/8T/RS_data/Remote_Sensing/2017RNE/MODIS_READ/Result_daily_025_eps/'

;; ==============================================
;; * Make Grid

    Slat = 20
    Nlat = 50
    Llon  =100
    Rlon = 150

    del = 0.25
    fac = 1./del

    ni = (Rlon-Llon)/del+1.
    nj = (Nlat-Slat)/del+1.

    lat = fltarr(ni,nj)
    lon = fltarr(ni,nj)
    for j = 0, nj-1 do lat(*,j) = Nlat-del*j
    for i = 0, ni-1 do lon(i,*) = Llon+del*i

;; ============================================
;; * READ MODIS file

for jul = sjul, ejul do begin ;;각 날짜별로 돌린다.

    caldat, jul, mm, dd, yy
    stdjul = julday(01,01,yy)
    dayn = jul-stdjul+1.

    yyst	= string(yy,'(I4.4)')
    mmst	= string(mm,'(I2.2)')
    ddst	= string(dd,'(I2.2)')
    julst	= string(dayn,'(I3.3)')

	modisname  = modispath+'MOD04_3K.A'+yyst+julst ;;파일 이름 특성상 하루 분량의 데이터를 읽게된다.
;;	file	= file_search(modispath, 'MOD04_3K.A'+yyst+julst+'*.hdf', count = modisfilen)
	file       = file_search(modisname+'*.hdf', count = modisfilen) ;;하루 치 파일을 읽음. modisfilen개이다.

	if modisfilen lt 1 then begin
    	print,'====================================='
    	print,'Cannot find MODIS L2 file:'+modisname
    	print,'====================================='
	endif else begin
	
		;; ---------------
		;; READ MODIS data
		modaod_day = fltarr(ni,nj,modisfilen) & modaod_day(*,*,*) = !values.f_nan

		for ff = 0, modisfilen-1 do begin ;;각 파일별로 for문을 돌린다.

			MODIS_L2_AOD_READ,file=file(ff),aod=modaod,lat=modlat,lon=modlon
			locidx = where(modaod gt -1 and modlat gt Slat and modlat le Nlat and modlon gt Llon and modlon le Rlon, locnum)

			if locnum lt 10 then begin
    			print,'====================================='
    			print,'Cannot find Collodated data :'+file(ff)
    			print,'====================================='
			endif else begin

				mdlat_r = round(modlat(locidx)/del)*del
				mdlon_r = round(modlon(locidx)/del)*del

				for jj = 0., nj-1 do begin
				yidx = nlat-jj*del
				ygrid = where(mdlat_r gt yidx-0.01 and mdlat_r lt yidx+0.01, ynum)
				if ynum gt 0 then begin
				
				    for ii = 0., ni-1 do begin
				        xidx = llon+ii*del
				        xgrid = where(mdlon_r(ygrid) ge xidx-0.01 and mdlon_r(ygrid) le xidx+0.01,xnum)
				        if xnum gt 0 then begin
				            data = modaod(locidx(ygrid(xgrid)))
				            dum = where(data lt 5,nanc)
				            if nanc gt fix(xnum*0.5) then begin
				                result = moment(data(dum),/nan,sdev = std)
				                if result(0) gt 0 then begin
				                modaod_day(ii,jj,ff) = result(0) ;;하루치 파일들의 셀 별 값이다.
				                endif
				            endif
				        endif
				    endfor
				
				endif
				endfor

			endelse
		endfor	;; MODIS file for a day

                modaod_fin = fltarr(ni, nj) & modaod_fin(*,*) = !values.f_nan
                for jj = 0., nj-1 do begin
                for ii = 0., ni-1 do begin
                    modaod_fin(ii,jj) = mean(modaod_day(ii,jj,*),/nan) ;;하루치 값들을 셀 별로 평균내어 하나의 array로 만든다.
                endfor
                endfor

                set_plot,'ps'
                !p.font=0

                filename = workpath + 'MODIS_DayAOD'+yyst+julst+'.eps'

                minv = 0.0
                maxv = 2.0

                loadct,39,/silent
                device, /encapsulated, /color, bits_per_pixel = 8, filename = filename, $
                  /helvetica, /bold, font_size = 18, xs = 25, ys = 20
                map_set,limit = [Slat,Llon,Nlat,Rlon],color=-1 ,/isotropic,xmargin=[5,5],ymargin=[3,3]
                xyouts,0.5,0.9,'MODIS AOD'+yyst+julst,charsize=1.1,color=1,align=0.5,/normal
                loadct,33,/silent
                aodcolor = bytscl(modaod_fin,min=minv,max=maxv,top=254)

                for jj = 0, nj-2 do begin
                  for ii = 0, ni-2 do begin
                    if modaod_fin(ii,jj) gt -1 then begin
                      xx = [lon(ii,jj),lon(ii+1,jj),lon(ii+1,jj+1),lon(ii,jj+1),lon(ii,jj)]
                      yy = [lat(ii,jj),lat(ii+1,jj),lat(ii+1,jj+1),lat(ii,jj+1),lat(ii,jj)]
                      polyfill,xx,yy,color=aodcolor(ii,jj),/fill
                    endif
                  endfor
                endfor

                cgcolorbar,position=[0.1,0.08,0.9,0.10], minrange=minv, maxrange=maxv, divisions=5, format = '(f5.2)', $
                  color = 'black', ncolors = 254,charsize=0.8

                loadct,39,/silent
                map_continents,/continents,/countries,/coast, color=0, thick=1
                map_grid,/box,latdel=5,londel=5,color=0,charsize=0.8, thick = 1
                device,/close

              endelse
            endfor    ;; julian date
          END

          set_plot,'ps'
          !p.font=0

          filename = workpath + 'MODIS_DayAOD'+yyst+julst+'.eps'

          minv = 0.0
          maxv = 2.0

          loadct,39,/silent
          device, /encapsulated, /color, bits_per_pixel = 8, filename = filename, $
            /helvetica, /bold, font_size = 18, xs = 25, ys = 20
          map_set,limit = [Slat,Llon,Nlat,Rlon],color=-1 ,/isotropic,xmargin=[5,5],ymargin=[3,3]
          xyouts,0.5,0.9,'MODIS AOD'+yyst+julst,charsize=1.1,color=1,align=0.5,/normal
          loadct,33,/silent
          aodcolor = bytscl(modaod_fin,min=minv,max=maxv,top=254)

          for jj = 0, nj-2 do begin
            for ii = 0, ni-2 do begin
              if modaod_fin(ii,jj) gt -1 then begin
                xx = [lon(ii,jj),lon(ii+1,jj),lon(ii+1,jj+1),lon(ii,jj+1),lon(ii,jj)]
                yy = [lat(ii,jj),lat(ii+1,jj),lat(ii+1,jj+1),lat(ii,jj+1),lat(ii,jj)]
                polyfill,xx,yy,color=aodcolor(ii,jj),/fill
              endif
            endfor
          endfor

          cgcolorbar,position=[0.1,0.08,0.9,0.10], minrange=minv, maxrange=maxv, divisions=5, format = '(f5.2)', $
            color = 'black', ncolors = 254,charsize=0.8

          loadct,39,/silent
          map_continents,/continents,/countries,/coast, color=0, thick=1
          map_grid,/box,latdel=5,londel=5,color=0,charsize=0.8, thick = 1
          device,/close

        endelse
    
    OPENW, filevar, workpath+yyst+julst+'.txt', /GET_LUN
    for ii=0, ni-1 do begin
      for jj=0, nj-1 do begin
        printf, filevar, Nlat+del*jj, Llon+del*ii, modaod_fin(ii,jj)
      endfor
    endfor
    FREE_LUN, filevar
      
		print, jul
			
	endelse
endfor		;; julian date
END


'''
