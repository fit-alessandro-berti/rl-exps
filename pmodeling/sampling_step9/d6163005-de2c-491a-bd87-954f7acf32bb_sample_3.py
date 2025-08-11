import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
requirement_analysis = Transition(label='Requirement Analysis')
component_sourcing = Transition(label='Component Sourcing')
quality_check = Transition(label='Quality Check')
frame_assembly = Transition(label='Frame Assembly')
motor_installation = Transition(label='Motor Installation')
sensor_setup = Transition(label='Sensor Setup')
control_unit = Transition(label='Control Unit')
firmware_upload = Transition(label='Firmware Upload')
system_calibration = Transition(label='System Calibration')
flight_testing = Transition(label='Flight Testing')
error_correction = Transition(label='Error Correction')
cosmetic_finish = Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual = Transition(label='User Manual')
client_training = Transition(label='Client Training')
support_scheduling = Transition(label='Support Scheduling')

# Define silent transitions
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, error_correction])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[user_manual, client_training])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[support_scheduling])

# Define XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])

# Define POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)

# Print the final POWL model
print(root)