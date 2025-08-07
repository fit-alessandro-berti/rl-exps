import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Survey = Transition(label='Site Survey')
Design_Modules = Transition(label='Design Modules')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
LED_Tuning = Transition(label='LED Tuning')
Seed_Automation = Transition(label='Seed Automation')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Audit = Transition(label='Energy Audit')
Waste_System = Transition(label='Waste System')
Community_Meet = Transition(label='Community Meet')
Compliance_Check = Transition(label='Compliance Check')
Crop_Packing = Transition(label='Crop Packing')
Logistics_Plan = Transition(label='Logistics Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[Site_Survey, Design_Modules, Climate_Setup, Nutrient_Mix, LED_Tuning, Seed_Automation, Growth_Monitor, Pest_Control, Yield_Forecast, Energy_Audit, Waste_System, Community_Meet, Compliance_Check, Crop_Packing, Logistics_Plan])

# Define the edges in the partial order
root.order.add_edge(Site_Survey, Design_Modules)
root.order.add_edge(Site_Survey, Climate_Setup)
root.order.add_edge(Design_Modules, Nutrient_Mix)
root.order.add_edge(Design_Modules, LED_Tuning)
root.order.add_edge(Climate_Setup, Seed_Automation)
root.order.add_edge(Seed_Automation, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Pest_Control)
root.order.add_edge(Pest_Control, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Energy_Audit)
root.order.add_edge(Energy_Audit, Waste_System)
root.order.add_edge(Waste_System, Community_Meet)
root.order.add_edge(Community_Meet, Compliance_Check)
root.order.add_edge(Compliance_Check, Crop_Packing)
root.order.add_edge(Crop_Packing, Logistics_Plan)

# Print the final result
print(root)