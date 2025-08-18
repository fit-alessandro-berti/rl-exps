import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
ColonySourcing = Transition(label='Colony Sourcing')
HiveDesign = Transition(label='Hive Design')
SiteSurvey = Transition(label='Site Survey')
InstallationPrep = Transition(label='Installation Prep')
HiveSetup = Transition(label='Hive Setup')
SensorInstall = Transition(label='Sensor Install')
HealthMonitor = Transition(label='Health Monitor')
PestControl = Transition(label='Pest Control')
HoneyHarvest = Transition(label='Honey Harvest')
WaxProcessing = Transition(label='Wax Processing')
ProductPackaging = Transition(label='Product Packaging')
OrderDispatch = Transition(label='Order Dispatch')
WorkshopSetup = Transition(label='Workshop Setup')
CommunityOutreach = Transition(label='Community Outreach')
RegulationCheck = Transition(label='Regulation Check')
DataAnalysis = Transition(label='Data Analysis')
MaintenancePlan = Transition(label='Maintenance Plan')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    ColonySourcing,
    HiveDesign,
    SiteSurvey,
    InstallationPrep,
    HiveSetup,
    SensorInstall,
    HealthMonitor,
    PestControl,
    HoneyHarvest,
    WaxProcessing,
    ProductPackaging,
    OrderDispatch,
    WorkshopSetup,
    CommunityOutreach,
    RegulationCheck,
    DataAnalysis,
    MaintenancePlan
])

# Add dependencies between activities (POWL edges)
root.order.add_edge(ColonySourcing, HiveDesign)
root.order.add_edge(HiveDesign, SiteSurvey)
root.order.add_edge(SiteSurvey, InstallationPrep)
root.order.add_edge(InstallationPrep, HiveSetup)
root.order.add_edge(HiveSetup, SensorInstall)
root.order.add_edge(SensorInstall, HealthMonitor)
root.order.add_edge(HealthMonitor, PestControl)
root.order.add_edge(PestControl, HoneyHarvest)
root.order.add_edge(HoneyHarvest, WaxProcessing)
root.order.add_edge(WaxProcessing, ProductPackaging)
root.order.add_edge(ProductPackaging, OrderDispatch)
root.order.add_edge(OrderDispatch, WorkshopSetup)
root.order.add_edge(WorkshopSetup, CommunityOutreach)
root.order.add_edge(CommunityOutreach, RegulationCheck)
root.order.add_edge(RegulationCheck, DataAnalysis)
root.order.add_edge(DataAnalysis, MaintenancePlan)

# Print the POWL model
print(root)