from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
client_meet = Transition(label='Client Meet')
requirement_gather = Transition(label='Requirement Gather')
module_design = Transition(label='Module Design')
supplier_vetting = Transition(label='Supplier Vetting')
component_order = Transition(label='Component Order')
prototype_build = Transition(label='Prototype Build')
field_testing = Transition(label='Field Testing')
test_analysis = Transition(label='Test Analysis')
software_setup = Transition(label='Software Setup')
data_integration = Transition(label='Data Integration')
pilot_train = Transition(label='Pilot Train')
compliance_check = Transition(label='Compliance Check')
fleet_deploy = Transition(label='Fleet Deploy')
remote_monitor = Transition(label='Remote Monitor')
maintenance_plan = Transition(label='Maintenance Plan')
performance_tune = Transition(label='Performance Tune')

# Define the control flow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[module_design, supplier_vetting, component_order, prototype_build, field_testing, test_analysis, software_setup, data_integration])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pilot_train, compliance_check, fleet_deploy, remote_monitor, maintenance_plan, performance_tune])

# Define the root
root = StrictPartialOrder(nodes=[client_meet, requirement_gather, loop1, loop2])
root.order.add_edge(client_meet, requirement_gather)
root.order.add_edge(requirement_gather, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, client_meet)

print(root)