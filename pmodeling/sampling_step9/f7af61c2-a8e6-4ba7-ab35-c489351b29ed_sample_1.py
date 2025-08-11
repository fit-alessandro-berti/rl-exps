import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
skip = SilentTransition()

# Define the process steps
site_analysis = OperatorPOWL(operator=Operator.AND, children=[Site_Analysis, Structure_Check])
farm_design = OperatorPOWL(operator=Operator.AND, children=[Farm_Design, Env_Control])
nutrient_prep = OperatorPOWL(operator=Operator.AND, children=[Nutrient_Prep, Seed_Selection])
automated_plant = OperatorPOWL(operator=Operator.AND, children=[Automated_Plant, Sensor_Setup])
microclimate_mon = OperatorPOWL(operator=Operator.AND, children=[Microclimate_Mon, Health_Monitor])
light_adjust = OperatorPOWL(operator=Operator.AND, children=[Light_Adjust, Irrigation_Mod])
waste_recycle = OperatorPOWL(operator=Operator.AND, children=[Waste_Recycle, Energy_Optimize])
quality_check = OperatorPOWL(operator=Operator.AND, children=[Quality_Check, Crop_Harvest])
distribution_plan = OperatorPOWL(operator=Operator.AND, children=[Distribution_Plan])

# Define the loop nodes
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[microclimate_mon, light_adjust, irrigation_mod])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, distribution_plan])

# Define the final POWL model
root = StrictPartialOrder(nodes=[site_analysis, farm_design, nutrient_prep, automated_plant, monitoring_loop, quality_loop])
root.order.add_edge(site_analysis, farm_design)
root.order.add_edge(farm_design, nutrient_prep)
root.order.add_edge(nutrient_prep, automated_plant)
root.order.add_edge(automated_plant, monitoring_loop)
root.order.add_edge(monitoring_loop, quality_loop)
root.order.add_edge(quality_loop, quality_loop)