from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the process steps
client_meet_choice = OperatorPOWL(operator=Operator.XOR, children=[client_meet, requirement_gather])
module_design_choice = OperatorPOWL(operator=Operator.XOR, children=[module_design, supplier_vetting])
component_order_choice = OperatorPOWL(operator=Operator.XOR, children=[component_order, prototype_build])
field_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[field_testing, test_analysis])
software_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[software_setup, data_integration])
pilot_train_choice = OperatorPOWL(operator=Operator.XOR, children=[pilot_train, compliance_check])
fleet_deploy_choice = OperatorPOWL(operator=Operator.XOR, children=[fleet_deploy, remote_monitor])
maintenance_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, performance_tune])

# Define the partial order
root = StrictPartialOrder(nodes=[client_meet_choice, module_design_choice, component_order_choice, field_testing_choice, software_setup_choice, pilot_train_choice, fleet_deploy_choice, maintenance_plan_choice])
root.order.add_edge(client_meet_choice, module_design_choice)
root.order.add_edge(module_design_choice, component_order_choice)
root.order.add_edge(component_order_choice, field_testing_choice)
root.order.add_edge(field_testing_choice, software_setup_choice)
root.order.add_edge(software_setup_choice, pilot_train_choice)
root.order.add_edge(pilot_train_choice, fleet_deploy_choice)
root.order.add_edge(fleet_deploy_choice, maintenance_plan_choice)

# Print the root POWL model
print(root)