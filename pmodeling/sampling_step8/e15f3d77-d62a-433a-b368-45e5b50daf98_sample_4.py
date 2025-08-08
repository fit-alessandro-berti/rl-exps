import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Gather_Specs = Transition(label='Gather Specs')
Adapt_Design = Transition(label='Adapt Design')
Source_Parts = Transition(label='Source Parts')
Component_Test = Transition(label='Component Test')
Assemble_Frame = Transition(label='Assemble Frame')
Install_Firmware = Transition(label='Install Firmware')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Stress_Test = Transition(label='Stress Test')
Flight_Simulate = Transition(label='Flight Simulate')
Validate_Battery = Transition(label='Validate Battery')
Check_Accuracy = Transition(label='Check Accuracy')
Package_Units = Transition(label='Package Units')
Create_Manuals = Transition(label='Create Manuals')
Ship_Drones = Transition(label='Ship Drones')
Collect_Feedback = Transition(label='Collect Feedback')

skip = SilentTransition()

# Define the process flow
Gather_Specs --> Adapt_Design
Adapt_Design --> Source_Parts
Source_Parts --> Component_Test
Component_Test --> Assemble_Frame
Assemble_Frame --> Install_Firmware
Install_Firmware --> Calibrate_Sensors
Calibrate_Sensors --> Stress_Test
Stress_Test --> Flight_Simulate
Flight_Simulate --> Validate_Battery
Validate_Battery --> Check_Accuracy
Check_Accuracy --> Package_Units
Package_Units --> Create_Manuals
Create_Manuals --> Ship_Drones
Ship_Drones --> Collect_Feedback

root = StrictPartialOrder(nodes=[Gather_Specs, Adapt_Design, Source_Parts, Component_Test, Assemble_Frame, Install_Firmware, Calibrate_Sensors, Stress_Test, Flight_Simulate, Validate_Battery, Check_Accuracy, Package_Units, Create_Manuals, Ship_Drones, Collect_Feedback])