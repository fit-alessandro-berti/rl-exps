from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
SiteReview = Transition(label='Site Review')
ImpactStudy = Transition(label='Impact Study')
DesignPlan = Transition(label='Design Plan')
StructureMod = Transition(label='Structure Mod')
HydroponicsSetup = Transition(label='Hydroponics Setup')
CropSelect = Transition(label='Crop Select')
NutrientMix = Transition(label='Nutrient Mix')
PestControl = Transition(label='Pest Control')
SensorInstall = Transition(label='Sensor Install')
StaffTrain = Transition(label='Staff Train')
ComplianceAudit = Transition(label='Compliance Audit')
PackagingDev = Transition(label='Packaging Dev')
LogisticsPlan = Transition(label='Logistics Plan')
CommunityEngage = Transition(label='Community Engage')
SustainabilityCheck = Transition(label='Sustainability Check')

root = StrictPartialOrder(nodes=[
    SiteReview, ImpactStudy, DesignPlan, StructureMod, HydroponicsSetup, CropSelect,
    NutrientMix, PestControl, SensorInstall, StaffTrain, ComplianceAudit, PackagingDev,
    LogisticsPlan, CommunityEngage, SustainabilityCheck
])

# Define the dependencies
root.order.add_edge(SiteReview, ImpactStudy)
root.order.add_edge(ImpactStudy, DesignPlan)
root.order.add_edge(DesignPlan, StructureMod)
root.order.add_edge(StructureMod, HydroponicsSetup)
root.order.add_edge(HydroponicsSetup, CropSelect)
root.order.add_edge(CropSelect, NutrientMix)
root.order.add_edge(NutrientMix, PestControl)
root.order.add_edge(PestControl, SensorInstall)
root.order.add_edge(SensorInstall, StaffTrain)
root.order.add_edge(StaffTrain, ComplianceAudit)
root.order.add_edge(ComplianceAudit, PackagingDev)
root.order.add_edge(PackagingDev, LogisticsPlan)
root.order.add_edge(LogisticsPlan, CommunityEngage)
root.order.add_edge(CommunityEngage, SustainabilityCheck)

print(root)