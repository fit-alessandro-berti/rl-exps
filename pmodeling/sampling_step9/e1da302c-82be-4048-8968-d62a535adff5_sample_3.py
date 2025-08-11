import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[MaintenancePlan])
xor = OperatorPOWL(operator=Operator.XOR, children=[RegulationCheck, skip])
root = StrictPartialOrder(nodes=[ColonySourcing, HiveDesign, SiteSurvey, InstallationPrep, HiveSetup, SensorInstall, HealthMonitor, PestControl, HoneyHarvest, WaxProcessing, ProductPackaging, OrderDispatch, WorkshopSetup, CommunityOutreach, Regulatio