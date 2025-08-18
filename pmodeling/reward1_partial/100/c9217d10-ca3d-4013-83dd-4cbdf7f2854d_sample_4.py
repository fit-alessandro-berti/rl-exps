import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
SiteSurvey = Transition(label='Site Survey')
ClimateStudy = Transition(label='Climate Study')
DesignLayout = Transition(label='Design Layout')
SystemInstall = Transition(label='System Install')
CropSelect = Transition(label='Crop Select')
NutrientPlan = Transition(label='Nutrient Plan')
SensorSetup = Transition(label='Sensor Setup')
AutomationTest = Transition(label='Automation Test')
StaffTrain = Transition(label='Staff Train')
ComplianceCheck = Transition(label='Compliance Check')
MarketingSync = Transition(label='Marketing Sync')
DataMonitor = Transition(label='Data Monitor')
YieldAnalyze = Transition(label='Yield Analyze')
SupplyChain = Transition(label='Supply Chain')
CustomerEngage = Transition(label='Customer Engage')

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        SiteSurvey,
        ClimateStudy,
        DesignLayout,
        SystemInstall,
        CropSelect,
        NutrientPlan,
        SensorSetup,
        AutomationTest,
        StaffTrain,
        ComplianceCheck,
        MarketingSync,
        DataMonitor,
        YieldAnalyze,
        SupplyChain,
        CustomerEngage
    ]
)

# Define the dependencies between activities
root.order.add_edge(SiteSurvey, ClimateStudy)
root.order.add_edge(ClimateStudy, DesignLayout)
root.order.add_edge(DesignLayout, SystemInstall)
root.order.add_edge(SystemInstall, CropSelect)
root.order.add_edge(CropSelect, NutrientPlan)
root.order.add_edge(NutrientPlan, SensorSetup)
root.order.add_edge(SensorSetup, AutomationTest)
root.order.add_edge(AutomationTest, StaffTrain)
root.order.add_edge(StaffTrain, ComplianceCheck)
root.order.add_edge(ComplianceCheck, MarketingSync)
root.order.add_edge(MarketingSync, DataMonitor)
root.order.add_edge(DataMonitor, YieldAnalyze)
root.order.add_edge(YieldAnalyze, SupplyChain)
root.order.add_edge(SupplyChain, CustomerEngage)

# Print the root model
print(root)