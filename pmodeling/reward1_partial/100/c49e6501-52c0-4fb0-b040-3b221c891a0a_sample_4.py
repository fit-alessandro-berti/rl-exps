import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the process structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[StressTest, SoftwarePatch])
xor = OperatorPOWL(operator=Operator.XOR, children=[AlgorithmTune, skip])
root = StrictPartialOrder(nodes=[ComponentCheck, SpecReview, PartsSorting, MechanicalFit, FirmwareLoad, CalibrationRun, loop, xor, ValidationPass, DataLink, OnsiteDeploy, LiveMonitor, UpdatePush, RecoveryPlan, MaintenanceLog])
root.order.add_edge(ValidationPass, DataLink)
root.order.add_edge(DataLink, OnsiteDeploy)
root.order.add_edge(OnsiteDeploy, LiveMonitor)
root.order.add_edge(LiveMonitor, UpdatePush)
root.order.add_edge(UpdatePush, RecoveryPlan)
root.order.add_edge(RecoveryPlan, MaintenanceLog)

print(root)