import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_analysis   = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
farm_design     = Transition(label='Farm Design')
env_control     = Transition(label='Env Control')
nutrient_prep   = Transition(label='Nutrient Prep')
seed_selection  = Transition(label='Seed Selection')
automated_plant = Transition(label='Automated Plant')
sensor_setup    = Transition(label='Sensor Setup')
microclimate_mon= Transition(label='Microclimate Mon')
health_monitor  = Transition(label='Health Monitor')
light_adjust    = Transition(label='Light Adjust')
irrigation_mod  = Transition(label='Irrigation Mod')
waste_recycle   = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
quality_check   = Transition(label='Quality Check')
crop_harvest    = Transition(label='Crop Harvest')
distribution_plan = Transition(label='Distribution Plan')

# Build the loop body: Monitor -> Adjust -> Recycle -> Optimize
monitor_body = StrictPartialOrder(nodes=[microclimate_mon, health_monitor])
monitor_body.order.add_edge(microclimate_mon, health_monitor)

adjust_body = StrictPartialOrder(nodes=[light_adjust, irrigation_mod])
adjust_body.order.add_edge(light_adjust, irrigation_mod)

recycle_body = StrictPartialOrder(nodes=[waste_recycle])
recycle_body.order.add_edge(waste_recycle, waste_recycle)

optimize_body = StrictPartialOrder(nodes=[energy_optimize])
optimize_body.order.add_edge(energy_optimize, energy_optimize)

# LOOP: Monitor -> Adjust -> Recycle -> Optimize, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, adjust_body, recycle_body, optimize_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis, structure_check, farm_design, env_control,
    nutrient_prep, seed_selection, automated_plant, sensor_setup,
    loop, quality_check, crop_harvest, distribution_plan
])

# Sequence edges
root.order.add_edge(site_analysis,    structure_check)
root.order.add_edge(structure_check,  farm_design)
root.order.add_edge(farm_design,      env_control)
root.order.add_edge(env_control,      nutrient_prep)
root.order.add_edge(nutrient_prep,    seed_selection)
root.order.add_edge(seed_selection,   automated_plant)
root.order.add_edge(automated_plant,  sensor_setup)
root.order.add_edge(sensor_setup,     loop)
root.order.add_edge(loop,             quality_check)
root.order.add_edge(quality_check,    crop_harvest)
root.order.add_edge(crop_harvest,     distribution_plan)