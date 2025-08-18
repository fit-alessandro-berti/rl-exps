import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the activities
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

# Define the loops and choices
# Client Onboard, Needs Assess, Drone Config, Route Program, Compliance Check, Insurance Verify, Lease Contract, Fleet Deploy, Monitor Setup, Usage Track, Maintenance Plan, Incident Manage, Billing Process, Performance Report, Contract Renew, Price Adjust, Feedback Collect
# are all concurrent activities, so we define a silent transition to represent concurrency
skip = SilentTransition()

# Define the loop for the activities
loop_activities = [client_onboard, needs_assess, drone_config, route_program, compliance_check, insurance_verify, lease_contract, fleet_deploy, monitor_setup, usage_track, maintenance_plan, incident_manage, billing_process, performance_report, contract_renew, price_adjust, feedback_collect]
loop = OperatorPOWL(operator=Operator.LOOP, children=loop_activities)

# Define the XOR for the activities
xor_activities = [maintenance_plan, incident_manage, feedback_collect]
xor = OperatorPOWL(operator=Operator.XOR, children=xor_activities)

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)