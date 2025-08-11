import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteAudit = Transition(label='Site Audit')
ImpactStudy = Transition(label='Impact Study')
DesignModules = Transition(label='Design Modules')
SensorSetup = Transition(label='Sensor Setup')
HydroponicsInstall = Transition(label='Hydroponics Install')
NutrientTest = Transition(label='Nutrient Test')
LightingConfig = Transition(label='Lighting Config')
StaffTraining = Transition(label='Staff Training')
DataCollection = Transition(label='Data Collection')
YieldAnalysis = Transition(label='Yield Analysis')
PestControl = Transition(label='Pest Control')
HarvestPlan = Transition(label='Harvest Plan')
PackagingPrep = Transition(label='Packaging Prep')
MarketDelivery = Transition(label='Market Delivery')
FeedbackLoop = Transition(label='Feedback Loop')

# Define silent activities
Skip = SilentTransition()

# Define the loop node for feedback loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop])

# Define the exclusive choice for sensor setup
xor = OperatorPOWL(operator=Operator.XOR, children=[SensorSetup, Skip])

# Define the exclusive choice for hydroponics installation
xor2 = OperatorPOWL(operator=Operator.XOR, children=[HydroponicsInstall, Skip])

# Define the exclusive choice for lighting configuration
xor3 = OperatorPOWL(operator=Operator.XOR, children=[LightingConfig, Skip])

# Define the exclusive choice for staff training
xor4 = OperatorPOWL(operator=Operator.XOR, children=[StaffTraining, Skip])

# Define the exclusive choice for yield analysis
xor5 = OperatorPOWL(operator=Operator.XOR, children=[YieldAnalysis, Skip])

# Define the exclusive choice for pest control
xor6 = OperatorPOWL(operator=Operator.XOR, children=[PestControl, Skip])

# Define the exclusive choice for harvest plan
xor7 = OperatorPOWL(operator=Operator.XOR, children=[HarvestPlan, Skip])

# Define the exclusive choice for packaging preparation
xor8 = OperatorPOWL(operator=Operator.XOR, children=[PackagingPrep, Skip])

# Define the exclusive choice for market delivery
xor9 = OperatorPOWL(operator=Operator.XOR, children=[MarketDelivery, Skip])

# Define the exclusive choice for feedback loop
xor10 = OperatorPOWL(operator=Operator.XOR, children=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor10])
root.order.add_edge(xor10, loop)
root.order.add_edge(xor10, xor)
root.order.add_edge(xor10, xor2)
root.order.add_edge(xor10, xor3)
root.order.add_edge(xor10, xor4)
root.order.add_edge(xor10, xor5)
root.order.add_edge(xor10, xor6)
root.order.add_edge(xor10, xor7)
root.order.add_edge(xor10, xor8)
root.order.add_edge(xor10, xor9)