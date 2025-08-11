import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
MilkSelection = Transition(label='Milk Selection')
QualityTesting = Transition(label='Quality Testing')
MilkPasteurize = Transition(label='Milk Pasteurize')
CheeseCrafting = Transition(label='Cheese Crafting')
ControlledAging = Transition(label='Controlled Aging')
SensoryReview = Transition(label='Sensory Review')
CustomPackaging = Transition(label='Custom Packaging')
LabelPrinting = Transition(label='Label Printing')
ExportLicensing = Transition(label='Export Licensing')
DocumentationPrep = Transition(label='Documentation Prep')
CustomsClearance = Transition(label='Customs Clearance')
ColdShipping = Transition(label='Cold Shipping')
DeliveryTracking = Transition(label='Delivery Tracking')
FeedbackReview = Transition(label='Feedback Review')
MarketAnalysis = Transition(label='Market Analysis')

# Define the silent transitions
skip = SilentTransition()

# Define the loops and exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[MilkSelection, QualityTesting])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[MilkPasteurize, CheeseCrafting])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ControlledAging, SensoryReview])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[CustomPackaging, LabelPrinting])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[ExportLicensing, DocumentationPrep])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[CustomsClearance, ColdShipping])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[DeliveryTracking, FeedbackReview])

# Define the root node
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])

# Add the dependencies
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)

# Save the final result in the variable 'root'
root