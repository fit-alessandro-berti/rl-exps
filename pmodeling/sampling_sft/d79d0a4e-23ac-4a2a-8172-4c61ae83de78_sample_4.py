import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Build the calibration loop: Calibration Test -> Stress Check -> Firmware Flash -> Feedback Loop -> Stress Check
calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[calibration_test, stress_check])
firmware_loop = OperatorPOWL(operator=Operator.LOOP, children=[firmware_flash, feedback_loop])

# Build the final assembly partial order
final_assembly = StrictPartialOrder(nodes=[
    spec_review,
    component_pick,
    frame_build,
    motor_mount,
    sensor_fit,
    wiring_setup,
    software_load,
    calibration_loop,
    firmware_loop,
    package_prep,
    doc_compile,
    ship_arrange,
    remote_setup
])
final_assembly.order.add_edge(spec_review, component_pick)
final_assembly.order.add_edge(component_pick, frame_build)
final_assembly.order.add_edge(frame_build, motor_mount)
final_assembly.order.add_edge(frame_build, sensor_fit)
final_assembly.order.add_edge(motor_mount, wiring_setup)
final_assembly.order.add_edge(sensor_fit, wiring_setup)
final_assembly.order.add_edge(wiring_setup, software_load)
final_assembly.order.add_edge(software_load, calibration_loop)
final_assembly.order.add_edge(calibration_loop, firmware_loop)
final_assembly.order.add_edge(firmware_loop, package_prep)
final_assembly.order.add_edge(package_prep, doc_compile)
final_assembly.order.add_edge(doc_compile, ship_arrange)
final_assembly.order.add_edge(ship_arrange, remote_setup)

# Set the root of the process
root = final_assembly