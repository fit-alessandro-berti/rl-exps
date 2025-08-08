import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
MilkSourcing = Transition(label='Milk Sourcing')
CulturePrep = Transition(label='Culture Prep')
MilkPasteurize = Transition(label='Milk Pasteurize')
Coagulation = Transition(label='Coagulation')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
HandMolding = Transition(label='Hand Molding')
Pressing = Transition(label='Pressing')
Salting = Transition(label='Salting')
RindTreatment = Transition(label='Rind Treatment')
AgingSetup = Transition(label='Aging Setup')
MicroclimateControl = Transition(label='Microclimate Control')
FlavorProfiling = Transition(label='Flavor Profiling')
QualityCheck = Transition(label='Quality Check')
SensoryReview = Transition(label='Sensory Review')
TextureInspect = Transition(label='Texture Inspect')
EcoPackaging = Transition(label='Eco Packaging')
BatchLabeling = Transition(label='Batch Labeling')
BlockchainLog = Transition(label='Blockchain Log')
NicheShipping = Transition(label='Niche Shipping')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    MilkSourcing,
    CulturePrep,
    MilkPasteurize,
    Coagulation,
    CurdCutting,
    WheyDraining,
    HandMolding,
    Pressing,
    Salting,
    RindTreatment,
    AgingSetup,
    MicroclimateControl,
    FlavorProfiling,
    QualityCheck,
    SensoryReview,
    TextureInspect,
    EcoPackaging,
    BatchLabeling,
    BlockchainLog,
    NicheShipping
])

# Define dependencies between activities
root.order.add_edge(MilkSourcing, CulturePrep)
root.order.add_edge(CulturePrep, MilkPasteurize)
root.order.add_edge(MilkPasteurize, Coagulation)
root.order.add_edge(Coagulation, CurdCutting)
root.order.add_edge(CurdCutting, WheyDraining)
root.order.add_edge(WheyDraining, HandMolding)
root.order.add_edge(HandMolding, Pressing)
root.order.add_edge(Pressing, Salting)
root.order.add_edge(Salting, RindTreatment)
root.order.add_edge(RindTreatment, AgingSetup)
root.order.add_edge(AgingSetup, MicroclimateControl)
root.order.add_edge(MicroclimateControl, FlavorProfiling)
root.order.add_edge(FlavorProfiling, QualityCheck)
root.order.add_edge(QualityCheck, SensoryReview)
root.order.add_edge(SensoryReview, TextureInspect)
root.order.add_edge(TextureInspect, EcoPackaging)
root.order.add_edge(EcoPackaging, BatchLabeling)
root.order.add_edge(BatchLabeling, BlockchainLog)
root.order.add_edge(BlockchainLog, NicheShipping)

# Print the root POWL model
print(root)