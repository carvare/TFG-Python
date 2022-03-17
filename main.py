import config
import keyboard
from frametimer import FrameTimer
from positionerfactory import PositionerFactory
from config import Config
from plotter import *

config = Config.read_config()

frame_timer = FrameTimer()

positioners = [PositionerFactory.create_predictor(config)]#, PositionerFactory.create_tracker(config)]
while True:
    pass
while not keyboard.is_pressed('q'):
    delta_time = frame_timer.mark()
    
    for positioner in positioners:
        positioner.update(delta_time)
    positioners[0].get_position()
    #print(f"Predicted position: {positioners[0].get_position()}")# Tracked position: {positioners[1].get_position()}")
    
del positioners

plotter.print_metrics()
plotter.plot()
plotter.save_to_file()