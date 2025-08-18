from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
StructuralCheck = Transition(label='Structural Check')
PermitApply = Transition(label='Permit Apply')
DesignLayout = Transition(label='Design Layout')
SoilPrep = Transition(label='Soil Prep')
BedInstall = Transition(label='Bed Install')
IrrigationSetup = Transition(label='Irrigation Setup')
SensorMount = Transition(label='Sensor Mount')
SolarConnect = Transition(label='Solar Connect')
SeedOrder = Transition(label='Seed Order')
NutrientMix = Transition(label='Nutrient Mix')
CommunityMeet = Transition(label='Community Meet')
StaffTrain = Transition(label='Staff Train')
PlantCrop = Transition(label='Plant Crop')
MaintenancePlan = Transition(label='Maintenance Plan')
HarvestSchedule = Transition(label='Harvest Schedule')
WasteManage = Transition(label='Waste Manage')

# Define the partial order
root = StrictPartialOrder(nodes=[StructuralCheck, PermitApply, DesignLayout, SoilPrep, BedInstall, IrrigationSetup, SensorMount, SolarConnect, SeedOrder, NutrientMix, CommunityMeet, StaffTrain, PlantCrop, MaintenancePlan, HarvestSchedule, WasteManage])

# Define the dependencies
root.order.add_edge(StructuralCheck, PermitApply)
root.order.add_edge(PermitApply, DesignLayout)
root.order.add_edge(DesignLayout, SoilPrep)
root.order.add_edge(SoilPrep, BedInstall)
root.order.add_edge(BedInstall, IrrigationSetup)
root.order.add_edge(IrrigationSetup, SensorMount)
root.order.add_edge(SensorMount, SolarConnect)
root.order.add_edge(SolarConnect, SeedOrder)
root.order.add_edge(SeedOrder, NutrientMix)
root.order.add_edge(NutrientMix, CommunityMeet)
root.order.add_edge(CommunityMeet, StaffTrain)
root.order.add_edge(StaffTrain, PlantCrop)
root.order.add_edge(PlantCrop, MaintenancePlan)
root.order.add_edge(MaintenancePlan, HarvestSchedule)
root.order.add_edge(HarvestSchedule, WasteManage)

print(root)