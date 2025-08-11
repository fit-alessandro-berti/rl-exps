import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop node for firmware and software patching
firmwareLoop = OperatorPOWL(operator=Operator.LOOP, children=[FirmwareLoad, SoftwarePatch])
softwareLoop = OperatorPOWL(operator=Operator.LOOP, children=[AlgorithmTune, CommsSetup])

# Define the parallel activities for validation and deployment
validation = OperatorPOWL(operator=Operator.XOR, children=[ValidationPass, skip])
deployment = OperatorPOWL(operator=Operator.XOR, children=[OnsiteDeploy, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[ComponentCheck, SpecReview, PartsSorting, MechanicalFit, firmwareLoop, softwareLoop, ValidationPass, DataLink, deployment, LiveMonitor, UpdatePush, RecoveryPlan, MaintenanceLog])
root.order.add_edge(ComponentCheck, SpecReview)
root.order.add_edge(SpecReview, PartsSorting)
root.order.add_edge(PartsSorting, MechanicalFit)
root.order.add_edge(MechanicalFit, firmwareLoop)
root.order.add_edge(firmwareLoop, softwareLoop)
root.order.add_edge(softwareLoop, ValidationPass)
root.order.add_edge(ValidationPass, DataLink)
root.order.add_edge(DataLink, deployment)
root.order.add_edge(deployment, LiveMonitor)
root.order.add_edge(LiveMonitor, UpdatePush)
root.order.add_edge(UpdatePush, RecoveryPlan)
root.order.add_edge(RecoveryPlan, MaintenanceLog)