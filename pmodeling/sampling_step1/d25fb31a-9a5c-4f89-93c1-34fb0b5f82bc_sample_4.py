from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities as transitions
AssessStructure = Transition(label='Assess Structure')
AnalyzeEnvironment = Transition(label='Analyze Environment')
DesignModules = Transition(label='Design Modules')
ProcureMaterials = Transition(label='Procure Materials')
InstallIrrigation = Transition(label='Install Irrigation')
SetSensors = Transition(label='Set Sensors')
SelectSeeds = Transition(label='Select Seeds')
SchedulePlanting = Transition(label='Schedule Planting')
MonitorGrowth = Transition(label='Monitor Growth')
CollectData = Transition(label='Collect Data')
ManagePests = Transition(label='Manage Pests')
HarvestCrops = Transition(label='Harvest Crops')
CoordinateSales = Transition(label='Coordinate Sales')
CompostWaste = Transition(label='Compost Waste')
ReviewFeedback = Transition(label='Review Feedback')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    AssessStructure,
    AnalyzeEnvironment,
    DesignModules,
    ProcureMaterials,
    InstallIrrigation,
    SetSensors,
    SelectSeeds,
    SchedulePlanting,
    MonitorGrowth,
    CollectData,
    ManagePests,
    HarvestCrops,
    CoordinateSales,
    CompostWaste,
    ReviewFeedback
])

# Define the partial order relationships
root.order.add_edge(AssessStructure, AnalyzeEnvironment)
root.order.add_edge(AnalyzeEnvironment, DesignModules)
root.order.add_edge(DesignModules, ProcureMaterials)
root.order.add_edge(ProcureMaterials, InstallIrrigation)
root.order.add_edge(InstallIrrigation, SetSensors)
root.order.add_edge(SetSensors, SelectSeeds)
root.order.add_edge(SelectSeeds, SchedulePlanting)
root.order.add_edge(SchedulePlanting, MonitorGrowth)
root.order.add_edge(MonitorGrowth, CollectData)
root.order.add_edge(CollectData, ManagePests)
root.order.add_edge(ManagePests, HarvestCrops)
root.order.add_edge(HarvestCrops, CoordinateSales)
root.order.add_edge(CoordinateSales, CompostWaste)
root.order.add_edge(CompostWaste, ReviewFeedback)

print(root)