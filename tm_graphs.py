import geoplot as gplt
import geoplot.crs as gcrs
import geopandas as gpd
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('mvc.csv')
a.head()
type(a)
b = [a['BOROUGH'], a['CRASH DATE']]
c = pd.concat(b, axis=1)
a['CRASH DATE'] = pd.to_datetime(a['CRASH DATE'])
a = a[(a['CRASH DATE'] >= "2021-01-01")]
a.to_csv('collisions.csv')
a = a.dropna()
type(c)
c.columns
c['CRASH DATE'] = pd.to_datetime(c['CRASH DATE'])
a
c = c[(c['CRASH DATE'] >= "2021-01-01")]
d = c.groupby('BOROUGH').agg('count')
z = pd.read_csv('mv_boroughs.csv')

# bar plot for collisions
plt.figure(facecolor='gainsboro')
plt.axes().set_facecolor('gainsboro')
plt.bar(d.index, d['CRASH DATE'],
        color=['darksalmon', 'firebrick', 'salmon', 'red', 'lightcoral'])
plt.title('Collisions')
plt.ylabel("January 2021 - November 2021")
plt.show()

# bar plot to moving violations
plt.figure(facecolor='gainsboro')
plt.axes().set_facecolor('gainsboro')
plt.title('Moving Violations')
plt.bar(z.Borough, z['Moving Violations'],
        color=['salmon', 'firebrick', 'darksalmon', 'red', 'lightcoral'])
plt.ylabel("January 2021 - November 2021")
plt.show()

# code to plot the map with the heatmap
a = pd.read_csv('another_check.csv')
nyc_collision_factors = gpd.GeoDataFrame(
    a, geometry=gpd.points_from_xy(a.lon, a.lat))
nyc_boroughs = gpd.read_file(gplt.datasets.get_path('nyc_boroughs'))
proj = gcrs.AlbersEqualArea(central_latitude=40.7128,
                            central_longitude=-74.0059)
fig = plt.figure(figsize=(10, 5))
plt.figure(facecolor='gainsboro')
plt.axes().set_facecolor('gainsboro')
ax1 = plt.subplot(121, projection=proj)
gplt.kdeplot(
    nyc_collision_factors[
        nyc_collision_factors['CONTRIBUTING FACTOR VEHICLE 1'] != ""
    ],
    cmap='Reds',
    projection=proj,
    shade=True, shade_lowest=False,
    clip=nyc_boroughs.geometry,
    ax=ax1
)
gplt.polyplot(nyc_boroughs, zorder=1, ax=ax1)
plt.title("Collisions, 2021")
