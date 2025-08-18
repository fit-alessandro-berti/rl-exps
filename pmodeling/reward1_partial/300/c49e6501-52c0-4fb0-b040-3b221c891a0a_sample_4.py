import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define POWL models
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[stress_test, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[software_patch, algorithm_tune])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[comms_setup, maintenance_log])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[update_push, recovery_plan])

loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[spec_review, parts_sorting])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[mechanical_fit, firmware_load])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[calibration_run, xor_1])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[data_link, xor_2])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[live_monitor, xor_3])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[onsite_deploy, xor_4])

# Define root
root = StrictPartialOrder(nodes=[component_check, loop_1, loop_2, loop_3, loop_4, loop_5, loop_6])
root.order.add_edge(component_check, loop_1)
root.order.add_edge(component_check, loop_2)
root.order.add_edge(component_check, loop_3)
root.order.add_edge(component_check, loop_4)
root.order.add_edge(component_check, loop_5)
root.order.add_edge(component_check, loop_6)