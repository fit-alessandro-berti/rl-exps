import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.petri_net.obj import PetriNet, Marking

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[stress_test, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[software_patch, algorithm_tune])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[comms_setup, maintenance_log])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[update_push, recovery_plan])
choice1 = OperatorPOWL(operator=Operator.XOR, children=[validation_pass, skip])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[data_link, onsite_deploy])

# Define the root POWL model
root = StrictPartialOrder(nodes=[component_check, spec_review, parts_sorting, mechanical_fit, firmware_load, calibration_run, loop1, loop2, loop3, loop4, choice1, choice2, live_monitor, onsite_deploy])
root.order.add_edge(component_check, spec_review)
root.order.add_edge(spec_review, parts_sorting)
root.order.add_edge(parts_sorting, mechanical_fit)
root.order.add_edge(mechanical_fit, firmware_load)
root.order.add_edge(firmware_load, calibration_run)
root.order.add_edge(calibration_run, loop1)
root.order.add_edge(loop1, stress_test)
root.order.add_edge(stress_test, loop2)
root.order.add_edge(loop2, software_patch)
root.order.add_edge(software_patch, algorithm_tune)
root.order.add_edge(algorithm_tune, loop3)
root.order.add_edge(loop3, comms_setup)
root.order.add_edge(comms_setup, maintenance_log)
root.order.add_edge(maintenance_log, loop4)
root.order.add_edge(loop4, update_push)
root.order.add_edge(update_push, recovery_plan)
root.order.add_edge(recovery_plan, loop1)
root.order.add_edge(loop1, choice1)
root.order.add_edge(choice1, validation_pass)
root.order.add_edge(validation_pass, live_monitor)
root.order.add_edge(live_monitor, onsite_deploy)
root.order.add_edge(onsite_deploy, data_link)
root.order.add_edge(data_link, onsite_deploy)