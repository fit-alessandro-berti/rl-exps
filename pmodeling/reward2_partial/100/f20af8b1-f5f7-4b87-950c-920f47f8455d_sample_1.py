import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
Site_Survey = Transition(label='Site Survey')
Env_Analysis = Transition(label='Env Analysis')
Modular_Build = Transition(label='Modular Build')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Seed_Select = Transition(label='Seed Select')
Nutrient_Prep = Transition(label='Nutrient Prep')
Climate_Calibrate = Transition(label='Climate Calibrate')
Sensor_Install = Transition(label='Sensor Install')
AI_Integration = Transition(label='AI Integration')
Crop_Monitor = Transition(label='Crop Monitor')
Growth_Adjust = Transition(label='Growth Adjust')
Harvest_Sort = Transition(label='Harvest Sort')
Packaging = Transition(label='Packaging')
Distribution_Plan = Transition(label='Distribution Plan')
Sustain_Audit = Transition(label='Sustain Audit')
Energy_Optimize = Transition(label='Energy Optimize')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Env_Analysis, Modular_Build, Hydroponic_Setup,
    Seed_Select, Nutrient_Prep, Climate_Calibrate, Sensor_Install,
    AI_Integration, Crop_Monitor, Growth_Adjust, Harvest_Sort,
    Packaging, Distribution_Plan, Sustain_Audit, Energy_Optimize
])

# Define the dependencies (order)
root.order.add_edge(Site_Survey, Env_Analysis)
root.order.add_edge(Env_Analysis, Modular_Build)
root.order.add_edge(Modular_Build, Hydroponic_Setup)
root.order.add_edge(Hydroponic_Setup, Seed_Select)
root.order.add_edge(Seed_Select, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Climate_Calibrate)
root.order.add_edge(Climate_Calibrate, Sensor_Install)
root.order.add_edge(Sensor_Install, AI_Integration)
root.order.add_edge(AI_Integration, Crop_Monitor)
root.order.add_edge(Crop_Monitor, Growth_Adjust)
root.order.add_edge(Growth_Adjust, Harvest_Sort)
root.order.add_edge(Harvest_Sort, Packaging)
root.order.add_edge(Packaging, Distribution_Plan)
root.order.add_edge(Distribution_Plan, Sustain_Audit)
root.order.add_edge(Sustain_Audit, Energy_Optimize)

print(root)