import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SeedSelect = Transition(label='Seed Select')
NutrientMix = Transition(label='Nutrient Mix')
ClimateSetup = Transition(label='Climate Setup')
LightAdjust = Transition(label='Light Adjust')
CO2Control = Transition(label='CO2 Control')
HumidityTune = Transition(label='Humidity Tune')
GrowthMonitor = Transition(label='Growth Monitor')
PestDetect = Transition(label='Pest Detect')
HarvestPlan = Transition(label='Harvest Plan')
ProduceSort = Transition(label='Produce Sort')
PackBiodeg = Transition(label='Pack Biodeg')
DroneDispatch = Transition(label='Drone Dispatch')
WasteRecycle = Transition(label='Waste Recycle')
CompostCreate = Transition(label='Compost Create')
CycleReview = Transition(label='Cycle Review')
skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[ClimateSetup, LightAdjust, CO2Control, HumidityTune, GrowthMonitor, PestDetect, HarvestPlan, ProduceSort, PackBiodeg, DroneDispatch, WasteRecycle, CompostCreate])
xor = OperatorPOWL(operator=Operator.XOR, children=[CycleReview, skip])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# The POWL model for the integrated management of an urban vertical farm is defined in the 'root' variable.