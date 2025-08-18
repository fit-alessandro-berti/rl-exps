import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
System_Assembly = Transition(label='System Assembly')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Prep = Transition(label='Nutrient Prep')
Water_Testing = Transition(label='Water Testing')
Climate_Setup = Transition(label='Climate Setup')
Data_Integration = Transition(label='Data Integration')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Control = Transition(label='Pest Control')
Waste_Sorting = Transition(label='Waste Sorting')
Harvest_Plan = Transition(label='Harvest Plan')
Produce_Pack = Transition(label='Produce Pack')
Energy_Audit = Transition(label='Energy Audit')
Community_Setup = Transition(label='Community Setup')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model components
loop_Sensor_Install = OperatorPOWL(operator=Operator.LOOP, children=[Sensor_Install, skip])
xor_Waste_Sorting = OperatorPOWL(operator=Operator.XOR, children=[Waste_Sorting, skip])
xor_Pest_Control = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, skip])
xor_Harvest_Plan = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Material_Sourcing, System_Assembly, Sensor_Install, Nutrient_Prep, Water_Testing, Climate_Setup, Data_Integration, Growth_Monitoring, loop_Sensor_Install, xor_Waste_Sorting, xor_Pest_Control, xor_Harvest_Plan, Produce_Pack, Energy_Audit, Community_Setup])
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Material_Sourcing)
root.order.add_edge(Material_Sourcing, System_Assembly)
root.order.add_edge(System_Assembly, Sensor_Install)
root.order.add_edge(Sensor_Install, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Water_Testing)
root.order.add_edge(Water_Testing, Climate_Setup)
root.order.add_edge(Climate_Setup, Data_Integration)
root.order.add_edge(Data_Integration, Growth_Monitoring)
root.order.add_edge(Growth_Monitoring, loop_Sensor_Install)
root.order.add_edge(loop_Sensor_Install, xor_Waste_Sorting)
root.order.add_edge(xor_Waste_Sorting, xor_Pest_Control)
root.order.add_edge(xor_Pest_Control, xor_Harvest_Plan)
root.order.add_edge(xor_Harvest_Plan, Produce_Pack)
root.order.add_edge(Produce_Pack, Energy_Audit)
root.order.add_edge(Energy_Audit, Community_Setup)