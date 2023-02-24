# The pydat Library



The main objective of this online package is to drive SDF curves from the USGS gage data. However, it has the capability to create the SDF curves for any data. It also has functions to get the USGS staion list, daily streamflow time-series, and analog streamflows. 

## Example

In this example the main functions of this package will be shown. 

### Step. 1.

Import the packages.


```python
from pydat import pydat
import matplotlib.pyplot as plt
```

### Step. 2. 

#### valid_station(status='good', state='', basin='', start_date="1800-01-01", end_date=today))

valid_station function gets all of the station information for the stations which are suitable for SDF curve calculation or all of the stations available in a given state or basin and time period.  


```python
station_names =  pydat.valid_station(state='OH')

station_names.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>agency_cd</th>
      <th>site_no</th>
      <th>station_nm</th>
      <th>site_tp_cd</th>
      <th>dec_lat_va</th>
      <th>dec_long_va</th>
      <th>coord_acy_cd</th>
      <th>dec_coord_datum_cd</th>
      <th>alt_va</th>
      <th>alt_acy_va</th>
      <th>...</th>
      <th>stat_cd</th>
      <th>ts_id</th>
      <th>loc_web_ds</th>
      <th>medium_grp_cd</th>
      <th>parm_grp_cd</th>
      <th>srs_id</th>
      <th>access_cd</th>
      <th>begin_date</th>
      <th>end_date</th>
      <th>count_nu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USGS</td>
      <td>03086500</td>
      <td>Mahoning River at Alliance OH</td>
      <td>ST</td>
      <td>40.932836</td>
      <td>-81.094541</td>
      <td>S</td>
      <td>NAD83</td>
      <td>1034.79</td>
      <td>0.10</td>
      <td>...</td>
      <td>3</td>
      <td>108591</td>
      <td>NaN</td>
      <td>wat</td>
      <td>NaN</td>
      <td>1645423</td>
      <td>0</td>
      <td>1941-09-01</td>
      <td>1993-09-29</td>
      <td>19022</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USGS</td>
      <td>03089500</td>
      <td>Mill Creek near Berlin Center OH</td>
      <td>ST</td>
      <td>41.000336</td>
      <td>-80.968424</td>
      <td>S</td>
      <td>NAD83</td>
      <td>1032.90</td>
      <td>0.01</td>
      <td>...</td>
      <td>3</td>
      <td>108600</td>
      <td>NaN</td>
      <td>wat</td>
      <td>NaN</td>
      <td>1645423</td>
      <td>0</td>
      <td>1941-10-01</td>
      <td>1971-10-04</td>
      <td>10961</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USGS</td>
      <td>03091500</td>
      <td>Mahoning River at Pricetown OH</td>
      <td>ST</td>
      <td>41.131446</td>
      <td>-80.971202</td>
      <td>S</td>
      <td>NAD83</td>
      <td>904.77</td>
      <td>0.10</td>
      <td>...</td>
      <td>3</td>
      <td>108605</td>
      <td>NaN</td>
      <td>wat</td>
      <td>NaN</td>
      <td>1645423</td>
      <td>0</td>
      <td>1929-08-01</td>
      <td>2023-02-23</td>
      <td>34175</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USGS</td>
      <td>03092000</td>
      <td>Kale Creek near Pricetown OH</td>
      <td>ST</td>
      <td>41.139779</td>
      <td>-80.995092</td>
      <td>S</td>
      <td>NAD83</td>
      <td>914.70</td>
      <td>0.01</td>
      <td>...</td>
      <td>3</td>
      <td>108609</td>
      <td>NaN</td>
      <td>wat</td>
      <td>NaN</td>
      <td>1645423</td>
      <td>0</td>
      <td>1941-05-01</td>
      <td>1993-09-29</td>
      <td>19145</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USGS</td>
      <td>03092500</td>
      <td>West Branch Mahoning River near Newton Falls OH</td>
      <td>ST</td>
      <td>41.171723</td>
      <td>-81.020927</td>
      <td>S</td>
      <td>NAD83</td>
      <td>912.20</td>
      <td>0.01</td>
      <td>...</td>
      <td>3</td>
      <td>108618</td>
      <td>NaN</td>
      <td>wat</td>
      <td>NaN</td>
      <td>1645423</td>
      <td>0</td>
      <td>1926-10-01</td>
      <td>1981-10-02</td>
      <td>20091</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>



### Step. 3. 

#### daily_data(site='', start_date="1800-01-01", end_date=today)

daily_data function provides the daily mean streamflow data from the USGS website for a given date or from 1800 until the current day.   
 
- The site parameter asks for site number.
- The start_date parameter asks for the start of the time-series.
- The end_date parameter asks for the end of the time-series.


```python
daily_stream = pydat.daily_data(site="03098600")

