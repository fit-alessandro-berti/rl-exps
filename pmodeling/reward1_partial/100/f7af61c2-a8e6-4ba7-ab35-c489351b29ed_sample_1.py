import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
farm_design = Transition(label='Farm Design')
env_control = Transition(label='Env Control')
nutrient_prep = Transition(label='Nutrient Prep')
seed_selection = Transition(label='Seed Selection')
automated_plant = Transition(label='Automated Plant')
sensor_setup = Transition(label='Sensor Setup')
microclimate_monitor = Transition(label='Microclimate Mon')
health_monitor = Transition(label='Health Monitor')
light_adjust = Transition(label='Light Adjust')
irrigation_mod = Transition(label='Irrigation Mod')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
quality_check = Transition(label='Quality Check')
crop_harvest = Transition(label='Crop Harvest')
distribution_plan = Transition(label='Distribution Plan')

# Define transitions as silent transitions
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[light_adjust, irrigation_mod])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, energy_optimize])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, distribution_plan])

# Define XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, skip])

# Define the root process
root = StrictPartialOrder(nodes=[site_analysis, structure_check, farm_design, env_control, nutrient_prep, seed_selection, automated_plant, sensor_setup, microclimate_monitor, health_monitor, loop1, loop2, loop3, xor])
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, farm_design)
root.order.add_edge(farm_design, env_control)
root.order.add_edge(env_control, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_selection)
root.order.add_edge(seed_selection, automated_plant)
root.order.add_edge(automated_plant, sensor_setup)
root.order.add_edge(sensor_setup, microclimate_monitor)
root.order.add_edge(microclimate_monitor, health_monitor)
root.order.add_edge(health_monitor, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor)

print(root)