import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Structure_Prep = Transition(label='Structure Prep')
System_Install = Transition(label='System Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Setup = Transition(label='Sensor Setup')
AI_Calibration = Transition(label='AI Calibration')
Seed_Sourcing = Transition(label='Seed Sourcing')
Staff_Training = Transition(label='Staff Training')
Energy_Connect = Transition(label='Energy Connect')
Water_Cycle = Transition(label='Water Cycle')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Audit = Transition(label='Waste Audit')
Community_Meet = Transition(label='Community Meet')
Data_Review = Transition(label='Data Review')
Yield_Forecast = Transition(label='Yield Forecast')

# Define the partial order relationships between the activities
root = StrictPartialOrder(nodes=[Site_Survey, Permit_Filing, Structure_Prep, System_Install, Nutrient_Mix, Sensor_Setup, AI_Calibration, Seed_Sourcing, Staff_Training, Energy_Connect, Water_Cycle, Growth_Monitor, Waste_Audit, Community_Meet, Data_Review, Yield_Forecast])

# Define the dependencies between activities
root.order.add_edge(Site_Survey, Permit_Filing)
root.order.add_edge(Site_Survey, Structure_Prep)
root.order.add_edge(Permit_Filing, Structure_Prep)
root.order.add_edge(Structure_Prep, System_Install)
root.order.add_edge(System_Install, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Sensor_Setup)
root.order.add_edge(Sensor_Setup, AI_Calibration)
root.order.add_edge(AI_Calibration, Seed_Sourcing)
root.order.add_edge(Seed_Sourcing, Staff_Training)
root.order.add_edge(Staff_Training, Energy_Connect)
root.order.add_edge(Energy_Connect, Water_Cycle)
root.order.add_edge(Water_Cycle, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Waste_Audit)
root.order.add_edge(Waste_Audit, Community_Meet)
root.order.add_edge(Community_Meet, Data_Review)
root.order.add_edge(Data_Review, Yield_Forecast)

# Print the final POWL model
print(root)