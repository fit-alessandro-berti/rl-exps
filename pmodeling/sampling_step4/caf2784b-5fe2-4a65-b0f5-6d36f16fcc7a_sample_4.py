import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) based on the given names
Site_Audit = Transition(label='Site Audit')
Impact_Study = Transition(label='Impact Study')
Design_Modules = Transition(label='Design Modules')
Sensor_Setup = Transition(label='Sensor Setup')
Hydroponics_Install = Transition(label='Hydroponics Install')
Nutrient_Test = Transition(label='Nutrient Test')
Lighting_Config = Transition(label='Lighting Config')
Staff_Training = Transition(label='Staff Training')
Data_Collection = Transition(label='Data Collection')
Yield_Analysis = Transition(label='Yield Analysis')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Market_Delivery = Transition(label='Market Delivery')
Feedback_Loop = Transition(label='Feedback Loop')

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[Site_Audit, Impact_Study, Design_Modules, Sensor_Setup, Hydroponics_Install, Nutrient_Test, Lighting_Config, Staff_Training, Data_Collection, Yield_Analysis, Pest_Control, Harvest_Plan, Packaging_Prep, Market_Delivery, Feedback_Loop])
root.order.add_edge(Site_Audit, Impact_Study)
root.order.add_edge(Impact_Study, Design_Modules)
root.order.add_edge(Design_Modules, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Hydroponics_Install)
root.order.add_edge(Hydroponics_Install, Nutrient_Test)
root.order.add_edge(Nutrient_Test, Lighting_Config)
root.order.add_edge(Lighting_Config, Staff_Training)
root.order.add_edge(Staff_Training, Data_Collection)
root.order.add_edge(Data_Collection, Yield_Analysis)
root.order.add_edge(Yield_Analysis, Pest_Control)
root.order.add_edge(Pest_Control, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Market_Delivery)
root.order.add_edge(Market_Delivery, Feedback_Loop)