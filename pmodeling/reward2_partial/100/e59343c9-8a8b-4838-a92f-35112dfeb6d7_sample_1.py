from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the process
SiteSurvey = Transition(label='Site Survey')
PermitApproval = Transition(label='Permit Approval')
DesignLayout = Transition(label='Design Layout')
SystemProcure = Transition(label='System Procure')
NutrientPrep = Transition(label='Nutrient Prep')
StructureBuild = Transition(label='Structure Build')
SensorInstall = Transition(label='Sensor Install')
ClimateSetup = Transition(label='Climate Setup')
SeedSelect = Transition(label='Seed Select')
GerminateSeeds = Transition(label='Germinate Seeds')
MonitorGrowth = Transition(label='Monitor Growth')
DataAnalyze = Transition(label='Data Analyze')
PestControl = Transition(label='Pest Control')
HarvestCrop = Transition(label='Harvest Crop')
PackageGoods = Transition(label='Package Goods')
ShipProducts = Transition(label='Ship Products')

# Create the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    PermitApproval,
    DesignLayout,
    SystemProcure,
    NutrientPrep,
    StructureBuild,
    SensorInstall,
    ClimateSetup,
    SeedSelect,
    GerminateSeeds,
    MonitorGrowth,
    DataAnalyze,
    PestControl,
    HarvestCrop,
    PackageGoods,
    ShipProducts
])

# Define the order of execution
root.order.add_edge(SiteSurvey, PermitApproval)
root.order.add_edge(PermitApproval, DesignLayout)
root.order.add_edge(DesignLayout, SystemProcure)
root.order.add_edge(SystemProcure, NutrientPrep)
root.order.add_edge(NutrientPrep, StructureBuild)
root.order.add_edge(StructureBuild, SensorInstall)
root.order.add_edge(SensorInstall, ClimateSetup)
root.order.add_edge(ClimateSetup, SeedSelect)
root.order.add_edge(SeedSelect, GerminateSeeds)
root.order.add_edge(GerminateSeeds, MonitorGrowth)
root.order.add_edge(MonitorGrowth, DataAnalyze)
root.order.add_edge(DataAnalyze, PestControl)
root.order.add_edge(PestControl, HarvestCrop)
root.order.add_edge(HarvestCrop, PackageGoods)
root.order.add_edge(PackageGoods, ShipProducts)

print(root)