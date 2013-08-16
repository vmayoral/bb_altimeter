bb_altimeter
============

![MPL3115A2 Altimeter](http://cache.freescale.com/files/graphic/product_freescale/P22755_MPL3115A2_PROD_.jpg)


ROS package for the **BeagleBone** that publishes the altimeter MPL3115A2 values into a topic. 

The python script checks if Linux i2c-tools have been installed and in that case it runs a loop that gathers and publishes altitute samples. The sensor can also get samples of pressure and/or temperature. Take a look at the [datasheet](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Sensors/Pressure/MPL3115A2.pdf) for more details.

There's also more information about the sensor at the [Data Manipulation and Basic Settings of the MPL3115A2 Command Line Interface Driver Code](http://cache.freescale.com/files/sensors/doc/app_note/AN4519.pdf) and [Sensor I2C Setup and FAQ](http://cache.freescale.com/files/sensors/doc/app_note/AN4481.pdf?fpsp=1&WT_TYPE=Application%20Notes&WT_VENDOR=FREESCALE&WT_FILE_FORMAT=pdf&WT_ASSET=Documentation). The equations used for the altimeter are further explained at [Pressure Altimetry using the MPL3115A2](http://cache.freescale.com/files/sensors/doc/app_note/AN4528.pdf?fpsp=1&WT_TYPE=Application%20Notes&WT_VENDOR=FREESCALE&WT_FILE_FORMAT=pdf&WT_ASSET=Documentation)

----------------

This ROS package makes use of the Linux i2c-tools so you should install them before running the package

--------------