daily_stream.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Datetime</th>
      <th>USGS_flow</th>
      <th>variable</th>
      <th>USGS_ID</th>
      <th>measurement_unit</th>
      <th>qualifiers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1987-10-01 00:00:00+00:00</td>
      <td>738.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1987-10-02 00:00:00+00:00</td>
      <td>619.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1987-10-03 00:00:00+00:00</td>
      <td>570.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1987-10-04 00:00:00+00:00</td>
      <td>521.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1987-10-05 00:00:00+00:00</td>
      <td>490.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
</div>



### Step. 4. 

#### sdf_creator(site='03098600', duration='all', figure=True, length='optimal')

sdf_creator function does the calculation for the SDF curves and then plot it based on the user's preferance. 
- The duration parameter asks whether it should calculate the SDF curves for the all (2 to 10) duration or any other length.
- The figure parameter asks whether it should plot the SDF curve or not.
- The length parameter asks whether it should do the calculation based on the best data period.

It has three outputs:
- SDF curve results.
- Streamflow for the station.
- Plot file.

Here it will give the SDF curves for all station '03098600', all the durations, and the optimal length. Also, it will show the figure. 


```python
all_sdf, all_streamflow, all_fig = pydat.sdf_creator(site='03098600', duration='all', figure=True, length='optimal')
```


    
![png](output_12_0.png)
    



