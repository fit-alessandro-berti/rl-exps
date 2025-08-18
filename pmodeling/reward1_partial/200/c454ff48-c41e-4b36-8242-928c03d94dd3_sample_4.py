import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
Site_Assess = Transition(label='Site Assess')
Permit_Obtain = Transition(label='Permit Obtain')
Soil_Testing = Transition(label='Soil Testing')
Crop_Select = Transition(label='Crop Select')
Irrigation_Setup = Transition(label='Irrigation Setup')
Drainage_Install = Transition(label='Drainage Install')
Energy_Integrate = Transition(label='Energy Integrate')
Staff_Train = Transition(label='Staff Train')
Pest_Control = Transition(label='Pest Control')
Logistics_Plan = Transition(label='Logistics Plan')
Supply_Coordinate = Transition(label='Supply Coordinate')
Distribution_Map = Transition(label='Distribution Map')
Community_Engage = Transition(label='Community Engage')
Monitoring_Setup = Transition(label='Monitoring Setup')
Yield_Optimize = Transition(label='Yield Optimize')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Assess, Permit_Obtain])
xor = OperatorPOWL(operator=Operator.XOR, children=[Soil_Testing, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Select, Irrigation_Setup])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Drainage_Install, skip])
root.order.add_edge(xor, loop2)
root.order.add_edge(loop2, xor2)

loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Energy_Integrate, Staff_Train])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, skip])
root.order.add_edge(xor2, loop3)
root.order.add_edge(loop3, xor3)

loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Logistics_Plan, Supply_Coordinate])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Distribution_Map, skip])
root.order.add_edge(xor3, loop4)
root.order.add_edge(loop4, xor4)

loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Community_Engage, Monitoring_Setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Yield_Optimize, skip])
root.order.add_edge(xor4, loop5)
root.order.add_edge(loop5, xor5)