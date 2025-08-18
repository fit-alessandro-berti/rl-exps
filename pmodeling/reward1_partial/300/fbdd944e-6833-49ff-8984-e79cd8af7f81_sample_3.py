import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
client_onboard = Transition(label='Client Onboard')
needs_assess = Transition(label='Needs Assess')
drone_config = Transition(label='Drone Config')
route_program = Transition(label='Route Program')
compliance_check = Transition(label='Compliance Check')
insurance_verify = Transition(label='Insurance Verify')
lease_contract = Transition(label='Lease Contract')
fleet_deploy = Transition(label='Fleet Deploy')
monitor_setup = Transition(label='Monitor Setup')
usage_track = Transition(label='Usage Track')
maintenance_plan = Transition(label='Maintenance Plan')
incident_manage = Transition(label='Incident Manage')
billing_process = Transition(label='Billing Process')
performance_report = Transition(label='Performance Report')
contract_renew = Transition(label='Contract Renew')
price_adjust = Transition(label='Price Adjust')
feedback_collect = Transition(label='Feedback Collect')

# Define the process flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, insurance_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, incident_manage])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[billing_process, performance_report])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[contract_renew, price_adjust])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, SilentTransition()])

root = StrictPartialOrder(nodes=[client_onboard, needs_assess, drone_config, route_program, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(client_onboard, needs_assess)
root.order.add_edge(needs_assess, drone_config)
root.order.add_edge(drone_config, route_program)
root.order.add_edge(route_program, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, fleet_deploy)
root.order.add_edge(fleet_deploy, monitor_setup)
root.order.add_edge(monitor_setup, usage_track)

print(root)