import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop for microclimate monitoring and health monitoring
loop = OperatorPOWL(operator=Operator.LOOP, children=[microclimate_mon, health_monitor])

# Define the exclusive choice for sensor setup and light adjustment
xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, light_adjust])

# Define the exclusive choice for irrigation modification and waste recycling
xor2 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_mod, waste_recycle])

# Define the exclusive choice for energy optimization and quality check
xor3 = OperatorPOWL(operator=Operator.XOR, children=[energy_optimize, quality_check])

# Define the exclusive choice for crop harvesting and distribution planning
xor4 = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, distribution_plan])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_analysis, structure_check, farm_design, env_control, nutrient_prep, seed_selection, automated_plant, loop, xor, xor2, xor3, xor4])
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, farm_design)
root.order.add_edge(farm_design, env_control)
root.order.add_edge(env_control, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_selection)
root.order.add_edge(seed_selection, automated_plant)
root.order.add_edge(automated_plant, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, quality_check)
root.order.add_edge(quality_check, crop_harvest)
root.order.add_edge(crop_harvest, distribution_plan)