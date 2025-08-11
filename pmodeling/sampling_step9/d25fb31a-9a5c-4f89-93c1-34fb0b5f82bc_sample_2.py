import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[AssessStructure, AnalyzeEnvironment, DesignModules, ProcureMaterials, InstallIrrigation, SetSensors, SelectSeeds, SchedulePlanting, MonitorGrowth, CollectData, ManagePests, HarvestCrops, CoordinateSales, CompostWaste, ReviewFeedback])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, loop])
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop, xor)