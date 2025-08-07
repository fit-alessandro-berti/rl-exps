import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Colony_Sourcing = Transition(label='Colony Sourcing')
Hive_Design = Transition(label='Hive Design')
Site_Survey = Transition(label='Site Survey')
Installation_Prep = Transition(label='Installation Prep')
Hive_Setup = Transition(label='Hive Setup')
Sensor_Install = Transition(label='Sensor Install')
Health_Monitor = Transition(label='Health Monitor')
Pest_Control = Transition(label='Pest Control')
Honey_Harvest = Transition(label='Honey Harvest')
Wax_Processing = Transition(label='Wax Processing')
Product_Packaging = Transition(label='Product Packaging')
Order_Dispatch = Transition(label='Order Dispatch')
Workshop_Setup = Transition(label='Workshop Setup')
Community_Outreach = Transition(label='Community Outreach')
Regulation_Check = Transition(label='Regulation Check')
Data_Analysis = Transition(label='Data Analysis')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[Colony_Sourcing, Hive_Design, Site_Survey, Installation_Prep, Hive_Setup, Sensor_Install, Health_Monitor, Pest_Control, Honey_Harvest, Wax_Processing, Product_Packaging, Order_Dispatch, Workshop_Setup, Community_Outreach, Regulation_Check, Data_Analysis, Maintenance_Plan])

# Define dependencies
root.order.add_edge(Colony_Sourcing, Hive_Design)
root.order.add_edge(Hive_Design, Site_Survey)
root.order.add_edge(Site_Survey, Installation_Prep)
root.order.add_edge(Installation_Prep, Hive_Setup)
root.order.add_edge(Hive_Setup, Sensor_Install)
root.order.add_edge(Sensor_Install, Health_Monitor)
root.order.add_edge(Health_Monitor, Pest_Control)
root.order.add_edge(Pest_Control, Honey_Harvest)
root.order.add_edge(Honey_Harvest, Wax_Processing)
root.order.add_edge(Wax_Processing, Product_Packaging)
root.order.add_edge(Product_Packaging, Order_Dispatch)
root.order.add_edge(Order_Dispatch, Workshop_Setup)
root.order.add_edge(Workshop_Setup, Community_Outreach)
root.order.add_edge(Community_Outreach, Regulation_Check)
root.order.add_edge(Regulation_Check, Data_Analysis)
root.order.add_edge(Data_Analysis, Maintenance_Plan)

print(root)