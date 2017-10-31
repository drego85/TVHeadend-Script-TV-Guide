#!/usr/bin/python3
# coding=utf-8
# This file is part of TVHeadend Script Guida TV
#
# Copyright(c) 2017 Andrea Draghetti
# https://www.andreadraghetti.it
#
# This script takes over a part of the code 
# written by Mathias F. Svendsen - okey.dk
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 3 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import io
import os
import lzma
import requests
from optparse import OptionParser

headerdesktop = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
                 "Accept-Language": "it"}
timeoutconnection = 120

parser = OptionParser(version="%prog 1.0b")
parser.add_option("-d","--description", action="store_true",dest="description",default=False, help="Prints the description of this script")
parser.add_option("-c","--capabilities", dest="capabilities", action="store_true" ,help="Not sure what this is - but saw it in tv_grab_file.", default=False)
(options, args) = parser.parse_args()

if options.description is False and options.capabilities is False:
    url = "http://www.vuplus-community.net/rytec/rytecIT_Sky.xz"
    
    # Scarico il file XZ
    page = requests.get(url, headers=headerdesktop, timeout=timeoutconnection, stream=True)
    compressedFile = io.BytesIO()
    compressedFile.write(page.content)
    compressedFile.seek(0)
    
    # Decomprimo il file XZ    
    decompressedFile = lzma.LZMAFile(compressedFile, mode='r')
    
    file_content = decompressedFile.read()

    print (file_content)
elif options.description is True:
    print ("TV Italy Sky Grab by URL")
elif options.capabilities is True:
    print ("baseline")
