import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[MilkSelection, QualityTesting, MilkPasteurize, CheeseCrafting, ControlledAging, SensoryReview, CustomPackaging, LabelPrinting])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ExportLicensing, DocumentationPrep, CustomsClearance, ColdShipping, DeliveryTracking, FeedbackReview, MarketAnalysis])

# Define the root node as a partial order
root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)

print(root)