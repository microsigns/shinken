#!/usr/bin/env python2.6
#Copyright (C) 2009-2010 :
#    Gabes Jean, naparuba@gmail.com
#    Gerhard Lausser, Gerhard.Lausser@consol.de
#
#This file is part of Shinken.
#
#Shinken is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Shinken is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Shinken.  If not, see <http://www.gnu.org/licenses/>.

#
# This file is used to test reading and processing of config files
#

#It's ugly I know....
from shinken_test import *


class TestHostDepWithMultipleNames(ShinkenTest):
    #Uncomment this is you want to use a specific configuration
    #for your test
    def setUp(self):
        self.setup_with_file('etc/nagios_hostdep_with_multiple_names.cfg')

    
    #Change ME :)
    def test_DepWithMultipleNames(self):
        for n in ['svn1', 'svn2', 'svn3', 'svn4', 'nas1', 'nas2', 'nas3']:
            globals()[n] = self.sched.hosts.find_by_name(n)
            self.assert_(globals()[n] is not None)
        # We check that nas3 is a father of svn4, the simple case
        self.assert_(nas3 in [e[0] for e in svn4.act_depend_of])

        # Now the more complex one
        for son in [svn1, svn2, svn3]:
            for father in [nas1, nas2]:
                print 'Checking if', father.get_name(), 'is the father of', son.get_name()
                print son.act_depend_of
                for e in son.act_depend_of:
                    print e[0].get_name()
                self.assert_(father in [e[0] for e in son.act_depend_of])

if __name__ == '__main__':
    unittest.main()

