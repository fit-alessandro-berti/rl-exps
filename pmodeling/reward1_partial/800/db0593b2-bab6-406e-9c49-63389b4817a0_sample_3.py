from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Assess = Transition(label='Site Assess')
Env_Analysis = Transition(label='Env Analysis')
Modular_Install = Transition(label='Modular Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Selection = Transition(label='Crop Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Calibrate = Transition(label='Lighting Calibrate')
Pest_Monitor = Transition(label='Pest Monitor')
Staff_Training = Transition(label='Staff Training')
Energy_Integrate = Transition(label='Energy Integrate')
Data_Analytics = Transition(label='Data Analytics')
Waste_Recycle = Transition(label='Waste Recycle')
Market_Develop = Transition(label='Market Develop')
Yield_Optimize = Transition(label='Yield Optimize')
Climate_Simulate = Transition(label='Climate Simulate')

# Define partial order
root = StrictPartialOrder(nodes=[
    Site_Assess, Env_Analysis, Modular_Install, Irrigation_Setup,
    Crop_Selection, Nutrient_Mix, Lighting_Calibrate, Pest_Monitor,
    Staff_Training, Energy_Integrate, Data_Analytics, Waste_Recycle,
    Market_Develop, Yield_Optimize, Climate_Simulate
])

# Add dependencies
root.order.add_edge(Site_Assess, Env_Analysis)
root.order.add_edge(Env_Analysis, Modular_Install)
root.order.add_edge(Modular_Install, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Crop_Selection)
root.order.add_edge(Crop_Selection, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Lighting_Calibrate)
root.order.add_edge(Lighting_Calibrate, Pest_Monitor)
root.order.add_edge(Pest_Monitor, Staff_Training)
root.order.add_edge(Staff_Training, Energy_Integrate)
root.order.add_edge(Energy_Integrate, Data_Analytics)
root.order.add_edge(Data_Analytics, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Market_Develop)
root.order.add_edge(Market_Develop, Yield_Optimize)
root.order.add_edge(Yield_Optimize, Climate_Simulate)

print(root)