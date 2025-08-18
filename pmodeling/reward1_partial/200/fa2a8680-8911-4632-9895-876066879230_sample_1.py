import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
client_meet = Transition(label='Client Meet')
gather_requirements = Transition(label='Requirement Gather')
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

# Define silent transitions for no-operation
skip = SilentTransition()

# Define loop for field testing and analysis
loop_field_testing_analysis = OperatorPOWL(operator=Operator.LOOP, children=[field_testing, test_analysis])

# Define exclusive choice for software setup and data integration
xor_software_data = OperatorPOWL(operator=Operator.XOR, children=[software_setup, data_integration])

# Define exclusive choice for pilot training and compliance check
xor_pilot_compliance = OperatorPOWL(operator=Operator.XOR, children=[pilot_train, compliance_check])

# Define exclusive choice for maintenance plan and performance tune
xor_maintenance_performance = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, performance_tune])

# Define root POWL model with all activities and loops
root = StrictPartialOrder(nodes=[
    client_meet, gather_requirements, module_design, supplier_vetting, component_order,
    prototype_build, loop_field_testing_analysis, xor_software_data, xor_pilot_compliance,
    xor_maintenance_performance, fleet_deploy, remote_monitor
])
root.order.add_edge(client_meet, gather_requirements)
root.order.add_edge(gather_requirements, module_design)
root.order.add_edge(module_design, supplier_vetting)
root.order.add_edge(supplier_vetting, component_order)
root.order.add_edge(component_order, prototype_build)
root.order.add_edge(prototype_build, loop_field_testing_analysis)
root.order.add_edge(loop_field_testing_analysis, xor_software_data)
root.order.add_edge(xor_software_data, xor_pilot_compliance)
root.order.add_edge(xor_pilot_compliance, xor_maintenance_performance)
root.order.add_edge(xor_maintenance_performance, fleet_deploy)
root.order.add_edge(fleet_deploy, remote_monitor)