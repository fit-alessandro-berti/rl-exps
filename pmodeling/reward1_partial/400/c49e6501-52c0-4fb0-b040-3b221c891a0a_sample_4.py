import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[spec_review, parts_sorting])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[mechanical_fit, firmware_load])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[calibration_run, stress_test])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[software_patch, algorithm_tune])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[comms_setup, validation_pass])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[data_link, onsite_deploy])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[live_monitor, update_push])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, maintenance_log])

# Create the POWL model
root = StrictPartialOrder(nodes=[
    component_check,
    choice1,
    choice2,
    choice3,
    choice4,
    choice5,
    choice6,
    choice7,
    choice8
])

# Add dependencies
root.order.add_edge(component_check, choice1)
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)

# Print the POWL model
print(root)