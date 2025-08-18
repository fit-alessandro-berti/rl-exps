from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Site_Analysis = Transition(label='Site Analysis')
Structure_Check = Transition(label='Structure Check')
Farm_Design = Transition(label='Farm Design')
Env_Control = Transition(label='Env Control')
Nutrient_Prep = Transition(label='Nutrient Prep')
Seed_Selection = Transition(label='Seed Selection')
Automated_Plant = Transition(label='Automated Plant')
Sensor_Setup = Transition(label='Sensor Setup')
Microclimate_Mon = Transition(label='Microclimate Mon')
Health_Monitor = Transition(label='Health Monitor')
Light_Adjust = Transition(label='Light Adjust')
Irrigation_Mod = Transition(label='Irrigation Mod')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Optimize = Transition(label='Energy Optimize')
Quality_Check = Transition(label='Quality Check')
Crop_Harvest = Transition(label='Crop Harvest')
Distribution_Plan = Transition(label='Distribution Plan')

# Define the partial order (POWL model)
root = StrictPartialOrder(nodes=[
    Site_Analysis,
    Structure_Check,
    Farm_Design,
    Env_Control,
    Nutrient_Prep,
    Seed_Selection,
    Automated_Plant,
    Sensor_Setup,
    Microclimate_Mon,
    Health_Monitor,
    Light_Adjust,
    Irrigation_Mod,
    Waste_Recycle,
    Energy_Optimize,
    Quality_Check,
    Crop_Harvest,
    Distribution_Plan
])

# Add the dependencies (partial order edges)
root.order.add_edge(Site_Analysis, Structure_Check)
root.order.add_edge(Structure_Check, Farm_Design)
root.order.add_edge(Farm_Design, Env_Control)
root.order.add_edge(Env_Control, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Seed_Selection)
root.order.add_edge(Seed_Selection, Automated_Plant)
root.order.add_edge(Automated_Plant, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Microclimate_Mon)
root.order.add_edge(Microclimate_Mon, Health_Monitor)
root.order.add_edge(Health_Monitor, Light_Adjust)
root.order.add_edge(Light_Adjust, Irrigation_Mod)
root.order.add_edge(Irrigation_Mod, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Energy_Optimize)
root.order.add_edge(Energy_Optimize, Quality_Check)
root.order.add_edge(Quality_Check, Crop_Harvest)
root.order.add_edge(Crop_Harvest, Distribution_Plan)

# Print the root to verify
print(root)