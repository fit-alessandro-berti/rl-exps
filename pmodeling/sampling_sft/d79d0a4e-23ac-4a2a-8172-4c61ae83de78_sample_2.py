import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
spec_review    = Transition(label='Spec Review')
component_pick = Transition(label='Component Pick')
frame_build    = Transition(label='Frame Build')
motor_mount    = Transition(label='Motor Mount')
sensor_fit     = Transition(label='Sensor Fit')
wiring_setup   = Transition(label='Wiring Setup')
software_load  = Transition(label='Software Load')
calibration    = Transition(label='Calibration Test')
stress_check   = Transition(label='Stress Check')
firmware_flash = Transition(label='Firmware Flash')
feedback_loop  = Transition(label='Feedback Loop')
package_prep   = Transition(label='Package Prep')
doc_compile    = Transition(label='Doc Compile')
ship_arrange   = Transition(label='Ship Arrange')
remote_setup   = Transition(label='Remote Setup')

# Loop for iterative firmware updating
loop_firmware = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, firmware_flash])

# Build the partial order
root = StrictPartialOrder(nodes=[
    spec_review, component_pick,
    frame_build, motor_mount, sensor_fit, wiring_setup,
    software_load,
    calibration, stress_check, loop_firmware,
    package_prep, doc_compile, ship_arrange, remote_setup
])

# Define the control-flow dependencies
root.order.add_edge(spec_review, component_pick)
root.order.add_edge(component_pick, frame_build)
root.order.add_edge(frame_build, motor_mount)
root.order.add_edge(frame_build, sensor_fit)
root.order.add_edge(frame_build, wiring_setup)
root.order.add_edge(motor_mount, software_load)
root.order.add_edge(sensor_fit, software_load)
root.order.add_edge(wiring_setup, software_load)
root.order.add_edge(software_load, calibration)
root.order.add_edge(software_load, stress_check)
root.order.add_edge(calibration, loop_firmware)
root.order.add_edge(stress_check, loop_firmware)
root.order.add_edge(loop_firmware, package_prep)
root.order.add_edge(package_prep, doc_compile)
root.order.add_edge(doc_compile, ship_arrange)
root.order.add_edge(ship_arrange, remote_setup)

# Final concurrent maintenance setup
root.order.add_edge(remote_setup, remote_setup)

print(root)