from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order
root = StrictPartialOrder()

# Add the transitions to the partial order
root.add_transition(client_onboard)
root.add_transition(needs_assess)
root.add_transition(drone_config)
root.add_transition(route_program)
root.add_transition(compliance_check)
root.add_transition(insurance_verify)
root.add_transition(lease_contract)
root.add_transition(fleet_deploy)
root.add_transition(monitor_setup)
root.add_transition(usage_track)
root.add_transition(maintenance_plan)
root.add_transition(incident_manage)
root.add_transition(billing_process)
root.add_transition(performance_report)
root.add_transition(contract_renew)
root.add_transition(price_adjust)
root.add_transition(feedback_collect)

# Define the control flow operators
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[client_onboard, needs_assess]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[drone_config, route_program]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[compliance_check, insurance_verify]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[lease_contract, fleet_deploy]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[monitor_setup, usage_track]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, incident_manage]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[billing_process, performance_report]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[contract_renew, price_adjust]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, route_program]))

# Add the loop for the drone customization
loop = OperatorPOWL(operator=Operator.LOOP, children=[drone_config, route_program])
root.add_operator(loop)

# Add the loop for the usage tracking
usage_loop = OperatorPOWL(operator=Operator.LOOP, children=[usage_track, maintenance_plan])
root.add_operator(usage_loop)

# Add the loop for the incident management
incident_loop = OperatorPOWL(operator=Operator.LOOP, children=[incident_manage, billing_process])
root.add_operator(incident_loop)

# Add the loop for the performance reporting
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[performance_report, contract_renew])
root.add_operator(report_loop)

# Add the loop for the price adjustment
price_loop = OperatorPOWL(operator=Operator.LOOP, children=[price_adjust, feedback_collect])
root.add_operator(price_loop)

# Add the loop for the feedback collection
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect, route_program])
root.add_operator(feedback_loop)

# Add the loop for the contract renewal
renew_loop = OperatorPOWL(operator=Operator.LOOP, children=[contract_renew, price_adjust])
root.add_operator(renew_loop)

# Define the dependencies
root.add_edge(client_onboard, needs_assess)
root.add_edge(needs_assess, drone_config)
root.add_edge(drone_config, route_program)
root.add_edge(route_program, compliance_check)
root.add_edge(compliance_check, insurance_verify)
root.add_edge(insurance_verify, lease_contract)
root.add_edge(lease_contract, fleet_deploy)
root.add_edge(fleet_deploy, monitor_setup)
root.add_edge(monitor_setup, usage_track)
root.add_edge(usage_track, maintenance_plan)
root.add_edge(maintenance_plan, incident_manage)
root.add_edge(incident_manage, billing_process)
root.add_edge(billing_process, performance_report)
root.add_edge(performance_report, contract_renew)
root.add_edge(contract_renew, price_adjust)
root.add_edge(price_adjust, feedback_collect)
root.add_edge(feedback_collect, route_program)

# Print the root model
print(root)