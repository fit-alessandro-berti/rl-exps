import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the process steps
stress_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[stress_test])
software_patch_loop = OperatorPOWL(operator=Operator.LOOP, children=[software_patch])
algorithm_tune_loop = OperatorPOWL(operator=Operator.LOOP, children=[algorithm_tune])
update_push_loop = OperatorPOWL(operator=Operator.LOOP, children=[update_push])

# Define the choices and loops
spec_review_choice = OperatorPOWL(operator=Operator.XOR, children=[spec_review, skip])
parts_sorting_choice = OperatorPOWL(operator=Operator.XOR, children=[parts_sorting, skip])
mechanical_fit_choice = OperatorPOWL(operator=Operator.XOR, children=[mechanical_fit, skip])
firmware_load_choice = OperatorPOWL(operator=Operator.XOR, children=[firmware_load, skip])
calibration_run_choice = OperatorPOWL(operator=Operator.XOR, children=[calibration_run, skip])
stress_test_choice = OperatorPOWL(operator=Operator.XOR, children=[stress_test, skip])
software_patch_choice = OperatorPOWL(operator=Operator.XOR, children=[software_patch, skip])
algorithm_tune_choice = OperatorPOWL(operator=Operator.XOR, children=[algorithm_tune, skip])
comms_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[comms_setup, skip])
update_push_choice = OperatorPOWL(operator=Operator.XOR, children=[update_push, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    component_check,
    spec_review_choice,
    parts_sorting_choice,
    mechanical_fit_choice,
    firmware_load_choice,
    calibration_run_choice,
    stress_test_loop,
    software_patch_loop,
    algorithm_tune_loop,
    comms_setup_choice,
    update_push_loop,
    validation_pass,
    data_link,
    onsite_deploy,
    live_monitor,
    update_push_choice,
    recovery_plan,
    maintenance_log
])

# Add edges to the partial order
root.order.add_edge(component_check, spec_review_choice)
root.order.add_edge(spec_review_choice, parts_sorting_choice)
root.order.add_edge(parts_sorting_choice, mechanical_fit_choice)
root.order.add_edge(mechanical_fit_choice, firmware_load_choice)
root.order.add_edge(firmware_load_choice, calibration_run_choice)
root.order.add_edge(calibration_run_choice, stress_test_loop)
root.order.add_edge(stress_test_loop, software_patch_loop)
root.order.add_edge(software_patch_loop, algorithm_tune_loop)
root.order.add_edge(algorithm_tune_loop, comms_setup_choice)
root.order.add_edge(comms_setup_choice, update_push_loop)
root.order.add_edge(update_push_loop, validation_pass)
root.order.add_edge(validation_pass, data_link)
root.order.add_edge(data_link, onsite_deploy)
root.order.add_edge(onsite_deploy, live_monitor)
root.order.add_edge(live_monitor, update_push_choice)
root.order.add_edge(update_push_choice, recovery_plan)
root.order.add_edge(recovery_plan, maintenance_log)

# Print the final POWL model
print(root)