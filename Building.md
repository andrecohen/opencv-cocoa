Instructions on how to build OpenCV 2.0 with Cocoa/Quicktime support


## Requirements ##

  * OSX 10.5 or 10.6
  * XCode 3.x
  * CMake

## Instructions ##

Checkout the latest source code.

```
$ svn checkout http://opencv-cocoa.googlecode.com/svn/trunk/ opencv-cocoa
```

Enter the opencv-cocoa directory and start building!

```
$ cd opencv-cocoa
$ cmake -G "Unix Makefiles"
$ make
$ make install
```

## Notes ##
By default Cocoa will be used over Carbon. Currently the library is compiled with the settings that cmake has by default, this means that it most likely will build a 32bit version of OpenCV. 64bit is still difficult to use since most people have only 32bit versions of ffmpeg, python, and etc&.