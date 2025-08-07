import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
comp_check   = Transition(label='Component Check')
spec_review  = Transition(label='Spec Review')
parts_sort   = Transition(label='Parts Sorting')
mech_fit     = Transition(label='Mechanical Fit')
firmware_load= Transition(label='Firmware Load')
calibration  = Transition(label='Calibration Run')
stress_test  = Transition(label='Stress Test')
software_patch=Transition(label='Software Patch')
algorithm_tune=Transition(label='Algorithm Tune')
comms_setup  = Transition(label='Comms Setup')
validation   = Transition(label='Validation Pass')
data_link    = Transition(label='Data Link')
onsite_deploy= Transition(label='Onsite Deploy')
live_monitor = Transition(label='Live Monitor')
update_push  = Transition(label='Update Push')
recovery_plan= Transition(label='Recovery Plan')
maintenance_log= Transition(label='Maintenance Log')

# Loop for iterative firmware updates: run update_push, then either exit or do recovery_plan then update_push again
update_loop = OperatorPOWL(operator=Operator.LOOP, children=[update_push, recovery_plan])

# Build the partial order
root = StrictPartialOrder(nodes=[
    comp_check, spec_review, parts_sort, mech_fit, firmware_load,
    calibration, stress_test, software_patch, algorithm_tune,
    comms_setup, validation, data_link, onsite_deploy,
    live_monitor, update_loop, maintenance_log
])

# Add control-flow edges
root.order.add_edge(comp_check, spec_review)
root.order.add_edge(spec_review, parts_sort)
root.order.add_edge(parts_sort, mech_fit)
root.order.add_edge(mech_fit, firmware_load)
root.order.add_edge(firmware_load, calibration)
root.order.add_edge(calibration, stress_test)
root.order.add_edge(stress_test, software_patch)
root.order.add_edge(software_patch, algorithm_tune)
root.order.add_edge(algorithm_tune, comms_setup)
root.order.add_edge(comms_setup, validation)
root.order.add_edge(validation, data_link)
root.order.add_edge(data_link, onsite_deploy)
root.order.add_edge(onsite_deploy, live_monitor)
root.order.add_edge(live_monitor, update_loop)
root.order.add_edge(update_loop, live_monitor)
root.order.add_edge(live_monitor, maintenance_log)