import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    component_check,
    spec_review,
    parts_sorting,
    mechanical_fit,
    firmware_load,
    calibration_run,
    stress_test,
    software_patch,
    algorithm_tune,
    comms_setup,
    validation_pass,
    data_link,
    onsite_deploy,
    live_monitor,
    update_push,
    recovery_plan,
    maintenance_log
])

# Add dependencies if necessary
# For example, if 'stress_test' depends on 'mechanical_fit':
# root.order.add_edge(mechanical_fit, stress_test)

print(root)