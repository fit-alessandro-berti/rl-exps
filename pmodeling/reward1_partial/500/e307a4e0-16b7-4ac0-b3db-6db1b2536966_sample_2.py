from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
InitialAssess = Transition(label='Initial Assess')
ArtifactScan = Transition(label='Artifact Scan')
ConditionMap = Transition(label='Condition Map')
MaterialTest = Transition(label='Material Test')
CleaningPhase = Transition(label='Cleaning Phase')
StabilityCheck = Transition(label='Stability Check')
MinorRepair = Transition(label='Minor Repair')
StructuralReinforce = Transition(label='Structural Reinforce')
SurfaceRestore = Transition(label='Surface Restore')
CoatingApply = Transition(label='Coating Apply')
EthicsReview = Transition(label='Ethics Review')
ProvenanceVerify = Transition(label='Provenance Verify')
ClientUpdate = Transition(label='Client Update')
FinalReport = Transition(label='Final Report')
ArchiveStore = Transition(label='Archive Store')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        InitialAssess,
        ArtifactScan,
        ConditionMap,
        MaterialTest,
        CleaningPhase,
        StabilityCheck,
        MinorRepair,
        StructuralReinforce,
        SurfaceRestore,
        CoatingApply,
        EthicsReview,
        ProvenanceVerify,
        ClientUpdate,
        FinalReport,
        ArchiveStore
    ]
)

# Define the order of activities
root.order.add_edge(InitialAssess, ArtifactScan)
root.order.add_edge(ArtifactScan, ConditionMap)
root.order.add_edge(ConditionMap, MaterialTest)
root.order.add_edge(MaterialTest, CleaningPhase)
root.order.add_edge(CleaningPhase, StabilityCheck)
root.order.add_edge(StabilityCheck, MinorRepair)
root.order.add_edge(MinorRepair, StructuralReinforce)
root.order.add_edge(StructuralReinforce, SurfaceRestore)
root.order.add_edge(SurfaceRestore, CoatingApply)
root.order.add_edge(CoatingApply, EthicsReview)
root.order.add_edge(EthicsReview, ProvenanceVerify)
root.order.add_edge(ProvenanceVerify, ClientUpdate)
root.order.add_edge(ClientUpdate, FinalReport)
root.order.add_edge(FinalReport, ArchiveStore)

# Print the final POWL model
print(root)