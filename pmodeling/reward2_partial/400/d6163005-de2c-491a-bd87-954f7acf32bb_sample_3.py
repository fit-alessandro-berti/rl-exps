import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
req_anal = Transition(label='Requirement Analysis')
comp_src = Transition(label='Component Sourcing')
qual_chk = Transition(label='Quality Check')
frame_assem = Transition(label='Frame Assembly')
mot_inst = Transition(label='Motor Installation')
sensor_setup = Transition(label='Sensor Setup')
ctrl_unit = Transition(label='Control Unit')
firmware_upload = Transition(label='Firmware Upload')
sys_calib = Transition(label='System Calibration')
flight_test = Transition(label='Flight Testing')
error_corr = Transition(label='Error Correction')
cosmetic_finish = Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual = Transition(label='User Manual')
client_train = Transition(label='Client Training')
support_sched = Transition(label='Support Scheduling')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    req_anal, comp_src, qual_chk, frame_assem, mot_inst, sensor_setup, ctrl_unit, firmware_upload, sys_calib, flight_test, error_corr, cosmetic_finish, packaging_prep, user_manual, client_train, support_sched
])

# Define the dependencies between activities
root.order.add_edge(req_anal, comp_src)
root.order.add_edge(comp_src, qual_chk)
root.order.add_edge(qual_chk, frame_assem)
root.order.add_edge(frame_assem, mot_inst)
root.order.add_edge(mot_inst, sensor_setup)
root.order.add_edge(sensor_setup, ctrl_unit)
root.order.add_edge(ctrl_unit, firmware_upload)
root.order.add_edge(firmware_upload, sys_calib)
root.order.add_edge(sys_calib, flight_test)
root.order.add_edge(flight_test, error_corr)
root.order.add_edge(error_corr, cosmetic_finish)
root.order.add_edge(cosmetic_finish, packaging_prep)
root.order.add_edge(packaging_prep, user_manual)
root.order.add_edge(user_manual, client_train)
root.order.add_edge(client_train, support_sched)

# Print the root model
print(root)