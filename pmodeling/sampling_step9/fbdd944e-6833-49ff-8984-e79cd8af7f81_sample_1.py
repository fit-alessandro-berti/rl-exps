import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[client_onboard, needs_assess])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[drone_config, route_program])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, insurance_verify])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[lease_contract, fleet_deploy])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[monitor_setup, usage_track])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, incident_manage])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[billing_process, performance_report])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[contract_renew, price_adjust])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect, skip])

# Define the partial order graph
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, loop9])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop9)
root.order.add_edge(loop9, loop1)

# Print the POWL model
print(root)