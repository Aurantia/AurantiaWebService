#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def check_arduino_data_integrity(dict_data):
    full_dict = (dict_data.has_key('ip_address') 
                    and dict_data.has_key('bustling')
                        and dict_data.has_key('luminosity')
                            and dict_data.has_key('temperature'))

    return full_dict
