from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions (tau labels)
skip = SilentTransition()

# Define the control flow
loop = OperatorPOWL(operator=Operator.LOOP, children=[mechanical_fit, calibration_run, stress_test])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[software_patch, algorithm_tune])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[comms_setup, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[validation_pass, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_link, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[onsite_deploy, live_monitor])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[update_push, recovery_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[maintenance_log, skip])

# Create the root node with the defined transitions and their order
root = StrictPartialOrder(nodes=[
    component_check, spec_review, parts_sorting, loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7
])
root.order.add_edge(component_check, spec_review)
root.order.add_edge(spec_review, parts_sorting)
root.order.add_edge(parts_sorting, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, skip)