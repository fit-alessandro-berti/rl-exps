import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SelectCrops = Transition(label='Select Crops')
InstallModules = Transition(label='Install Modules')
SetupSensors = Transition(label='Setup Sensors')
CalibrateClimate = Transition(label='Calibrate Climate')
ConfigureLighting = Transition(label='Configure Lighting')
IntegrateIoT = Transition(label='Integrate IoT')
TrainStaff = Transition(label='Train Staff')
RunTrials = Transition(label='Run Trials')
AnalyzeData = Transition(label='Analyze Data')
OptimizeYield = Transition(label='Optimize Yield')
CheckCompliance = Transition(label='Check Compliance')
PlanMarketing = Transition(label='Plan Marketing')
LaunchFacility = Transition(label='Launch Facility')

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, DesignLayout, SelectCrops, InstallModules, SetupSensors, CalibrateClimate, ConfigureLighting, IntegrateIoT, TrainStaff, RunTrials, AnalyzeData, OptimizeYield, CheckCompliance, PlanMarketing, LaunchFacility
])

# Define the order (dependencies) between the activities
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, SelectCrops)
root.order.add_edge(SelectCrops, InstallModules)
root.order.add_edge(InstallModules, SetupSensors)
root.order.add_edge(SetupSensors, CalibrateClimate)
root.order.add_edge(CalibrateClimate, ConfigureLighting)
root.order.add_edge(ConfigureLighting, IntegrateIoT)
root.order.add_edge(IntegrateIoT, TrainStaff)
root.order.add_edge(TrainStaff, RunTrials)
root.order.add_edge(RunTrials, AnalyzeData)
root.order.add_edge(AnalyzeData, OptimizeYield)
root.order.add_edge(OptimizeYield, CheckCompliance)
root.order.add_edge(CheckCompliance, PlanMarketing)
root.order.add_edge(PlanMarketing, LaunchFacility)

# Return the root of the POWL model
print(root)