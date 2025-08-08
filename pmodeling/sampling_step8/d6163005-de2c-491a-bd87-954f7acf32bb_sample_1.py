from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
req_anal = Transition(label='Requirement Analysis')
comp_src = Transition(label='Component Sourcing')
qual_chk = Transition(label='Quality Check')
frame_asm = Transition(label='Frame Assembly')
motor_inst = Transition(label='Motor Installation')
sensor_set = Transition(label='Sensor Setup')
ctrl_unit = Transition(label='Control Unit')
firm_upl = Transition(label='Firmware Upload')
calib = Transition(label='System Calibration')
flight_test = Transition(label='Flight Testing')
error_corr = Transition(label='Error Correction')
cosmetic_finish = Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual = Transition(label='User Manual')
client_train = Transition(label='Client Training')
support_sched = Transition(label='Support Scheduling')

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    req_anal,
    comp_src,
    qual_chk,
    frame_asm,
    motor_inst,
    sensor_set,
    ctrl_unit,
    firm_upl,
    calib,
    flight_test,
    error_corr,
    cosmetic_finish,
    packaging_prep,
    user_manual,
    client_train,
    support_sched
])

# Define the partial order relationships
root.order.add_edge(req_anal, comp_src)
root.order.add_edge(comp_src, qual_chk)
root.order.add_edge(qual_chk, frame_asm)
root.order.add_edge(frame_asm, motor_inst)
root.order.add_edge(motor_inst, sensor_set)
root.order.add_edge(sensor_set, ctrl_unit)
root.order.add_edge(ctrl_unit, firm_upl)
root.order.add_edge(firm_upl, calib)
root.order.add_edge(calib, flight_test)
root.order.add_edge(flight_test, error_corr)
root.order.add_edge(error_corr, cosmetic_finish)
root.order.add_edge(cosmetic_finish, packaging_prep)
root.order.add_edge(packaging_prep, user_manual)
root.order.add_edge(user_manual, client_train)
root.order.add_edge(client_train, support_sched)

print(root)