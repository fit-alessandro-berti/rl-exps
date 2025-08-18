import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
SiteAnalysis = Transition(label='Site Analysis')
SensorSetup = Transition(label='Sensor Setup')
DataCapture = Transition(label='Data Capture')
AIPrediction = Transition(label='AI Prediction')
CommunityPoll = Transition(label='Community Poll')
IrrigationAdjust = Transition(label='Irrigation Adjust')
NutrientMix = Transition(label='Nutrient Mix')
PestControl = Transition(label='Pest Control')
SoilTesting = Transition(label='Soil Testing')
BiocharApply = Transition(label='Biochar Apply')
MicrobialAdd = Transition(label='Microbial Add')
AutomatedHarvest = Transition(label='Automated Harvest')
YieldReview = Transition(label='Yield Review')
WasteProcess = Transition(label='Waste Process')
FeedbackLoop = Transition(label='Feedback Loop')

# Create the StrictPartialOrder model
root = StrictPartialOrder(nodes=[SiteAnalysis, SensorSetup, DataCapture, AIPrediction, CommunityPoll, IrrigationAdjust, NutrientMix, PestControl, SoilTesting, BiocharApply, MicrobialAdd, AutomatedHarvest, YieldReview, WasteProcess, FeedbackLoop])

# Define the partial order dependencies
root.order.add_edge(SiteAnalysis, SensorSetup)
root.order.add_edge(SensorSetup, DataCapture)
root.order.add_edge(DataCapture, AIPrediction)
root.order.add_edge(AIPrediction, CommunityPoll)
root.order.add_edge(CommunityPoll, IrrigationAdjust)
root.order.add_edge(IrrigationAdjust, NutrientMix)
root.order.add_edge(NutrientMix, PestControl)
root.order.add_edge(PestControl, SoilTesting)
root.order.add_edge(SoilTesting, BiocharApply)
root.order.add_edge(BiocharApply, MicrobialAdd)
root.order.add_edge(MicrobialAdd, AutomatedHarvest)
root.order.add_edge(AutomatedHarvest, YieldReview)
root.order.add_edge(YieldReview, WasteProcess)
root.order.add_edge(WasteProcess, FeedbackLoop)

# Print the root POWL model
print(root)