import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
farm_design = Transition(label='Farm Design')
env_control = Transition(label='Env Control')
nutrient_prep = Transition(label='Nutrient Prep')
seed_selection = Transition(label='Seed Selection')
automated_plant = Transition(label='Automated Plant')
sensor_setup = Transition(label='Sensor Setup')
microclimate_mon = Transition(label='Microclimate Mon')
health_monitor = Transition(label='Health Monitor')
light_adjust = Transition(label='Light Adjust')
irrigation_mod = Transition(label='Irrigation Mod')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
quality_check = Transition(label='Quality Check')
crop_harvest = Transition(label='Crop Harvest')
distribution_plan = Transition(label='Distribution Plan')

# Define the process structure
root = StrictPartialOrder(nodes=[site_analysis, structure_check, farm_design, env_control, nutrient_prep, seed_selection, automated_plant, sensor_setup, microclimate_mon, health_monitor, light_adjust, irrigation_mod, waste_recycle, energy_optimize, quality_check, crop_harvest, distribution_plan])

# Define the dependencies between nodes
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, farm_design)
root.order.add_edge(farm_design, env_control)
root.order.add_edge(env_control, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_selection)
root.order.add_edge(seed_selection, automated_plant)
root.order.add_edge(automated_plant, sensor_setup)
root.order.add_edge(sensor_setup, microclimate_mon)
root.order.add_edge(microclimate_mon, health_monitor)
root.order.add_edge(health_monitor, light_adjust)
root.order.add_edge(light_adjust, irrigation_mod)
root.order.add_edge(irrigation_mod, waste_recycle)
root.order.add_edge(waste_recycle, energy_optimize)
root.order.add_edge(energy_optimize, quality_check)
root.order.add_edge(quality_check, crop_harvest)
root.order.add_edge(crop_harvest, distribution_plan)

# Print the POWL model
print(root)