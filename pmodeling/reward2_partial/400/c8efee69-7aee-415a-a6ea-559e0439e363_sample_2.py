import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
StarterPrep = Transition(label='Starter Prep')
CurdCutting = Transition(label='Curd Cutting')
MoldingCheese = Transition(label='Molding Cheese')
SaltingProcess = Transition(label='Salting Process')
AgingControl = Transition(label='Aging Control')
HumidityCheck = Transition(label='Humidity Check')
PackagingDesign = Transition(label='Packaging Design')
LabelPrinting = Transition(label='Label Printing')
InventoryAudit = Transition(label='Inventory Audit')
ColdStorage = Transition(label='Cold Storage')
OrderProcessing = Transition(label='Order Processing')
LogisticsPlanning = Transition(label='Logistics Planning')
RetailDelivery = Transition(label='Retail Delivery')
ConsumerFeedback = Transition(label='Consumer Feedback')
BatchAdjustment = Transition(label='Batch Adjustment')
EventCoordination = Transition(label='Event Coordination')

# Define the workflow
root = StrictPartialOrder(nodes=[
    MilkSourcing, QualityTesting, StarterPrep, CurdCutting, MoldingCheese, SaltingProcess, AgingControl, HumidityCheck,
    PackagingDesign, LabelPrinting, InventoryAudit, ColdStorage, OrderProcessing, LogisticsPlanning, RetailDelivery,
    ConsumerFeedback, BatchAdjustment, EventCoordination])

# Define the dependencies (partial order)
root.order.add_edge(MilkSourcing, QualityTesting)
root.order.add_edge(QualityTesting, StarterPrep)
root.order.add_edge(StarterPrep, CurdCutting)
root.order.add_edge(CurdCutting, MoldingCheese)
root.order.add_edge(MoldingCheese, SaltingProcess)
root.order.add_edge(SaltingProcess, AgingControl)
root.order.add_edge(AgingControl, HumidityCheck)
root.order.add_edge(HumidityCheck, PackagingDesign)
root.order.add_edge(PackagingDesign, LabelPrinting)
root.order.add_edge(LabelPrinting, InventoryAudit)
root.order.add_edge(InventoryAudit, ColdStorage)
root.order.add_edge(ColdStorage, OrderProcessing)
root.order.add_edge(OrderProcessing, LogisticsPlanning)
root.order.add_edge(LogisticsPlanning, RetailDelivery)
root.order.add_edge(RetailDelivery, ConsumerFeedback)
root.order.add_edge(ConsumerFeedback, BatchAdjustment)
root.order.add_edge(BatchAdjustment, EventCoordination)

# Note: The partial order defined here assumes a linear flow of activities. 
# In a real-world scenario, dependencies might be more complex and require additional transitions and edges.