import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
client_onboard    = Transition(label='Client Onboard')
needs_assess      = Transition(label='Needs Assess')
drone_config      = Transition(label='Drone Config')
route_program     = Transition(label='Route Program')
compliance_check  = Transition(label='Compliance Check')
insurance_verify  = Transition(label='Insurance Verify')
lease_contract    = Transition(label='Lease Contract')
fleet_deploy      = Transition(label='Fleet Deploy')
monitor_setup     = Transition(label='Monitor Setup')
usage_track       = Transition(label='Usage Track')
maintenance_plan  = Transition(label='Maintenance Plan')
incident_manage   = Transition(label='Incident Manage')
billing_process   = Transition(label='Billing Process')
performance_report= Transition(label='Performance Report')
contract_renew    = Transition(label='Contract Renew')
price_adjust      = Transition(label='Price Adjust')
feedback_collect  = Transition(label='Feedback Collect')

# Silent transition for loop exits
skip = SilentTransition()

# Build the maintenance loop: do Maintenance Plan, then either exit or do Incident Manage and Maintenance Plan again
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, incident_manage])

# Build the billing loop: do Billing Process, then either exit or do Price Adjust and Billing Process again
billing_loop = OperatorPOWL(operator=Operator.LOOP, children=[billing_process, price_adjust])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    client_onboard, needs_assess, drone_config, route_program,
    compliance_check, insurance_verify, lease_contract, fleet_deploy,
    monitor_setup, usage_track, maintenance_loop,
    billing_loop, performance_report, contract_renew,
    feedback_collect
])

# Add the control-flow edges
root.order.add_edge(client_onboard,     needs_assess)
root.order.add_edge(needs_assess,       drone_config)
root.order.add_edge(drone_config,       route_program)
root.order.add_edge(route_program,      compliance_check)
root.order.add_edge(compliance_check,   insurance_verify)
root.order.add_edge(insurance_verify,   lease_contract)
root.order.add_edge(lease_contract,     fleet_deploy)
root.order.add_edge(fleet_deploy,       monitor_setup)
root.order.add_edge(monitor_setup,      usage_track)
root.order.add_edge(usage_track,        maintenance_loop)
root.order.add_edge(maintenance_loop,   billing_loop)
root.order.add_edge(billing_loop,       performance_report)
root.order.add_edge(performance_report, contract_renew)
root.order.add_edge(contract_renew,     feedback_collect)