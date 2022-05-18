# 課題１
import json
from collections import Counter



with open('data/sensor.json', 'r', encoding='utf-8_sig') as f:
  df = json.load(f)
  new_data = Counter()
  accel_dict = Counter()
  accel_dict["x"] = df["sensordata"]["accel"]["x"]
  accel_dict["y"] = df["sensordata"]["accel"]["y"]
  accel_dict["z"] = df["sensordata"]["accel"]["z"]
  # print(accel_dict)
  # new_data["accel"] = accel_dict

  light_data = Counter()
  light_data["light"] = df["sensordata"]["light"]["light"]
  # print(light_data)
  # new_data["light"] = light_data

  touch_data = list()
  touch_data[0][0].append(df["sensordata"]["touch"][0]["x"])
  # touch_data[0][1] = df["sensordata"]["touch"][0]["y"]
  # touch_data[0][2] = df["sensordata"]["touch"][0]["force"]
  # touch_data[1][0] = df["sensordata"]["touch"][1]["x"]
  # touch_data[1][1] = df["sensordata"]["touch"][1]["y"]
  # touch_data[1][2] = df["sensordata"]["touch"][1]["force"]
  print(touch_data)
  # new_data["touch"] = touch_data


  timestamp = Counter()
  timestamp["time"] = df["timestamp"]
  # print(timestamp)
  # new_data["timestamp"] = timestamp

