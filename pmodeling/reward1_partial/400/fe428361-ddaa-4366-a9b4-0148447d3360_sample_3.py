from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
client_consult = Transition(label='Client Consult')
payload_assess = Transition(label='Payload Assess')
drone_configure = Transition(label='Drone Configure')
regulation_check = Transition(label='Regulation Check')
flight_simulate = Transition(label='Flight Simulate')
route_optimize = Transition(label='Route Optimize')
package_secure = Transition(label='Package Secure')
pre_flight_inspect = Transition(label='Pre-Flight Inspect')
weather_monitor = Transition(label='Weather Monitor')
launch_drone = Transition(label='Launch Drone')
flight_track = Transition(label='Flight Track')
delivery_confirm = Transition(label='Delivery Confirm')
data_analyze = Transition(label='Data Analyze')
feedback_collect = Transition(label='Feedback Collect')
warranty_register = Transition(label='Warranty Register')
issue_resolve = Transition(label='Issue Resolve')
package_return = Transition(label='Package Return')

# Define the control flow
xor = OperatorPOWL(operator=Operator.XOR, children=[
    regulation_check,
    SilentTransition(label='No Regulation Check')
])

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    flight_simulate,
    route_optimize,
    package_secure,
    pre_flight_inspect,
    weather_monitor,
    launch_drone,
    flight_track,
    delivery_confirm,
    data_analyze,
    feedback_collect,
    warranty_register,
    issue_resolve,
    package_return
])

root = StrictPartialOrder(nodes=[client_consult, payload_assess, drone_configure, xor, loop])
root.order.add_edge(client_consult, payload_assess)
root.order.add_edge(payload_assess, drone_configure)
root.order.add_edge(drone_configure, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor)

print(root)