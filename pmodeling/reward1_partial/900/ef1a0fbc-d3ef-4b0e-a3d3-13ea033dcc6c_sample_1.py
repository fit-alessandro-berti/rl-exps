import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
MilkSourcing = Transition(label='Milk Sourcing')
FarmSelection = Transition(label='Farm Selection')
QualityTesting = Transition(label='Quality Testing')
MilkPasteurize = Transition(label='Milk Pasteurize')
StarterCulture = Transition(label='Starter Culture')
Coagulation = Transition(label='Coagulation')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
MoldInoculate = Transition(label='Mold Inoculate')
AgingControl = Transition(label='Aging Control')
FlavorTasting = Transition(label='Flavor Tasting')
PackagingDesign = Transition(label='Packaging Design')
LabelApproval = Transition(label='Label Approval')
InventoryAudit = Transition(label='Inventory Audit')
OrderFulfill = Transition(label='Order Fulfill')
RetailShipping = Transition(label='Retail Shipping')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    MilkSourcing,
    FarmSelection,
    QualityTesting,
    MilkPasteurize,
    StarterCulture,
    Coagulation,
    CurdCutting,
    WheyDraining,
    MoldInoculate,
    AgingControl,
    FlavorTasting,
    PackagingDesign,
    LabelApproval,
    InventoryAudit,
    OrderFulfill,
    RetailShipping
])

# Define the dependencies
root.order.add_edge(MilkSourcing, FarmSelection)
root.order.add_edge(FarmSelection, QualityTesting)
root.order.add_edge(QualityTesting, MilkPasteurize)
root.order.add_edge(MilkPasteurize, StarterCulture)
root.order.add_edge(StarterCulture, Coagulation)
root.order.add_edge(Coagulation, CurdCutting)
root.order.add_edge(CurdCutting, WheyDraining)
root.order.add_edge(WheyDraining, MoldInoculate)
root.order.add_edge(MoldInoculate, AgingControl)
root.order.add_edge(AgingControl, FlavorTasting)
root.order.add_edge(FlavorTasting, PackagingDesign)
root.order.add_edge(PackagingDesign, LabelApproval)
root.order.add_edge(LabelApproval, InventoryAudit)
root.order.add_edge(InventoryAudit, OrderFulfill)
root.order.add_edge(OrderFulfill, RetailShipping)

print(root)