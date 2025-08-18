import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
SiteSurvey = Transition(label='Site Survey')
PermitReview = Transition(label='Permit Review')
DesignLayout = Transition(label='Design Layout')
MaterialSourcing = Transition(label='Material Sourcing')
IrrigationSetup = Transition(label='Irrigation Setup')
SensorInstall = Transition(label='Sensor Install')
StructuralTest = Transition(label='Structural Test')
RecruitFarmers = Transition(label='Recruit Farmers')
TrialPlanting = Transition(label='Trial Planting')
PestControl = Transition(label='Pest Control')
SoillessPrep = Transition(label='Soilless Prep')
SystemCalibrate = Transition(label='System Calibrate')
DataMonitor = Transition(label='Data Monitor')
HarvestPlan = Transition(label='Harvest Plan')
CommunityOutreach = Transition(label='Community Outreach')

# Create the root Partial Order
root = StrictPartialOrder(nodes=[SiteSurvey, PermitReview, DesignLayout, MaterialSourcing, IrrigationSetup, SensorInstall, StructuralTest, RecruitFarmers, TrialPlanting, PestControl, SoillessPrep, SystemCalibrate, DataMonitor, HarvestPlan, CommunityOutreach])

# Define the order relationships
root.order.add_edge(SiteSurvey, PermitReview)
root.order.add_edge(PermitReview, DesignLayout)
root.order.add_edge(DesignLayout, MaterialSourcing)
root.order.add_edge(MaterialSourcing, IrrigationSetup)
root.order.add_edge(IrrigationSetup, SensorInstall)
root.order.add_edge(SensorInstall, StructuralTest)
root.order.add_edge(StructuralTest, RecruitFarmers)
root.order.add_edge(RecruitFarmers, TrialPlanting)
root.order.add_edge(TrialPlanting, PestControl)
root.order.add_edge(PestControl, SoillessPrep)
root.order.add_edge(SoillessPrep, SystemCalibrate)
root.order.add_edge(SystemCalibrate, DataMonitor)
root.order.add_edge(DataMonitor, HarvestPlan)
root.order.add_edge(HarvestPlan, CommunityOutreach)

print(root)