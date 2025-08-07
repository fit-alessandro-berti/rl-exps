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

# Define the partial order
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

# Add dependencies if any (in this case, there are none specified in the problem description)
# order.add_edge(component_check, spec_review)
# order.add_edge(component_check, parts_sorting)
# order.add_edge(component_check, mechanical_fit)
# order.add_edge(component_check, firmware_load)
# order.add_edge(component_check, calibration_run)
# order.add_edge(component_check, stress_test)
# order.add_edge(component_check, software_patch)
# order.add_edge(component_check, algorithm_tune)
# order.add_edge(component_check, comms_setup)
# order.add_edge(component_check, validation_pass)
# order.add_edge(component_check, data_link)
# order.add_edge(component_check, onsite_deploy)
# order.add_edge(component_check, live_monitor)
# order.add_edge(component_check, update_push)
# order.add_edge(component_check, recovery_plan)
# order.add_edge(component_check, maintenance_log)

# The root variable now holds the defined POWL model