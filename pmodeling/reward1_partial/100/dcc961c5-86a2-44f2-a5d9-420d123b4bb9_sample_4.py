import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Permit_Acquire = Transition(label='Permit Acquire')
Modular_Build = Transition(label='Modular Build')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Automation = Transition(label='Seed Automation')
Pest_Control = Transition(label='Pest Control')
Energy_Audit = Transition(label='Energy Audit')
Sensor_Install = Transition(label='Sensor Install')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Process = Transition(label='Waste Process')
Data_Analysis = Transition(label='Data Analysis')
Staff_Train = Transition(label='Staff Train')
Community_Link = Transition(label='Community Link')
Yield_Report = Transition(label='Yield Report')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define the workflow model
loop_Survey = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Permit_Acquire])
loop_Layout = OperatorPOWL(operator=Operator.LOOP, children=[Design_Layout, Modular_Build])
loop_Climate = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Setup, Nutrient_Mix])
loop_Seed = OperatorPOWL(operator=Operator.LOOP, children=[Seed_Automation, Pest_Control])
loop_Energy = OperatorPOWL(operator=Operator.LOOP, children=[Energy_Audit, Sensor_Install])
loop_Growth = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, Waste_Process])
loop_Data = OperatorPOWL(operator=Operator.LOOP, children=[Data_Analysis, Staff_Train])
loop_Community = OperatorPOWL(operator=Operator.LOOP, children=[Community_Link, Yield_Report])

xor_Survey = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_Survey])
xor_Layout = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_Layout])
xor_Climate = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_Climate])
xor_Seed = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_Seed])
xor_Energy = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_Energy])
xor_Growth = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_Growth])
xor_Data = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_Data])
xor_Community = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_Community])

root = StrictPartialOrder(nodes=[xor_Survey, xor_Layout, xor_Climate, xor_Seed, xor_Energy, xor_Growth, xor_Data, xor_Community])

# Add edges to represent the partial order relationship
root.order.add_edge(xor_Survey, xor_Layout)
root.order.add_edge(xor_Layout, xor_Climate)
root.order.add_edge(xor_Climate, xor_Seed)
root.order.add_edge(xor_Seed, xor_Energy)
root.order.add_edge(xor_Energy, xor_Growth)
root.order.add_edge(xor_Growth, xor_Data)
root.order.add_edge(xor_Data, xor_Community)

print(root)