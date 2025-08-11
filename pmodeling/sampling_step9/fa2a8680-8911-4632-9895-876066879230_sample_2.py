import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
client_meet = Transition(label='Client Meet')
req_gather = Transition(label='Requirement Gather')
module_design = Transition(label='Module Design')
supplier_vet = Transition(label='Supplier Vetting')
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

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the loop nodes
loop_fleet_deploy = OperatorPOWL(operator=Operator.LOOP, children=[fleet_deploy])
loop_performance_tune = OperatorPOWL(operator=Operator.LOOP, children=[performance_tune])

# Define the exclusive choice nodes
xor_test_analysis = OperatorPOWL(operator=Operator.XOR, children=[test_analysis, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[client_meet, req_gather, module_design, supplier_vet, component_order, prototype_build, field_testing, xor_test_analysis, software_setup, data_integration, pilot_train, compliance_check, loop_fleet_deploy, loop_performance_tune, remote_monitor, maintenance_plan, performance_tune])
root.order.add_edge(client_meet, req_gather)
root.order.add_edge(req_gather, module_design)
root.order.add_edge(module_design, supplier_vet)
root.order.add_edge(supplier_vet, component_order)
root.order.add_edge(component_order, prototype_build)
root.order.add_edge(prototype_build, field_testing)
root.order.add_edge(field_testing, xor_test_analysis)
root.order.add_edge(xor_test_analysis, software_setup)
root.order.add_edge(software_setup, data_integration)
root.order.add_edge(data_integration, pilot_train)
root.order.add_edge(pilot_train, compliance_check)
root.order.add_edge(compliance_check, loop_fleet_deploy)
root.order.add_edge(loop_fleet_deploy, remote_monitor)
root.order.add_edge(remote_monitor, maintenance_plan)
root.order.add_edge(maintenance_plan, loop_performance_tune)
root.order.add_edge(loop_performance_tune, performance_tune)