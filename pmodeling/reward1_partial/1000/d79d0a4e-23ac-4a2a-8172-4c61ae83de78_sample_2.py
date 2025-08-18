import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
spec_review = Transition(label='Spec Review')
component_pick = Transition(label='Component Pick')
frame_build = Transition(label='Frame Build')
motor_mount = Transition(label='Motor Mount')
sensor_fit = Transition(label='Sensor Fit')
wiring_setup = Transition(label='Wiring Setup')
software_load = Transition(label='Software Load')
calibration_test = Transition(label='Calibration Test')
stress_check = Transition(label='Stress Check')
firmware_flash = Transition(label='Firmware Flash')
feedback_loop = Transition(label='Feedback Loop')
package_prep = Transition(label='Package Prep')
doc_compile = Transition(label='Doc Compile')
ship_arrange = Transition(label='Ship Arrange')
remote_setup = Transition(label='Remote Setup')

# Define partial orders
# Spec Review -> Component Pick
root = StrictPartialOrder(nodes=[spec_review, component_pick])
root.order.add_edge(spec_review, component_pick)

# Component Pick -> Frame Build
root.order.add_edge(component_pick, frame_build)

# Frame Build -> Motor Mount
root.order.add_edge(frame_build, motor_mount)

# Motor Mount -> Sensor Fit
root.order.add_edge(motor_mount, sensor_fit)

# Sensor Fit -> Wiring Setup
root.order.add_edge(sensor_fit, wiring_setup)

# Wiring Setup -> Software Load
root.order.add_edge(wiring_setup, software_load)

# Software Load -> Calibration Test
root.order.add_edge(software_load, calibration_test)

# Calibration Test -> Stress Check
root.order.add_edge(calibration_test, stress_check)

# Stress Check -> Firmware Flash
root.order.add_edge(stress_check, firmware_flash)

# Firmware Flash -> Feedback Loop
root.order.add_edge(firmware_flash, feedback_loop)

# Feedback Loop -> Package Prep
root.order.add_edge(feedback_loop, package_prep)

# Package Prep -> Doc Compile
root.order.add_edge(package_prep, doc_compile)

# Doc Compile -> Ship Arrange
root.order.add_edge(doc_compile, ship_arrange)

# Ship Arrange -> Remote Setup
root.order.add_edge(ship_arrange, remote_setup)