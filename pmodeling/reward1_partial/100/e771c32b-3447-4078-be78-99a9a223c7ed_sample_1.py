import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSurvey = Transition(label='Site Survey')
ClimatePlan = Transition(label='Climate Plan')
SystemDesign = Transition(label='System Design')
AISetup = Transition(label='AI Setup')
SeedSourcing = Transition(label='Seed Sourcing')
NutrientMix = Transition(label='Nutrient Mix')
InstallHydro = Transition(label='Install Hydro')
EnergyAudit = Transition(label='Energy Audit')
StaffTraining = Transition(label='Staff Training')
TrialGrowth = Transition(label='Trial Growth')
YieldMeasure = Transition(label='Yield Measure')
WasteCycle = Transition(label='Waste Cycle')
ComplianceCheck = Transition(label='Compliance Check')
MarketStudy = Transition(label='Market Study')
CommunityMeet = Transition(label='Community Meet')
OptimizeEnvironment = Transition(label='Optimize Environment')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define partial order and exclusive choice operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAudit, StaffTraining])
xor = OperatorPOWL(operator=Operator.XOR, children=[ComplianceCheck, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[TrialGrowth, YieldMeasure])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[MarketStudy, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[CommunityMeet, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[WasteCycle, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[OptimizeEnvironment, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[SiteSurvey, ClimatePlan, SystemDesign, AISetup, SeedSourcing, NutrientMix, InstallHydro, loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(SiteSurvey, ClimatePlan)
root.order.add_edge(ClimatePlan, SystemDesign)
root.order.add_edge(SystemDesign, AISetup)
root.order.add_edge(AISetup, SeedSourcing)
root.order.add_edge(SeedSourcing, NutrientMix)
root.order.add_edge(NutrientMix, InstallHydro)
root.order.add_edge(InstallHydro, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, OptimizeEnvironment)