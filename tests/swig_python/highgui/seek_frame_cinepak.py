#! /usr/bin/env python

"""
This script checks HighGUI's frame seeking functionality
on a CinePak-compressed .avi file.
"""

# name if this test and it's requirements
TESTNAME = "seek_frame_cinepak"
REQUIRED = []
ERRORS=[0.086,0.082,0.087,0.085,0.086,0.085,0.086,0.086,0.086,0.086,0.089,0.087,0.090,0.088,0.088,0.088,0.089,0.088,0.089,0.088,0.091,0.089,0.092,0.091,0.091,0.090,0.091,0.090,0.091]

# needed for sys.exit(int), .works file handling and check routine
import sys
import works
import seek_test

# check requirements and delete old flag file, if it exists
if not works.check_files(REQUIRED,TESTNAME):
	sys.exit(77)

# name of file we check here
FILENAME='cinepak.avi'

# run check routine
result=seek_test.seek_frame_ok(FILENAME,ERRORS)

# create flag file for following tests
works.set_file(TESTNAME)

 # return result of test routine
sys.exit(result)
