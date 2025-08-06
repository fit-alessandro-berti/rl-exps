import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
FarmSelection = Transition(label='Farm Selection')
MilkTesting = Transition(label='Milk Testing')
StarterCulture = Transition(label='Starter Culture')
CurdFormation = Transition(label='Curd Formation')
PressingCheese = Transition(label='Pressing Cheese')
MicrobialProfiling = Transition(label='Microbial Profiling')
AgingControl = Transition(label='Aging Control')
HandWrapping = Transition(label='Hand Wrapping')
QualityAudit = Transition(label='Quality Audit')
PackagingPrep = Transition(label='Packaging Prep')
ClimateShipping = Transition(label='Climate Shipping')
RetailCoordination = Transition(label='Retail Coordination')
SeasonalReview = Transition(label='Seasonal Review')
ConsumerSurvey = Transition(label='Consumer Survey')
FeedbackAnalysis = Transition(label='Feedback Analysis')
MarketAdjustment = Transition(label='Market Adjustment')

# Define the silent transition for skipping steps
skip = SilentTransition()

# Define the loops and exclusive choices
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[MicrobialProfiling, QualityAudit])
handwrapping_loop = OperatorPOWL(operator=Operator.LOOP, children=[PackagingPrep, ClimateShipping])
retail_loop = OperatorPOWL(operator=Operator.LOOP, children=[RetailCoordination, SeasonalReview])
consumer_loop = OperatorPOWL(operator=Operator.LOOP, children=[ConsumerSurvey, FeedbackAnalysis, MarketAdjustment])

# Define the exclusive choices
aging_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, skip])
handwrapping_xor = OperatorPOWL(operator=Operator.XOR, children=[handwrapping_loop, skip])
retail_xor = OperatorPOWL(operator=Operator.XOR, children=[retail_loop, skip])
consumer_xor = OperatorPOWL(operator=Operator.XOR, children=[consumer_loop, skip])

# Define the root process
root = StrictPartialOrder(nodes=[FarmSelection, MilkTesting, StarterCulture, CurdFormation, PressingCheese, aging_xor, handwrapping_xor, retail_xor, consumer_xor])
root.order.add_edge(FarmSelection, MilkTesting)
root.order.add_edge(MilkTesting, StarterCulture)
root.order.add_edge(StarterCulture, CurdFormation)
root.order.add_edge(CurdFormation, PressingCheese)
root.order.add_edge(PressingCheese, aging_xor)
root.order.add_edge(aging_xor, aging_loop)
root.order.add_edge(aging_loop, MicrobialProfiling)
root.order.add_edge(MicrobialProfiling, QualityAudit)
root.order.add_edge(QualityAudit, aging_loop)
root.order.add_edge(aging_loop, aging_xor)
root.order.add_edge(aging_xor, handwrapping_xor)
root.order.add_edge(handwrapping_xor, handwrapping_loop)
root.order.add_edge(handwrapping_loop, PackagingPrep)
root.order.add_edge(PackagingPrep, ClimateShipping)
root.order.add_edge(ClimateShipping, handwrapping_loop)
root.order.add_edge(handwrapping_loop, handwrapping_xor)
root.order.add_edge(handwrapping_xor, retail_xor)
root.order.add_edge(retail_xor, retail_loop)
root.order.add_edge(retail_loop, RetailCoordination)
root.order.add_edge(RetailCoordination, SeasonalReview)
root.order.add_edge(SeasonalReview, retail_loop)
root.order.add_edge(retail_loop, retail_xor)
root.order.add_edge(retail_xor, consumer_xor)
root.order.add_edge(consumer_xor, consumer_loop)
root.order.add_edge(consumer_loop, ConsumerSurvey)
root.order.add_edge(ConsumerSurvey, FeedbackAnalysis)
root.order.add_edge(FeedbackAnalysis, MarketAdjustment)
root.order.add_edge(MarketAdjustment, consumer_loop)
root.order.add_edge(consumer_loop, consumer_xor)