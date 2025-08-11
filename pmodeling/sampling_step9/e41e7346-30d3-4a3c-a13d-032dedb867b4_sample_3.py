import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Light_Adjust = Transition(label='Light Adjust')
CO2_Control = Transition(label='CO2 Control')
Humidity_Tune = Transition(label='Humidity Tune')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Detect = Transition(label='Pest Detect')
Harvest_Plan = Transition(label='Harvest Plan')
Produce_Sort = Transition(label='Produce Sort')
Pack_Biodeg = Transition(label='Pack Biodeg')
Drone_Dispatch = Transition(label='Drone Dispatch')
Waste_Recycle = Transition(label='Waste Recycle')
Compost_Create = Transition(label='Compost Create')
Cycle_Review = Transition(label='Cycle Review')
skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Setup, Light_Adjust, CO2_Control, Humidity_Tune])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, Pest_Detect, Harvest_Plan])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Produce_Sort, Pack_Biodeg, Drone_Dispatch])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Recycle, Compost_Create, Cycle_Review])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)