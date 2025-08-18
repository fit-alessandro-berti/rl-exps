from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
component_check = Transition(label='Component Check')
spec_review = Transition(label='Spec Review')
parts_sorting = Transition(label='Parts Sorting')
mechanical_fit = Transition(label='Mechanical Fit')
firmware_load = Transition(label='Firmware Load')
calibration_run = Transition(label='Calibration Run')
stress_test = Transition(label='Stress Test')
software_patch = Transition(label='Software Patch')
algorithm_tune = Transition(label='Algorithm Tune')
comms_setup = Transition(label='Comms Setup')
validation_pass = Transition(label='Validation Pass')
data_link = Transition(label='Data Link')
onsite_deploy = Transition(label='Onsite Deploy')
live_monitor = Transition(label='Live Monitor')
update_push = Transition(label='Update Push')
recovery_plan = Transition(label='Recovery Plan')
maintenance_log = Transition(label='Maintenance Log')

skip = SilentTransition()

# Define the process tree structure
component_check_tree = OperatorPOWL(operator=Operator.AND, children=[component_check, spec_review])
parts_sorting_tree = OperatorPOWL(operator=Operator.AND, children=[parts_sorting, mechanical_fit])
firmware_load_tree = OperatorPOWL(operator=Operator.AND, children=[firmware_load, calibration_run])
stress_test_tree = OperatorPOWL(operator=Operator.AND, children=[stress_test, software_patch, algorithm_tune, comms_setup])
validation_pass_tree = OperatorPOWL(operator=Operator.AND, children=[validation_pass, data_link, onsite_deploy])
live_monitor_tree = OperatorPOWL(operator=Operator.AND, children=[live_monitor, update_push])
maintenance_log_tree = OperatorPOWL(operator=Operator.AND, children=[maintenance_log, recovery_plan])

# Define the partial order
root = StrictPartialOrder(nodes=[
    component_check_tree,
    parts_sorting_tree,
    firmware_load_tree,
    stress_test_tree,
    validation_pass_tree,
    live_monitor_tree,
    maintenance_log_tree
])

# Define the dependencies between nodes
root.order.add_edge(component_check_tree, parts_sorting_tree)
root.order.add_edge(parts_sorting_tree, mechanical_fit)
root.order.add_edge(firmware_load_tree, calibration_run)
root.order.add_edge(stress_test_tree, software_patch)
root.order.add_edge(stress_test_tree, algorithm_tune)
root.order.add_edge(stress_test_tree, comms_setup)
root.order.add_edge(validation_pass_tree, data_link)
root.order.add_edge(validation_pass_tree, onsite_deploy)
root.order.add_edge(live_monitor_tree, update_push)
root.order.add_edge(maintenance_log_tree, recovery_plan)

# Print the resulting POWL model
print(root)