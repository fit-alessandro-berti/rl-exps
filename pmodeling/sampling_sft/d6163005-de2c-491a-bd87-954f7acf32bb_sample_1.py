import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
req = Transition(label='Requirement Analysis')
comp = Transition(label='Component Sourcing')
qual = Transition(label='Quality Check')
frame = Transition(label='Frame Assembly')
motor = Transition(label='Motor Installation')
sensor = Transition(label='Sensor Setup')
control = Transition(label='Control Unit')
firmware = Transition(label='Firmware Upload')
calib = Transition(label='System Calibration')
flight = Transition(label='Flight Testing')
error = Transition(label='Error Correction')
finish = Transition(label='Cosmetic Finish')
pack = Transition(label='Packaging Prep')
manual = Transition(label='User Manual')
train = Transition(label='Client Training')
support = Transition(label='Support Scheduling')

# Build the loop for iterative flight testing
# A: Flight Testing -> Error Correction
# B: (silent) -> Flight Testing -> Error Correction (repeat)
loop_body = StrictPartialOrder(nodes=[flight, error])
loop_body.order.add_edge(flight, error)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, flight])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    req, comp, qual, frame, motor, sensor, control,
    firmware, calib, loop,
    finish, pack, manual, train, support
])

# Define the control-flow dependencies
root.order.add_edge(req, comp)
root.order.add_edge(comp, qual)
root.order.add_edge(qual, frame)
root.order.add_edge(frame, motor)
root.order.add_edge(frame, sensor)
root.order.add_edge(frame, control)
root.order.add_edge(motor, firmware)
root.order.add_edge(sensor, firmware)
root.order.add_edge(control, firmware)
root.order.add_edge(firmware, calib)
root.order.add_edge(calib, loop)
root.order.add_edge(loop, finish)
root.order.add_edge(finish, pack)
root.order.add_edge(pack, manual)
root.order.add_edge(manual, train)
root.order.add_edge(train, support)