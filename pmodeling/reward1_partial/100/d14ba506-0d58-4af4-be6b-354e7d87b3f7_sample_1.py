import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
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

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
        SiteAnalysis,
        StructuralCheck,
        RackInstall,
        SystemSetup,
        HydroponicsConfig,
        AeroponicsTune,
        LightingSetup,
        EnviroControl,
        SensorDeploy,
        WasteRecycle,
        WaterReuse,
        StaffTraining,
        TestGrow,
        DataAnalytics,
        YieldOptimize
    ]
)

# Define the control flow between activities
root.order.add_edge(SiteAnalysis, StructuralCheck)
root.order.add_edge(StructuralCheck, RackInstall)
root.order.add_edge(RackInstall, SystemSetup)
root.order.add_edge(SystemSetup, HydroponicsConfig)
root.order.add_edge(HydroponicsConfig, AeroponicsTune)
root.order.add_edge(AeroponicsTune, LightingSetup)
root.order.add_edge(LightingSetup, EnviroControl)
root.order.add_edge(EnviroControl, SensorDeploy)
root.order.add_edge(SensorDeploy, WasteRecycle)
root.order.add_edge(WasteRecycle, WaterReuse)
root.order.add_edge(WaterReuse, StaffTraining)
root.order.add_edge(StaffTraining, TestGrow)
root.order.add_edge(TestGrow, DataAnalytics)
root.order.add_edge(DataAnalytics, YieldOptimize)

# Print the final POWL model
print(root)