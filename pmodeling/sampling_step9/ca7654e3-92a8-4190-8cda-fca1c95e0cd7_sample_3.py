import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
MilkSourcing = Transition(label='Milk Sourcing')
CurdPreparation = Transition(label='Curd Preparation')
StarterCulture = Transition(label='starter Culture')
TemperatureControl = Transition(label='Temperature Control')
PressingCheese = Transition(label='Pressing Cheese')
SaltingStage = Transition(label='Salting Stage')
AgingProcess = Transition(label='Aging Process')
MicrobialTest = Transition(label='Microbial Test')
QualityCheck = Transition(label='Quality Check')
EcoPackaging = Transition(label='Eco Packaging')
LabelPrinting = Transition(label='Label Printing')
InventoryAudit = Transition(label='Inventory Audit')
OrderProcessing = Transition(label='Order Processing')
RetailShipping = Transition(label='Retail Shipping')
CustomerFeedback = Transition(label='Customer Feedback')
RecipeUpdate = Transition(label='Recipe Update')
MarketAnalysis = Transition(label='Market Analysis')

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, StarterCulture, TemperatureControl])
loop_curd_preparation = OperatorPOWL(operator=Operator.LOOP, children=[CurdPreparation, PressingCheese, SaltingStage])
loop_aging_process = OperatorPOWL(operator=Operator.LOOP, children=[AgingProcess, MicrobialTest, QualityCheck])
loop_eco_packaging = OperatorPOWL(operator=Operator.LOOP, children=[EcoPackaging, LabelPrinting])
loop_inventory_audit = OperatorPOWL(operator=Operator.LOOP, children=[InventoryAudit, OrderProcessing, RetailShipping])
loop_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[CustomerFeedback, RecipeUpdate, MarketAnalysis])

xor_milk_sourcing = OperatorPOWL(operator=Operator.XOR, children=[loop_milk_sourcing, skip])
xor_curd_preparation = OperatorPOWL(operator=Operator.XOR, children=[loop_curd_preparation, skip])
xor_aging_process = OperatorPOWL(operator=Operator.XOR, children=[loop_aging_process, skip])
xor_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[loop_eco_packaging, skip])
xor_inventory_audit = OperatorPOWL(operator=Operator.XOR, children=[loop_inventory_audit, skip])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[loop_customer_feedback, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor_milk_sourcing, xor_curd_preparation, xor_aging_process, xor_eco_packaging, xor_inventory_audit, xor_customer_feedback])
root.order.add_edge(xor_milk_sourcing, xor_curd_preparation)
root.order.add_edge(xor_curd_preparation, xor_aging_process)
root.order.add_edge(xor_aging_process, xor_eco_packaging)
root.order.add_edge(xor_eco_packaging, xor_inventory_audit)
root.order.add_edge(xor_inventory_audit, xor_customer_feedback)