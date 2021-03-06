"""
A Python implementation of RocketFuel topology engine.                  
Copyright (C) 2016 Sahil Shekhawat <sahilshekhawat01@gmail.com>         
                                                                        
This program is free software: you can redistribute it and/or modify    
it under the terms of the GNU General Public License as published by    
the Free Software Foundation, either version 3 of the License, org      
(at your option) any later version.                                 
                                                                        
This program is distributed in the hope that it will be useful,         
but WITHOUT ANY WARRANTY; without even the implied warranty of          
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           
GNU General Public License for more details.                            
                                                                        
You should have received a copy of the GNU General Public licenses      
along with this program.  If not, see <http://www.gnu.org/licenses/>.   

Type ``rocketfuel license`` to see this message.
"""

from setuptools import setup

setup(
    name='rocketfuel',
    version='0.0.1',
    license='GNU GPLv3',
    author='Sahil Shekhawat',
    py_modules=['rocketfuel'],
    author_email='sahilshekhawat01@gmail.com',
    url='https://github.com/sahilshekhawat/RocketFuelPython',
    description='A Python implementation of RocketFuel topology mapping engine.',
    install_requires=[
        'bs4',
        'click',
        'paramiko',
        'requests',
        'ipaddress',
        'python-daemon'
    ],
    entry_points='''
        [console_scripts]
        rocketfuel=rocketfuel:cli
    ''',
)