```python
# The SDF curve results.
all_sdf.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="5" halign="left">Duration = 2</th>
      <th colspan="5" halign="left">Duration = 3</th>
      <th>...</th>
      <th colspan="5" halign="left">Duration = 9</th>
      <th colspan="5" halign="left">Duration = 10</th>
    </tr>
    <tr>
      <th></th>
      <th>Date</th>
      <th>Flow_(cfs)</th>
      <th>Mean_Flow_(cfs)</th>
      <th>Severity_(cfs)</th>
      <th>Probability</th>
      <th>Date</th>
      <th>Flow_(cfs)</th>
      <th>Mean_Flow_(cfs)</th>
      <th>Severity_(cfs)</th>
      <th>Probability</th>
      <th>...</th>
      <th>Date</th>
      <th>Flow_(cfs)</th>
      <th>Mean_Flow_(cfs)</th>
      <th>Severity_(cfs)</th>
      <th>Probability</th>
      <th>Date</th>
      <th>Flow_(cfs)</th>
      <th>Mean_Flow_(cfs)</th>
      <th>Severity_(cfs)</th>
      <th>Probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1996.0</td>
      <td>1348.666667</td>
      <td>1014.619635</td>
      <td>-17.109113</td>
      <td>64.285714</td>
      <td>1997.0</td>
      <td>1445.079452</td>
      <td>1158.106240</td>
      <td>-5.386757</td>
      <td>33.333333</td>
      <td>...</td>
      <td>2003.0</td>
      <td>1468.561644</td>
      <td>1008.528305</td>
      <td>-17.606753</td>
      <td>100.000000</td>
      <td>2004.0</td>
      <td>1902.647541</td>
      <td>1097.940228</td>
      <td>-10.302111</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1998.0</td>
      <td>978.805479</td>
      <td>1211.942466</td>
      <td>-0.988525</td>
      <td>7.142857</td>
      <td>1999.0</td>
      <td>825.016438</td>
      <td>1082.967123</td>
      <td>-11.525361</td>
      <td>66.666667</td>
      <td>...</td>
      <td>2004.0</td>
      <td>1902.647541</td>
      <td>1144.314409</td>
      <td>-6.513502</td>
      <td>71.428571</td>
      <td>2005.0</td>
      <td>1633.901370</td>
      <td>1193.273105</td>
      <td>-2.513747</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1999.0</td>
      <td>825.016438</td>
      <td>901.910959</td>
      <td>-26.317019</td>
      <td>78.571429</td>
      <td>2000.0</td>
      <td>832.852459</td>
      <td>878.891459</td>
      <td>-28.197632</td>
      <td>83.333333</td>
      <td>...</td>
      <td>2005.0</td>
      <td>1633.901370</td>
      <td>1176.007154</td>
      <td>-3.924315</td>
      <td>57.142857</td>
      <td>2006.0</td>
      <td>1114.065753</td>
      <td>1169.813014</td>
      <td>-4.430355</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000.0</td>
      <td>832.852459</td>
      <td>828.934449</td>
      <td>-32.278945</td>
      <td>85.714286</td>
      <td>2001.0</td>
      <td>662.104110</td>
      <td>773.324336</td>
      <td>-36.822097</td>
      <td>100.000000</td>
      <td>...</td>
      <td>2006.0</td>
      <td>1114.065753</td>
      <td>1139.227854</td>
      <td>-6.929056</td>
      <td>85.714286</td>
      <td>2007.0</td>
      <td>1531.624658</td>
      <td>1178.467534</td>
      <td>-3.723310</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2001.0</td>
      <td>662.104110</td>
      <td>747.478284</td>
      <td>-38.933630</td>
      <td>100.000000</td>
      <td>2002.0</td>
      <td>835.095890</td>
      <td>776.684153</td>
      <td>-36.547612</td>
      <td>91.666667</td>
      <td>...</td>
      <td>2007.0</td>
      <td>1531.624658</td>
      <td>1200.652207</td>
      <td>-1.910900</td>
      <td>28.571429</td>
      <td>2018.0</td>
      <td>1345.435616</td>
      <td>1205.848763</td>
      <td>-1.486359</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 45 columns</p>
</div>




```python
# The streamflow resutls.
all_streamflow.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Datetime</th>
      <th>USGS_flow</th>
      <th>variable</th>
      <th>USGS_ID</th>
      <th>measurement_unit</th>
      <th>qualifiers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2557</th>
      <td>1994-10-01 00:00:00+00:00</td>
      <td>554.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2558</th>
      <td>1994-10-02 00:00:00+00:00</td>
      <td>578.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2559</th>
      <td>1994-10-03 00:00:00+00:00</td>
      <td>435.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2560</th>
      <td>1994-10-04 00:00:00+00:00</td>
      <td>355.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2561</th>
      <td>1994-10-05 00:00:00+00:00</td>
      <td>324.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
</div>



Here it will give the SDF curves for all station '03098600', 2 and 3 year durations, and the data length. Also, it will show the figure. 


```python
part_sdf_1, part_streamflow_1, part_fig_1 = pydat.sdf_creator(site='03098600', duration='2,3', figure=True)
```


    
![png](output_16_0.png)
    


Here it will give the SDF curves for all station '03098600', 5, 6, and 7 year durations, and the data length. Also, it will NOT show the figure. 


```python
part_sdf_2, part_streamflow_2, part_fig_2 = pydat.sdf_creator(site='03098600', duration='5,6,7', figure=False)
```


