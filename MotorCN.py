#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        MotorCN.py
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
#  $Author :      gndspkg$
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

__all__ = ["MotorCN", "MotorCNClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(MotorCN.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	MotorCN.additionnal_import

# Device States Description
# No states for this device


class MotorCN (PyTango.Device_4Impl):
    """"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(MotorCN.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	MotorCN.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        MotorCN.init_device(self)
        #----- PROTECTED REGION ID(MotorCN.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MotorCN.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(MotorCN.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MotorCN.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_posicion_read = 0
        #----- PROTECTED REGION ID(MotorCN.init_device) ENABLED START -----#
        self.set_state(PyTango.DevState.ON)
        self.serial_proxy=PyTango.DeviceProxy(self.SerialLine)

        #----- PROTECTED REGION END -----#	//	MotorCN.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(MotorCN.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MotorCN.always_executed_hook

    # -------------------------------------------------------------------------
    #    MotorCN read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_posicion(self, attr):
        self.debug_stream("In read_posicion()")
        #----- PROTECTED REGION ID(MotorCN.posicion_read) ENABLED START -----#
        attr.set_value(self.attr_posicion_read)
        #----- PROTECTED REGION END -----#	//	MotorCN.posicion_read
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(MotorCN.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MotorCN.read_attr_hardware


    # -------------------------------------------------------------------------
    #    MotorCN command methods
    # -------------------------------------------------------------------------
    
    def Move(self):
        """ Input:cantidad de pasos
        :param argin: 
        :type argin: PyTango.DevShort
        """
        self.debug_stream("In Move()")
        #----- PROTECTED REGION ID(MotorCN.Move) ENABLED START -----#
        self.serial_proxy.DevSerWriteString("m")
        #----- PROTECTED REGION END -----#	//	MotorCN.Move
        
    def GoHome(self):
        """ 
        """
        self.debug_stream("In GoHome()")
        #----- PROTECTED REGION ID(MotorCN.GoHome) ENABLED START -----#
        self.serial_proxy.DevSerWriteString("r")
        #----- PROTECTED REGION END -----#	//	MotorCN.GoHome
    
    def Leer_posicion(self):
        """ 
        """
        self.debug_stream("In Leerposicion()")
        #----- PROTECTED REGION ID(MotorCN.GoHome) ENABLED START -----#
	self.serial_proxy.DevSerFlush(1)
        self.serial_proxy.DevSerWriteString("p")
	tamano = self.serial_proxy.DevSerGetNChar()
        posicion = self.serial_proxy.DevSerReadNChar(tamano)
        self.attr_posicion_read = int(posicion)
        #----- PROTECTED REGION END -----#	//	MotorCN.GoHome    

    #----- PROTECTED REGION ID(MotorCN.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	MotorCN.programmer_methods

class MotorCNClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(MotorCN.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	MotorCN.global_class_variables


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
        'Move':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'GoHome':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'Leer_posicion':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'posicion':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "step",
                'max value': "2038",
                'min value': "-2038",
                'max alarm': "2038",
                'min alarm': "-2038",
                'max warning': "1900",
                'min warning': "-1900",
            } ],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(MotorCNClass, MotorCN, 'MotorCN')
        #----- PROTECTED REGION ID(MotorCN.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MotorCN.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
