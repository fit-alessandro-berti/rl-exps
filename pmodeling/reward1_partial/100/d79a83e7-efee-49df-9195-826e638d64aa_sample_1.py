import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
SiteSurvey = Transition(label='Site Survey')
EnvAssessment = Transition(label='Env Assessment')
RegCompliance = Transition(label='Reg Compliance')
ModularSetup = Transition(label='Modular Setup')
CropSelection = Transition(label='Crop Selection')
IoTIntegration = Transition(label='IoT Integration')
NutrientFlow = Transition(label='Nutrient Flow')
LightCalibration = Transition(label='Light Calibration')
StaffTraining = Transition(label='Staff Training')
PestControl = Transition(label='Pest Control')
MarketStrategy = Transition(label='Market Strategy')
LogisticsPlan = Transition(label='Logistics Plan')
YieldAnalysis = Transition(label='Yield Analysis')
DataReview = Transition(label='Data Review')
CommunityEngage = Transition(label='Community Engage')

# Define the loop node for continuous yield optimization and data review
loop = OperatorPOWL(operator=Operator.LOOP, children=[YieldAnalysis, DataReview])

# Define the partial order with concurrent activities
partial_order = StrictPartialOrder(nodes=[SiteSurvey, EnvAssessment, RegCompliance, ModularSetup, CropSelection, IoTIntegration, NutrientFlow, LightCalibration, StaffTraining, PestControl, MarketStrategy, LogisticsPlan, loop, CommunityEngage])

# Define the dependencies between activities
partial_order.order.add_edge(SiteSurvey, EnvAssessment)
partial_order.order.add_edge(EnvAssessment, RegCompliance)
partial_order.order.add_edge(RegCompliance, ModularSetup)
partial_order.order.add_edge(ModularSetup, CropSelection)
partial_order.order.add_edge(CropSelection, IoTIntegration)
partial_order.order.add_edge(IoTIntegration, NutrientFlow)
partial_order.order.add_edge(NutrientFlow, LightCalibration)
partial_order.order.add_edge(LightCalibration, StaffTraining)
partial_order.order.add_edge(StaffTraining, PestControl)
partial_order.order.add_edge(PestControl, MarketStrategy)
partial_order.order.add_edge(MarketStrategy, LogisticsPlan)
partial_order.order.add_edge(LogisticsPlan, YieldAnalysis)
partial_order.order.add_edge(YieldAnalysis, DataReview)
partial_order.order.add_edge(DataReview, CommunityEngage)
partial_order.order.add_edge(CommunityEngage, SiteSurvey)

# Set 'root' to the generated partial order
root = partial_order