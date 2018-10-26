''' created by Kevin 
 Open hdf file
#NameError: name 'SD' is not defined
#conda install -c conda-forge pyhdf
#conda install -c conda-forge basemap-data-hires
#conda install -c conda-forge basemap
#conda install -c conda-forge matplotlib
'''
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from datetime import datetime
import calendar
import os
from pyhdf.SD import SD, SDC


# some variables for downloading (site, file, perid and time gap, etc.)
startdate = '20150101' #start date
enddate = '20181010' #end date
time_gap = 6 #time gap
request_hour = range(0,24,time_gap) #make list
#request_hour = [0, 3, 6, 9, 12, 15, 18, 21] #make list


def JulianDate_to_date(y, jd):
    month = 1
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month += 1
    return datetime(y, month, jd).strftime('%Y%m%d')
#JulianDate_to_date(2018, 131) -- '20180511'

def date_to_JulianDate(dt, fmt):
    dt = datetime.strptime(dt, fmt)
    tt = dt.timetuple()
    return int('%d%03d' % (tt.tm_year, tt.tm_yday))
#date_to_JulianDate('20180201', '%Y%m%d') -- 2018032

#Make Grid
Slat, Nlat = 20, 50
Llon, Rlon = 150, 100
resolution = 0.25
fac = 1./resolution

ni = np.int((Nlat-Slat)/resolution+1)
nj = np.int((Llon-Rlon)/resolution+1)

array_data = []
for i in range(ni):
    temp = []
    for j in range(nj):
        temp.append({'latitude' : Slat+resolution*i, \
                     'longitude' : Llon-resolution*j, \
                     'data' : []})
    array_data.append(temp)

array_data[ni][nj]['data'].append(data)


dir_name = '/media/guitar79/6TB2/MODIS_AOD/DAAC_MOD04_3K/H28V05/'
f_name = 'MYD04_3K.A2016366.0440.006.2017010010311.hdf'

hdf = SD(dir_name+f_name, SDC.READ)
#print (hdf.datasets())
#print (dir(hdf))
# List available SDS datasets.
#{'Longitude': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 0), 'Latitude': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 1), 'Scan_Start_Time': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 6, 2), 'Solar_Zenith': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 3), 'Solar_Azimuth': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 4), 'Sensor_Zenith': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 5), 'Sensor_Azimuth': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 6), 'Scattering_Angle': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 7), 'Glint_Angle': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 8), 'Land_Ocean_Quality_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 9), 'Land_sea_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 10), 'Wind_Speed_Ncep_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 11), 'Optical_Depth_Land_And_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 12), 'Image_Optical_Depth_Land_And_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 13), 'Aerosol_Type_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 14), 'Fitting_Error_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 15), 'Surface_Reflectance_Land': (('Solution_2_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 676, 451), 22, 16), 'Corrected_Optical_Depth_Land': (('Solution_3_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 676, 451), 22, 17), 'Corrected_Optical_Depth_Land_wav2p1': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 18), 'Optical_Depth_Ratio_Small_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 19), 'Number_Pixels_Used_Land': (('Solution_1_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 20), 'Mean_Reflectance_Land': (('MODIS_Band_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 21), 'STD_Reflectance_Land': (('MODIS_Band_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 22), 'Mass_Concentration_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 23), 'Aerosol_Cloud_Fraction_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 24), 'Quality_Assurance_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04', 'QA_Byte_Land:mod04'), (676, 451, 5), 20, 25), 'Solution_Index_Ocean_Small': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 26), 'Solution_Index_Ocean_Large': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 27), 'Effective_Optical_Depth_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 28), 'Effective_Optical_Depth_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 29), 'Optical_Depth_Small_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 30), 'Optical_Depth_Small_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 31), 'Optical_Depth_Large_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 32), 'Optical_Depth_Large_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 33), 'Mass_Concentration_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 5, 34), 'Aerosol_Cloud_Fraction_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 35), 'Effective_Radius_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 36), 'PSML003_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 5, 37), 'Asymmetry_Factor_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 38), 'Asymmetry_Factor_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 39), 'Backscattering_Ratio_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 40), 'Backscattering_Ratio_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 41), 'Angstrom_Exponent_1_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 42), 'Angstrom_Exponent_2_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 43), 'Least_Squares_Error_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 44), 'Optical_Depth_Ratio_Small_Ocean_0.55micron': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 45), 'Optical_Depth_by_models_ocean': (('Solution_Index:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (9, 676, 451), 22, 46), 'Number_Pixels_Used_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 47), 'Mean_Reflectance_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 48), 'STD_Reflectance_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 49), 'Quality_Assurance_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04', 'QA_Byte_Ocean:mod04'), (676, 451, 5), 20, 50), 'Topographic_Altitude_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 51)}

# Read AOD dataset.
DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'
hdf_raw = hdf.select(DATAFIELD_NAME)
#print(dir(hdf_raw))
#print(dir(hdf_raw.dimensions()))

aod_attri = hdf_raw.attributes()
#print('aod_attri', aod_attri)

aod_data = hdf_raw[:,:]
scale_factor = hdf_raw.attributes()['scale_factor']
add_offset = hdf_raw.attributes()['add_offset']
aod = aod_data * scale_factor + add_offset
aod[aod < 0] = np.nan

# Read geolocation dataset.
lat = hdf.select('Latitude')
latitude = lat[:,:]
lon = hdf.select('Longitude')
longitude = lon[:,:]

longitude, latitude, aod

'''

array_data = []
for i in range(maxlat):
    temp = []
    for j in range(maxlon):
        temp.append({'latitude' : ni, 'longitude' : nj, 'data' : []})
    array_data.append([])

array_data[ni][nj]['data'].append(data)

array_sum = np.zeros((180, 360), dtype=np.float64)
array_cnt = np.zeros((180, 360), dtype=np.int32)
for data in datas:
    x,y,v = get_data(data)
    xx = int(2*x)
    yy = int(2*y)
    array_sum[xx][yy]+=v
    array_cnt[xx][yy]+=1
    
for i in range(180)
#variable for calculating date
start_date = datetime.date(datetime.strptime(startdate, '%Y%m%d')) #convert startdate to date type
end_date = datetime.date(datetime.strptime(enddate, '%Y%m%d')) #convert enddate to date type
duration = (end_date - start_date).days #total days for downloading
print ('*'*80)
#print ((duration+1), 'days', int((duration+1)*(24/time_gap)), 'files will be downloaded')

def filename_to_datetime(filename):
    fileinfo = filename.split('.')
    return datetime.strptime(fileinfo[4]+fileinfo[5], '%Y%m%d%H%M%S')

# Open file.


# Read geolocation dataset.
lat = hdf.select('Latitude')
latitude = lat[:,:]
lon = hdf.select('Longitude')
longitude = lon[:,:]


# sylender map
m = Basemap(projection='cyl', resolution='h', llcrnrlat=10, urcrnrlat = 60, \
llcrnrlon=100, urcrnrlon = 160)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
#x, y = m(longitude, latitude)
#m.pcolormesh(x, y, aod)
m.pcolormesh(longitude, latitude, aod)
plt.colorbar(cmap='bwr', extend='max')
plt.title('MODIS AOD')
plt.savefig(dir_name+f_name+'.png', bbox_inches='tight', dpi = 300)
plt.show()



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
	workpath	= '/media/guitar79/8T/RS_data/Remote_Sensing/2017RNE/MODIS_READ/Result_daily_025_txt/'

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

