import json

class MotionCaptureData(object):
  def __init__(self):
    self.Reset()

  def Reset(self):
    self._motion_data = []

  def Load(self, path):
    with open(path, 'r') as f:
      self._motion_data = json.load(f)

  def NumFrames(self):
    return  len(self._motion_data['Frames'])

  def KeyFrameDuration(self):
  	return self._motion_data['Frames'][0][0]  # assuming dt stays constant

  def CycleDuration(self):
    return self.KeyFrameDuration() * (self.NumFrames()-1)  # assuming dt stays constant
