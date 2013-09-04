bb_altimeter
============


ROS package for the **BeagleBone** that publishes the altimeter MPL3115A2 values into a topic. 

The python script checks if Linux i2c-tools have been installed and in that case it runs a loop that gathers and publishes altitute samples. The sensor can also get samples of pressure and/or temperature. Take a look at the [datasheet](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Sensors/Pressure/MPL3115A2.pdf) for more details.

<img src="https://raw.github.com/vmayoral/beagle-ros/master/docs/images/bb_altimeter.png" width="400px" />

There's also more information about the sensor at the [Data Manipulation and Basic Settings of the MPL3115A2 Command Line Interface Driver Code](http://cache.freescale.com/files/sensors/doc/app_note/AN4519.pdf) and [Sensor I2C Setup and FAQ](http://cache.freescale.com/files/sensors/doc/app_note/AN4481.pdf?fpsp=1&WT_TYPE=Application%20Notes&WT_VENDOR=FREESCALE&WT_FILE_FORMAT=pdf&WT_ASSET=Documentation). The equations used for the altimeter are further explained at [Pressure Altimetry using the MPL3115A2](http://cache.freescale.com/files/sensors/doc/app_note/AN4528.pdf?fpsp=1&WT_TYPE=Application%20Notes&WT_VENDOR=FREESCALE&WT_FILE_FORMAT=pdf&WT_ASSET=Documentation).

----------------

This ROS package makes use of the Linux i2c-tools so you should install them before running the package

--------------

####[mpl2115a2](https://github.com/vmayoral/bb_altimeter/blob/master/scripts/mpl2115a2.py)
ROS node that fetches altimeter data from the MPL3115A2 and publishes it to a topic through the i2c-dev interface. By default the sensor is assumed to be connected to the I2C Bus 1 (i2c-2 in the Beaglebone) at the address 0x60.

#####Published topics
*altimeter (std_msgs.msg String)*