```python
# The SDF curve results.
part_sdf_2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="5" halign="left">Duration = 5</th>
      <th colspan="5" halign="left">Duration = 6</th>
      <th colspan="5" halign="left">Duration = 7</th>
    </tr>
    <tr>
      <th></th>
      <th>Date</th>
      <th>Flow_(cfs)</th>
      <th>Mean_Flow_(cfs)</th>
      <th>Severity_(cfs)</th>
      <th>Probability</th>
      <th>Date</th>
      <th>Flow_(cfs)</th>
      <th>Mean_Flow_(cfs)</th>
      <th>Severity_(cfs)</th>
      <th>Probability</th>
      <th>Date</th>
      <th>Flow_(cfs)</th>
      <th>Mean_Flow_(cfs)</th>
      <th>Severity_(cfs)</th>
      <th>Probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1999.0</td>
      <td>825.016438</td>
      <td>1055.628128</td>
      <td>-13.758862</td>
      <td>70.0</td>
      <td>2000.0</td>
      <td>832.852459</td>
      <td>1018.498850</td>
      <td>-16.792194</td>
      <td>66.666667</td>
      <td>2001.0</td>
      <td>662.104110</td>
      <td>967.585315</td>
      <td>-20.951653</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000.0</td>
      <td>832.852459</td>
      <td>1086.084099</td>
      <td>-11.270715</td>
      <td>60.0</td>
      <td>2001.0</td>
      <td>662.104110</td>
      <td>1015.420768</td>
      <td>-17.043663</td>
      <td>77.777778</td>
      <td>2002.0</td>
      <td>835.095890</td>
      <td>989.660071</td>
      <td>-19.148222</td>
      <td>88.888889</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2001.0</td>
      <td>662.104110</td>
      <td>948.771588</td>
      <td>-22.488669</td>
      <td>80.0</td>
      <td>2002.0</td>
      <td>835.095890</td>
      <td>929.825638</td>
      <td>-24.036487</td>
      <td>100.000000</td>
      <td>2003.0</td>
      <td>1468.561644</td>
      <td>1006.787925</td>
      <td>-17.748936</td>
      <td>77.777778</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2002.0</td>
      <td>835.095890</td>
      <td>826.774875</td>
      <td>-32.455375</td>
      <td>100.0</td>
      <td>2003.0</td>
      <td>1468.561644</td>
      <td>933.739337</td>
      <td>-23.716751</td>
      <td>88.888889</td>
      <td>2004.0</td>
      <td>1902.647541</td>
      <td>1072.154795</td>
      <td>-12.408691</td>
      <td>66.666667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2003.0</td>
      <td>1468.561644</td>
      <td>924.726108</td>
      <td>-24.453100</td>
      <td>90.0</td>
      <td>2004.0</td>
      <td>1902.647541</td>
      <td>1087.713014</td>
      <td>-11.137638</td>
      <td>55.555556</td>
      <td>2005.0</td>
      <td>1633.901370</td>
      <td>1165.739922</td>
      <td>-4.763112</td>
      <td>55.555556</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The streamflow resutls.
part_streamflow_2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Datetime</th>
      <th>USGS_flow</th>
      <th>variable</th>
      <th>USGS_ID</th>
      <th>measurement_unit</th>
      <th>qualifiers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2557</th>
      <td>1994-10-01 00:00:00+00:00</td>
      <td>554.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2558</th>
      <td>1994-10-02 00:00:00+00:00</td>
      <td>578.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2559</th>
      <td>1994-10-03 00:00:00+00:00</td>
      <td>435.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2560</th>
      <td>1994-10-04 00:00:00+00:00</td>
      <td>355.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2561</th>
      <td>1994-10-05 00:00:00+00:00</td>
      <td>324.0</td>
      <td>streamflow</td>
      <td>="03098600"</td>
      <td>ft³/s</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
</div>



### Step. 5. 

#### streamflow_generator(site='', duration='', figure=False)

sdf_creator function does the calculation for the SDF curves and then plot it based on the user's preferance. 
- The site parameter asks for the site number.
- The duration parameter asks the duration length which can only be one number.
- The figure parameter asks whether the plot for the SDF curve is needed or not.

It has three outputs:
- The years that have analog streamflows.
- The severity and frequency of the points with streamflow analogs.
- The streamflow analog time-series.


```python
analog_years ,info, streamflow_analog = pydat.streamflow_generator(site='03098600', duration='3', figure=False)
```


```python
# Analog years info. 
analog_years
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index year</th>
      <th>similar year</th>
      <th>similar year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1997.0</td>
      <td>2016.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1999.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001.0</td>
      <td>2002.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2014.0</td>
      <td>2018.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2015.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016.0</td>
      <td>2017.0</td>
      <td>2022.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2017.0</td>
      <td>2022.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2018.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2022.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Analog points information. 
