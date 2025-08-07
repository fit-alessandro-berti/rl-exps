import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
req_analysis   = Transition(label='Requirement Analysis')
comp_sourcing  = Transition(label='Component Sourcing')
quality_check  = Transition(label='Quality Check')
frame_assem    = Transition(label='Frame Assembly')
motor_install  = Transition(label='Motor Installation')
sensor_setup   = Transition(label='Sensor Setup')
control_unit   = Transition(label='Control Unit')
firmware_upload= Transition(label='Firmware Upload')
system_calib   = Transition(label='System Calibration')
flight_test    = Transition(label='Flight Testing')
error_corr     = Transition(label='Error Correction')
cosmetic_finish= Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual    = Transition(label='User Manual')
client_train   = Transition(label='Client Training')
support_sched  = Transition(label='Support Scheduling')

# Define the flight testing loop: do Flight Testing, then optionally do Error Correction and Flight Testing again
flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flight_test, error_corr]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    req_analysis,
    comp_sourcing,
    quality_check,
    frame_assem,
    motor_install,
    sensor_setup,
    control_unit,
    firmware_upload,
    system_calib,
    flight_loop,
    cosmetic_finish,
    packaging_prep,
    user_manual,
    client_train,
    support_sched
])

# Add ordering constraints
root.order.add_edge(req_analysis,   comp_sourcing)
root.order.add_edge(comp_sourcing,  quality_check)
root.order.add_edge(quality_check,  frame_assem)
root.order.add_edge(frame_assem,    motor_install)
root.order.add_edge(frame_assem,    sensor_setup)
root.order.add_edge(frame_assem,    control_unit)
root.order.add_edge(motor_install,  firmware_upload)
root.order.add_edge(sensor_setup,   firmware_upload)
root.order.add_edge(control_unit,   firmware_upload)
root.order.add_edge(firmware_upload, system_calib)
root.order.add_edge(system_calib,   flight_loop)
root.order.add_edge(flight_loop,    cosmetic_finish)
root.order.add_edge(cosmetic_finish, packaging_prep)
root.order.add_edge(packaging_prep, user_manual)
root.order.add_edge(user_manual,    client_train)
root.order.add_edge(client_train,   support_sched)