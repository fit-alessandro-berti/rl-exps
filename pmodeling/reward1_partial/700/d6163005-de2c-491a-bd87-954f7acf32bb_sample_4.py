import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
req_anal = Transition(label='Requirement Analysis')
comp_src = Transition(label='Component Sourcing')
qual_chk = Transition(label='Quality Check')
frame_assembly = Transition(label='Frame Assembly')
motor_inst = Transition(label='Motor Installation')
sensor_setup = Transition(label='Sensor Setup')
control_unit = Transition(label='Control Unit')
firmware_upload = Transition(label='Firmware Upload')
sys_calib = Transition(label='System Calibration')
flight_testing = Transition(label='Flight Testing')
error_corr = Transition(label='Error Correction')
cosmetic_finish = Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual = Transition(label='User Manual')
client_train = Transition(label='Client Training')
support_sched = Transition(label='Support Scheduling')

# Define transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[req_anal, comp_src])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[qual_chk, frame_assembly])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[motor_inst, sensor_setup])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[control_unit, firmware_upload])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[sys_calib, flight_testing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[error_corr, cosmetic_finish])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, user_manual])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[client_train, support_sched])

# Define partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)