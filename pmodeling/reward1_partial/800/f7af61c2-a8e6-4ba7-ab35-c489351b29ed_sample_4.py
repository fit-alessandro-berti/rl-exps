from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loops and choices
site_structure_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, structure_check])
farm_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_design, env_control])
nutrient_seed_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_prep, seed_selection])
sensor_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, microclimate_mon, health_monitor])
light_irrigation_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_adjust, irrigation_mod])
waste_energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, energy_optimize])
quality_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check])

# Define the root
root = StrictPartialOrder(nodes=[site_structure_loop, farm_design_loop, nutrient_seed_loop, sensor_monitor_loop, light_irrigation_loop, waste_energy_loop, quality_check_loop, crop_harvest, distribution_plan])
root.order.add_edge(site_structure_loop, farm_design_loop)
root.order.add_edge(farm_design_loop, nutrient_seed_loop)
root.order.add_edge(nutrient_seed_loop, sensor_monitor_loop)
root.order.add_edge(sensor_monitor_loop, light_irrigation_loop)
root.order.add_edge(light_irrigation_loop, waste_energy_loop)
root.order.add_edge(waste_energy_loop, quality_check_loop)
root.order.add_edge(quality_check_loop, crop_harvest)
root.order.add_edge(crop_harvest, distribution_plan)

print(root)