import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transition (skip)
skip = SilentTransition()

# Define the POWL models for each activity
component_check_model = OperatorPOWL(operator=Operator.AND, children=[component_check, spec_review, parts_sorting, mechanical_fit])
firmware_load_model = OperatorPOWL(operator=Operator.AND, children=[firmware_load, calibration_run, stress_test])
software_patch_model = OperatorPOWL(operator=Operator.AND, children=[software_patch, algorithm_tune])
comms_setup_model = OperatorPOWL(operator=Operator.AND, children=[comms_setup, data_link])
onsite_deploy_model = OperatorPOWL(operator=Operator.AND, children=[live_monitor, update_push, recovery_plan, maintenance_log])

# Define the exclusive choice between firmware load and software patch
xor_model = OperatorPOWL(operator=Operator.XOR, children=[firmware_load_model, software_patch_model])

# Define the exclusive choice between comms setup and onsite deploy
xor_model_2 = OperatorPOWL(operator=Operator.XOR, children=[comms_setup_model, onsite_deploy])

# Define the root node
root = StrictPartialOrder(nodes=[xor_model, xor_model_2])

# Add edges to define the order of execution
root.order.add_edge(xor_model, xor_model_2)

print(root)