import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
Irrigation_Setup = Transition(label='Irrigation Setup')
Sensor_Install = Transition(label='Sensor Install')
Structural_Test = Transition(label='Structural Test')
Recruit_Farmers = Transition(label='Recruit Farmers')
Trial_Planting = Transition(label='Trial Planting')
Pest_Control = Transition(label='Pest Control')
Soilless_Prep = Transition(label='Soilless Prep')
System_Calibrate = Transition(label='System Calibrate')
Data_Monitor = Transition(label='Data Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Community_Outreach = Transition(label='Community Outreach')

# Define the partial order
root = StrictPartialOrder(nodes=[Site_Survey, Permit_Review, Design_Layout, Material_Sourcing, Irrigation_Setup, Sensor_Install, Structural_Test, Recruit_Farmers, Trial_Planting, Pest_Control, Soilless_Prep, System_Calibrate, Data_Monitor, Harvest_Plan, Community_Outreach])

# Define the dependencies (order)
root.order.add_edge(Site_Survey, Permit_Review)
root.order.add_edge(Permit_Review, Design_Layout)
root.order.add_edge(Design_Layout, Material_Sourcing)
root.order.add_edge(Material_Sourcing, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Sensor_Install)
root.order.add_edge(Sensor_Install, Structural_Test)
root.order.add_edge(Structural_Test, Recruit_Farmers)
root.order.add_edge(Recruit_Farmers, Trial_Planting)
root.order.add_edge(Trial_Planting, Pest_Control)
root.order.add_edge(Pest_Control, Soilless_Prep)
root.order.add_edge(Soilless_Prep, System_Calibrate)
root.order.add_edge(System_Calibrate, Data_Monitor)
root.order.add_edge(Data_Monitor, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Community_Outreach)