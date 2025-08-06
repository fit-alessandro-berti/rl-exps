import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
ComponentCheck = Transition(label='Component Check')
SpecReview = Transition(label='Spec Review')
PartsSorting = Transition(label='Parts Sorting')
MechanicalFit = Transition(label='Mechanical Fit')
FirmwareLoad = Transition(label='Firmware Load')
CalibrationRun = Transition(label='Calibration Run')
StressTest = Transition(label='Stress Test')
SoftwarePatch = Transition(label='Software Patch')
AlgorithmTune = Transition(label='Algorithm Tune')
CommsSetup = Transition(label='Comms Setup')
ValidationPass = Transition(label='Validation Pass')
DataLink = Transition(label='Data Link')
OnsiteDeploy = Transition(label='Onsite Deploy')
LiveMonitor = Transition(label='Live Monitor')
UpdatePush = Transition(label='Update Push')
RecoveryPlan = Transition(label='Recovery Plan')
MaintenanceLog = Transition(label='Maintenance Log')

# Define the partial order
root = StrictPartialOrder()

# Define the loop for the drone's life cycle
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    ComponentCheck, SpecReview, PartsSorting, MechanicalFit, FirmwareLoad, CalibrationRun, StressTest, SoftwarePatch, AlgorithmTune, CommsSetup, ValidationPass, DataLink, OnsiteDeploy, LiveMonitor, UpdatePush, RecoveryPlan, MaintenanceLog
])

# Add the loop to the root
root.nodes.append(loop)

# Define the exclusive choice for the end-to-end assembly
exclusiveChoice = OperatorPOWL(operator=Operator.XOR, children=[
    loop, RecoveryPlan
])

# Add the exclusive choice to the root
root.nodes.append(exclusiveChoice)

# Define the order between nodes
root.order.add_edge(loop, exclusiveChoice)

# Return the root
root