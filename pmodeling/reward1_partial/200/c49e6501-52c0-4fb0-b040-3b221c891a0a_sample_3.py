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

# Define the partial order
root = StrictPartialOrder(nodes=[
    ComponentCheck,
    SpecReview,
    PartsSorting,
    MechanicalFit,
    FirmwareLoad,
    CalibrationRun,
    StressTest,
    SoftwarePatch,
    AlgorithmTune,
    CommsSetup,
    ValidationPass,
    DataLink,
    OnsiteDeploy,
    LiveMonitor,
    UpdatePush,
    RecoveryPlan,
    MaintenanceLog
])

# Define the order
root.order.add_edge(ComponentCheck, SpecReview)
root.order.add_edge(SpecReview, PartsSorting)
root.order.add_edge(PartsSorting, MechanicalFit)
root.order.add_edge(MechanicalFit, FirmwareLoad)
root.order.add_edge(FirmwareLoad, CalibrationRun)
root.order.add_edge(CalibrationRun, StressTest)
root.order.add_edge(StressTest, SoftwarePatch)
root.order.add_edge(SoftwarePatch, AlgorithmTune)
root.order.add_edge(AlgorithmTune, CommsSetup)
root.order.add_edge(CommsSetup, ValidationPass)
root.order.add_edge(ValidationPass, DataLink)
root.order.add_edge(DataLink, OnsiteDeploy)
root.order.add_edge(OnsiteDeploy, LiveMonitor)
root.order.add_edge(LiveMonitor, UpdatePush)
root.order.add_edge(UpdatePush, RecoveryPlan)
root.order.add_edge(RecoveryPlan, MaintenanceLog)

# Print the root model
print(root)