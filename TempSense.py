#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        TempSense.py
#
#  Project :     
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      null$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["TempSense", "TempSenseClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(TempSense.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	TempSense.additionnal_import

# Device States Description
# No states for this device


class TempSense (PyTango.Device_4Impl):
    """"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(TempSense.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	TempSense.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        TempSense.init_device(self)
        #----- PROTECTED REGION ID(TempSense.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TempSense.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(TempSense.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TempSense.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_Temperature_read = 0.0
	self.attr_Hum_read = 0.0

        #----- PROTECTED REGION ID(TempSense.init_device) ENABLED START -----#
        
        self.set_state(PyTango.DevState.ON)
        self.serial_proxy=PyTango.DeviceProxy(self.SerialLine)

        #----- PROTECTED REGION END -----#	//	TempSense.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(TempSense.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TempSense.always_executed_hook

    # -------------------------------------------------------------------------
    #    TempSense read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_Temperature(self, attr):
        self.debug_stream("In read_Temperature()")
        #----- PROTECTED REGION ID(TempSense.Temperature_read) ENABLED START -----#
        #self.serial_proxy.DevSerFlush(1)        
        #self.serial_proxy.DevSerWriteString("t")
	#tamano = self.serial_proxy.DevSerGetNChar()
        #temp = self.serial_proxy.DevSerReadNChar(tamano)
	#self.attr_Temperature_read = float(temp)
        attr.set_value(self.attr_Temperature_read)
	#attr.set_value(float(temp))
	#self.Temperature.set_value(float(temp))
	        

        #----- PROTECTED REGION END -----#	//	TempSense.Temperature_read
      
  
    def read_Hum(self, attr):
        self.debug_stream("In read_Temperature()")
        #----- PROTECTED REGION ID(TempSense.Temperature_read) ENABLED START -----#
        #self.serial_proxy.DevSerFlush(1)        
        #self.serial_proxy.DevSerWriteString("h")
	#tamano = self.serial_proxy.DevSerGetNChar()
        #h = self.serial_proxy.DevSerReadNChar(tamano)
	#self.attr_Hum_read = float(h)
 
        attr.set_value(self.attr_Hum_read)

        
        #----- PROTECTED REGION END -----#	//	TempSense.Hum_read


            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(TempSense.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TempSense.read_attr_hardware


    # -------------------------------------------------------------------------
    #    TempSense command methods
    # -------------------------------------------------------------------------
    
    def Read(self):
        """ 
        """
        self.debug_stream("In GoHome()")
        #----- PROTECTED REGION ID(MotorCN.GoHome) ENABLED START -----#
        self.serial_proxy.DevSerFlush(1)        
        self.serial_proxy.DevSerWriteString("u")
	tamano = self.serial_proxy.DevSerGetNChar()
        u = self.serial_proxy.DevSerReadNChar(tamano)
	temp, hum = u.split('||')
	self.attr_Temperature_read = float(temp)
	self.attr_Hum_read = float(hum)

        #----- PROTECTED REGION END -----#	//	MotorCN.GoHome

    #----- PROTECTED REGION ID(TempSense.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	TempSense.programmer_methods

class TempSenseClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(TempSense.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	TempSense.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        'SerialLine':
            [PyTango.DevString, 
            "Serial port",
            ["test/arduino/1"] ],
        }


    #    Command definitions
    cmd_list = {
        'Read':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
                'Temperature':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ]],
		'Hum':
	    [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ]]
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(TempSenseClass, TempSense, 'TempSense')
        #----- PROTECTED REGION ID(TempSense.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TempSense.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
