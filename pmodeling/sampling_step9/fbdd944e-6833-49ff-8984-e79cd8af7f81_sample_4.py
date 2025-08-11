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

# Define silent transitions
skip = SilentTransition()

# Define the loops and exclusive choices
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check])
insurance_loop = OperatorPOWL(operator=Operator.LOOP, children=[insurance_verify])
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan])
incident_loop = OperatorPOWL(operator=Operator.LOOP, children=[incident_manage])
contract_renew_loop = OperatorPOWL(operator=Operator.LOOP, children=[contract_renew])

# Define the exclusive choices
client_onboard_xor = OperatorPOWL(operator=Operator.XOR, children=[client_onboard, skip])
needs_assess_xor = OperatorPOWL(operator=Operator.XOR, children=[needs_assess, skip])
drone_config_xor = OperatorPOWL(operator=Operator.XOR, children=[drone_config, skip])
route_program_xor = OperatorPOWL(operator=Operator.XOR, children=[route_program, skip])
insurance_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[insurance_verify, skip])
maintenance_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, skip])
incident_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[incident_manage, skip])
contract_renew_xor = OperatorPOWL(operator=Operator.XOR, children=[contract_renew, skip])
price_adjust_xor = OperatorPOWL(operator=Operator.XOR, children=[price_adjust, skip])
feedback_collect_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])

# Create the root model
root = StrictPartialOrder(nodes=[
    client_onboard_xor, needs_assess_xor, drone_config_xor, route_program_xor,
    compliance_loop, insurance_loop, maintenance_loop, incident_loop, contract_renew_loop,
    usage_track, billing_process, performance_report, price_adjust_xor, feedback_collect_xor
])

# Add dependencies between nodes
root.order.add_edge(client_onboard_xor, needs_assess_xor)
root.order.add_edge(needs_assess_xor, drone_config_xor)
root.order.add_edge(drone_config_xor, route_program_xor)
root.order.add_edge(route_program_xor, compliance_loop)
root.order.add_edge(compliance_loop, insurance_loop)
root.order.add_edge(insurance_loop, maintenance_loop)
root.order.add_edge(maintenance_loop, incident_loop)
root.order.add_edge(incident_loop, contract_renew_loop)
root.order.add_edge(contract_renew_loop, usage_track)
root.order.add_edge(usage_track, billing_process)
root.order.add_edge(billing_process, performance_report)
root.order.add_edge(performance_report, price_adjust_xor)
root.order.add_edge(price_adjust_xor, feedback_collect_xor)

# Print the root model
print(root)