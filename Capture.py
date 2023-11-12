
class Capture(object):
'''
Capture object
:param deviceID: device ID of your capture device, defaults to 0
:type deviceID: :obj:`int`
Example
>>> import pygr
>>> cap = pygr.Capture()
'''
def __init__(self, deviceID=0): # ID为0, 表示从默认的摄像头读取视频数据
self.deviceID = deviceID
self.capture = cv2.VideoCapture(self.deviceID) #
def read(self):
_, frame = self.capture.read() # 调用默认摄像头捕获一帧图像
frame = cv2.bilateralFilter(frame, 5, 50, 100) # 对捕获到的图像进行双边滤波
image = Image.fromarray(frame) # 转换图像数据格式
return image
