
# 检测图像中的凸点(手指)个数
def _get_contours(array):
# 利用findContours检测图像中的轮廓, 其中返回值contours包含了图像中所有轮廓的坐标点
_, contours, _ = cv2.findContours(array, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
return contours
# 根据图像中凹凸点中的 (开始点, 结束点, 远点)的坐标, 利用余弦定理计算两根手指之间的夹角, 其必为锐角, 根据锐角的个数判别手势.
def _get_defects_count(array, contour, defects, verbose = False):
ndefects = 0
for i in range(defects.shape[0]):
s,e,f,_ = defects[i,0]
beg = tuple(contour[s][0])
end = tuple(contour[e][0])
far = tuple(contour[f][0])
a = _get_eucledian_distance(beg, end)
b = _get_eucledian_distance(beg, far)
c = _get_eucledian_distance(end, far)
angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) # * 57
if angle <= math.pi/2 :#90:
ndefects = ndefects + 1
if verbose:
cv2.circle(array, far, 3, _COLOR_RED, -1)
if verbose:
cv2.line(array, beg, end, _COLOR_RED, 1)
return array, ndefects
def grdetect(array, verbose = False):
event = Event(Event.NONE)
copy = array.copy()
array = _remove_background(array) # 移除背景, add by wnavy
thresh = _divskin_detetc(array)
contours = _get_contours(thresh.copy()) # 计算图像的轮廓
largecont = max(contours, key = lambda contour: cv2.contourArea(contour))
hull = cv2.convexHull(largecont, returnPoints = False) # 计算轮廓的凸点
defects = cv2.convexityDefects(largecont, hull) # 计算轮廓的凹点
if defects is not None:
# 利用凹陷点坐标, 根据余弦定理计算图像中锐角个数
copy, ndefects = _get_defects_count(copy, largecont, defects, verbose = verbose)
# 根据锐角个数判断手势, 会有一定的误差
if ndefects == 0:
event.setType(Event.ZERO)
elif ndefects == 1:
event.setType(Event.TWO)
elif ndefects == 2:
event.setType(Event.THREE)
elif ndefects == 3:
event.setType(Event.FOUR)
elif ndefects == 4:
event.setType(Event.FIVE)
return event
