import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    client_onboard, needs_assess, drone_config, route_program, compliance_check,
    insurance_verify, lease_contract, fleet_deploy, monitor_setup, usage_track,
    maintenance_plan, incident_manage, billing_process, performance_report,
    contract_renew, price_adjust, feedback_collect
])

# Define the dependencies between activities
root.order.add_edge(client_onboard, needs_assess)
root.order.add_edge(needs_assess, drone_config)
root.order.add_edge(drone_config, route_program)
root.order.add_edge(route_program, compliance_check)
root.order.add_edge(compliance_check, insurance_verify)
root.order.add_edge(insurance_verify, lease_contract)
root.order.add_edge(lease_contract, fleet_deploy)
root.order.add_edge(fleet_deploy, monitor_setup)
root.order.add_edge(monitor_setup, usage_track)
root.order.add_edge(usage_track, maintenance_plan)
root.order.add_edge(maintenance_plan, incident_manage)
root.order.add_edge(incident_manage, billing_process)
root.order.add_edge(billing_process, performance_report)
root.order.add_edge(performance_report, contract_renew)
root.order.add_edge(contract_renew, price_adjust)
root.order.add_edge(price_adjust, feedback_collect)

# Print the POWL model
print(root)