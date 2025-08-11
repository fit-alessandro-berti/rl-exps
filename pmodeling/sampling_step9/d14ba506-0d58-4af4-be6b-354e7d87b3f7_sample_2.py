import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
SiteAnalysis = Transition(label='Site Analysis')
StructuralCheck = Transition(label='Structural Check')
RackInstall = Transition(label='Rack Install')
SystemSetup = Transition(label='System Setup')
HydroponicsConfig = Transition(label='Hydroponics Config')
AeroponicsTune = Transition(label='Aeroponics Tune')
LightingSetup = Transition(label='Lighting Setup')
EnviroControl = Transition(label='Enviro Control')
SensorDeploy = Transition(label='Sensor Deploy')
WasteRecycle = Transition(label='Waste Recycle')
WaterReuse = Transition(label='Water Reuse')
StaffTraining = Transition(label='Staff Training')
TestGrow = Transition(label='Test Grow')
DataAnalytics = Transition(label='Data Analytics')
YieldOptimize = Transition(label='Yield Optimize')

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define exclusive choice for SystemSetup
xor = OperatorPOWL(operator=Operator.XOR, children=[SystemSetup, skip])

# Define loop for TestGrow
loop = OperatorPOWL(operator=Operator.LOOP, children=[TestGrow])

# Define partial order
root = StrictPartialOrder(nodes=[SiteAnalysis, StructuralCheck, RackInstall, xor, HydroponicsConfig, AeroponicsTune, LightingSetup, EnviroControl, SensorDeploy, WasteRecycle, WaterReuse, StaffTraining, loop, DataAnalytics, YieldOptimize])

# Define dependencies
root.order.add_edge(SiteAnalysis, StructuralCheck)
root.order.add_edge(StructuralCheck, RackInstall)
root.order.add_edge(RackInstall, xor)
root.order.add_edge(xor, HydroponicsConfig)
root.order.add_edge(xor, AeroponicsTune)
root.order.add_edge(xor, LightingSetup)
root.order.add_edge(xor, EnviroControl)
root.order.add_edge(xor, SensorDeploy)
root.order.add_edge(xor, WasteRecycle)
root.order.add_edge(xor, WaterReuse)
root.order.add_edge(xor, StaffTraining)
root.order.add_edge(StaffTraining, loop)
root.order.add_edge(loop, DataAnalytics)
root.order.add_edge(DataAnalytics, YieldOptimize)

# Print the final result
print(root)