info
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>year</th>
      <th>severity</th>
      <th>frequency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1997</th>
      <th>index_year</th>
      <td>1997.0</td>
      <td>-5.4</td>
      <td>33.333333</td>
    </tr>
    <tr>
      <th>similar_year_1</th>
      <td>2016.0</td>
      <td>-5.8</td>
      <td>41.666667</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2001</th>
      <th>index_year</th>
      <td>2001.0</td>
      <td>-36.8</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>similar_year_1</th>
      <td>2002.0</td>
      <td>-36.5</td>
      <td>91.666667</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2014</th>
      <th>index_year</th>
      <td>2014.0</td>
      <td>-4.1</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>similar_year_1</th>
      <td>2018.0</td>
      <td>-4.0</td>
      <td>16.666667</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2016</th>
      <th>index_year</th>
      <td>2016.0</td>
      <td>-5.8</td>
      <td>41.666667</td>
    </tr>
    <tr>
      <th>similar_year_1</th>
      <td>2017.0</td>
      <td>-6.1</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>similar_year_2</th>
      <td>2022.0</td>
      <td>-6.1</td>
      <td>58.333333</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2017</th>
      <th>index_year</th>
      <td>2017.0</td>
      <td>-6.1</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>similar_year_1</th>
      <td>2022.0</td>
      <td>-6.1</td>
      <td>58.333333</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The analoge streamflow time-seies. 
streamflow_analog['1997'].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date_index</th>
      <th>Flow_cfs_index</th>
      <th>Date_similar_1</th>
      <th>Flow_cfs_similar_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1994-10-01 00:00:00+00:00</td>
      <td>554.0</td>
      <td>2013-10-01 00:00:00+00:00</td>
      <td>424.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1994-10-02 00:00:00+00:00</td>
      <td>578.0</td>
      <td>2013-10-02 00:00:00+00:00</td>
      <td>403.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1994-10-03 00:00:00+00:00</td>
      <td>435.0</td>
      <td>2013-10-03 00:00:00+00:00</td>
      <td>411.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994-10-04 00:00:00+00:00</td>
      <td>355.0</td>
      <td>2013-10-04 00:00:00+00:00</td>
      <td>460.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1994-10-05 00:00:00+00:00</td>
      <td>324.0</td>
      <td>2013-10-05 00:00:00+00:00</td>
      <td>505.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The analoge streamflow time-seies. 
streamflow_analog['2016'].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date_index</th>
      <th>Flow_cfs_index</th>
      <th>Date_similar_1</th>
      <th>Flow_cfs_similar_1</th>
      <th>Date_similar_2</th>
      <th>Flow_cfs_similar_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013-10-01 00:00:00+00:00</td>
      <td>424.0</td>
      <td>2014-10-01 00:00:00+00:00</td>
      <td>495.0</td>
      <td>2019-10-01 00:00:00+00:00</td>
      <td>650.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013-10-02 00:00:00+00:00</td>
      <td>403.0</td>
      <td>2014-10-02 00:00:00+00:00</td>
      <td>491.0</td>
      <td>2019-10-02 00:00:00+00:00</td>
      <td>596.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013-10-03 00:00:00+00:00</td>
      <td>411.0</td>
      <td>2014-10-03 00:00:00+00:00</td>
      <td>477.0</td>
      <td>2019-10-03 00:00:00+00:00</td>
      <td>538.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013-10-04 00:00:00+00:00</td>
      <td>460.0</td>
      <td>2014-10-04 00:00:00+00:00</td>
      <td>587.0</td>
      <td>2019-10-04 00:00:00+00:00</td>
      <td>470.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2013-10-05 00:00:00+00:00</td>
      <td>505.0</td>
      <td>2014-10-05 00:00:00+00:00</td>
      <td>529.0</td>
      <td>2019-10-05 00:00:00+00:00</td>
      <td>367.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
