import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    FarmSelection,
    MilkTesting,
    StarterCulture,
    CurdFormation,
    PressingCheese,
    MicrobialProfiling,
    AgingControl,
    HandWrapping,
    QualityAudit,
    PackagingPrep,
    ClimateShipping,
    RetailCoordination,
    SeasonalReview,
    ConsumerSurvey,
    FeedbackAnalysis,
    MarketAdjustment
])

# Define the dependencies between activities
root.order.add_edge(FarmSelection, MilkTesting)
root.order.add_edge(MilkTesting, StarterCulture)
root.order.add_edge(StarterCulture, CurdFormation)
root.order.add_edge(CurdFormation, PressingCheese)
root.order.add_edge(PressingCheese, MicrobialProfiling)
root.order.add_edge(MicrobialProfiling, AgingControl)
root.order.add_edge(AgingControl, HandWrapping)
root.order.add_edge(HandWrapping, QualityAudit)
root.order.add_edge(QualityAudit, PackagingPrep)
root.order.add_edge(PackagingPrep, ClimateShipping)
root.order.add_edge(ClimateShipping, RetailCoordination)
root.order.add_edge(RetailCoordination, SeasonalReview)
root.order.add_edge(SeasonalReview, ConsumerSurvey)
root.order.add_edge(ConsumerSurvey, FeedbackAnalysis)
root.order.add_edge(FeedbackAnalysis, MarketAdjustment)

# Print the final POWL model
print(root)