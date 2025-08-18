import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the dependencies between the nodes
root.order.add_edge(component_check, spec_review)
root.order.add_edge(spec_review, parts_sorting)
root.order.add_edge(parts_sorting, mechanical_fit)
root.order.add_edge(mechanical_fit, firmware_load)
root.order.add_edge(firmware_load, calibration_run)
root.order.add_edge(calibration_run, stress_test)
root.order.add_edge(stress_test, software_patch)
root.order.add_edge(software_patch, algorithm_tune)
root.order.add_edge(algorithm_tune, comms_setup)
root.order.add_edge(comms_setup, validation_pass)
root.order.add_edge(validation_pass, data_link)
root.order.add_edge(data_link, onsite_deploy)
root.order.add_edge(onsite_deploy, live_monitor)
root.order.add_edge(live_monitor, update_push)
root.order.add_edge(update_push, recovery_plan)
root.order.add_edge(recovery_plan, maintenance_log)

print(root)