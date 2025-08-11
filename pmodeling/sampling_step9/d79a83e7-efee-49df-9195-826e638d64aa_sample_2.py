import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, EnvAssessment, RegCompliance, ModularSetup, CropSelection, IoTIntegration, NutrientFlow, LightCalibration, StaffTraining, PestControl, MarketStrategy, LogisticsPlan, YieldAnalysis, DataReview, CommunityEngage])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)