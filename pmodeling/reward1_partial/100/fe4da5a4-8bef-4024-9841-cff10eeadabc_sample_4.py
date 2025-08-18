import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Permit_Securing = Transition(label='Permit Securing')
Structure_Check = Transition(label='Structure Check')
Soil_Testing = Transition(label='Soil Testing')
Water_Analysis = Transition(label='Water Analysis')
Material_Sourcing = Transition(label='Material Sourcing')
Planter_Setup = Transition(label='Planter Setup')
Sensor_Install = Transition(label='Sensor Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Vendor_Liaison = Transition(label='Vendor Liaison')
Staff_Training = Transition(label='Staff Training')
Pest_Control = Transition(label='Pest Control')
Produce_Marketing = Transition(label='Produce Marketing')
Crop_Rotation = Transition(label='Crop Rotation')
Health_Audit = Transition(label='Health Audit')
Waste_Composting = Transition(label='Waste Composting')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Permit_Securing, Structure_Check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Soil_Testing, Water_Analysis])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Material_Sourcing, Planter_Setup])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Sensor_Install, Irrigation_Setup])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Vendor_Liaison, Staff_Training])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Control, Produce_Marketing])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Rotation, Health_Audit])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Composting])

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop4])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop5])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop6])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop7])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop8])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)
root.order.add_edge(xor5, loop5)
root.order.add_edge(xor6, loop6)
root.order.add_edge(xor7, loop7)
root.order.add_edge(xor8, loop8)