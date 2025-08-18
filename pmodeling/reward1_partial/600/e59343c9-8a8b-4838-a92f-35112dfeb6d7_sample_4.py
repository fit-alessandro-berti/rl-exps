import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Survey = Transition(label='Site Survey')
Permit_Approval = Transition(label='Permit Approval')
Design_Layout = Transition(label='Design Layout')
System_Procure = Transition(label='System Procure')
Nutrient_Prep = Transition(label='Nutrient Prep')
Structure_Build = Transition(label='Structure Build')
Sensor_Install = Transition(label='Sensor Install')
Climate_Setup = Transition(label='Climate Setup')
Seed_Select = Transition(label='Seed Select')
Germinate_Seeds = Transition(label='Germinate Seeds')
Monitor_Growth = Transition(label='Monitor Growth')
Data_Analyze = Transition(label='Data Analyze')
Pest_Control = Transition(label='Pest Control')
Harvest_Crop = Transition(label='Harvest Crop')
Package_Goods = Transition(label='Package Goods')
Ship_Products = Transition(label='Ship Products')

# Define the process model
root = StrictPartialOrder(nodes=[Site_Survey, Permit_Approval, Design_Layout, System_Procure, Nutrient_Prep, Structure_Build, Sensor_Install, Climate_Setup, Seed_Select, Germinate_Seeds, Monitor_Growth, Data_Analyze, Pest_Control, Harvest_Crop, Package_Goods, Ship_Products])
root.order.add_edge(Site_Survey, Permit_Approval)
root.order.add_edge(Permit_Approval, Design_Layout)
root.order.add_edge(Design_Layout, System_Procure)
root.order.add_edge(System_Procure, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Structure_Build)
root.order.add_edge(Structure_Build, Sensor_Install)
root.order.add_edge(Sensor_Install, Climate_Setup)
root.order.add_edge(Climate_Setup, Seed_Select)
root.order.add_edge(Seed_Select, Germinate_Seeds)
root.order.add_edge(Germinate_Seeds, Monitor_Growth)
root.order.add_edge(Monitor_Growth, Data_Analyze)
root.order.add_edge(Data_Analyze, Pest_Control)
root.order.add_edge(Pest_Control, Harvest_Crop)
root.order.add_edge(Harvest_Crop, Package_Goods)
root.order.add_edge(Package_Goods, Ship_Products)

print(root)