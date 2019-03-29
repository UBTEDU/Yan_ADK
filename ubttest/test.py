# coding: utf-8

"""
    Copyright (c) 2019 UBTECH All rights reserved.
"""
VISIONWEBSTREAM_INSTANCE = None

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        VISIONWEBSTREAM_INSTANCE = cls._instances[cls]
        return cls._instances[cls]


class VisionWebStream(object):
    __metaclass__ = Singleton

    def __init__(self, port=8000):
        self._instance_num = 0
        self._terminate_flag = False

        self._camera = None
        address = ('', port)


    def terminate(self):
        '''
        Terminate web stream by setting _terminate_flag
        :return:
        '''
        self._camera.stop_recording()
        self._httpserver.shutdown()
        self._camera = None
        self._httpserver = None
        self._instance_num -= 1

    def run(self, resolution='640x480',):
        '''
        Start web stream http server
        :param resolution: It is a string. For example 640x480
        :param port: It is a numVisionWebStreamber. For example 8000
        :return:
        '''
        self._instance_num += 1
        if (self._instance_num != 0):
            return

        with picamera.PiCamera(resolution=resolution, framerate=24) as camera:

            camera.start_recording(output, format='mjpeg')
            self._camera = camera

            self._httpserver.serve_forever()

    def is_running(self):
        '''
        Get the web stream status
        :return:
        '''
        if self._instance_num != 0:
            return True
        else:
            return False

webstream = VisionWebStream()
print (webstream.is_running())