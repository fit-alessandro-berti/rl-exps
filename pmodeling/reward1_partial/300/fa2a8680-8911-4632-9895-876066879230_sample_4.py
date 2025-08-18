import pm4py
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

# Define the workflow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[requirement_gather, module_design])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[supplier_vetting, component_order])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, field_testing])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[test_analysis, software_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_integration, pilot_train])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, fleet_deploy])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[remote_monitor, maintenance_plan])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[performance_tune, client_meet])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor1)

# Print the root of the POWL model
print(root)