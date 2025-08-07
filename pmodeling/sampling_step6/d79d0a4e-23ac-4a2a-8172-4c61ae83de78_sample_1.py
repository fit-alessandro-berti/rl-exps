import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

root = StrictPartialOrder(nodes=[spec_review, component_pick, frame_build, motor_mount, sensor_fit, wiring_setup, software_load, calibration_test, stress_check, firmware_flash, feedback_loop, package_prep, doc_compile, ship_arrange, remote_setup])