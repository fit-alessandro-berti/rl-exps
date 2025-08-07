import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Analysis': Transition(label='Site Analysis'),
    'Structure Check': Transition(label='Structure Check'),
    'Farm Design': Transition(label='Farm Design'),
    'Env Control': Transition(label='Env Control'),
    'Nutrient Prep': Transition(label='Nutrient Prep'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Automated Plant': Transition(label='Automated Plant'),
    'Sensor Setup': Transition(label='Sensor Setup'),
    'Microclimate Mon': Transition(label='Microclimate Mon'),
    'Health Monitor': Transition(label='Health Monitor'),
    'Light Adjust': Transition(label='Light Adjust'),
    'Irrigation Mod': Transition(label='Irrigation Mod'),
    'Waste Recycle': Transition(label='Waste Recycle'),
    'Energy Optimize': Transition(label='Energy Optimize'),
    'Quality Check': Transition(label='Quality Check'),
    'Crop Harvest': Transition(label='Crop Harvest'),
    'Distribution Plan': Transition(label='Distribution Plan')
}

# Define the process flow
site_analysis = activities['Site Analysis']
structure_check = activities['Structure Check']
farm_design = activities['Farm Design']
env_control = activities['Env Control']
nutrient_prep = activities['Nutrient Prep']
seed_selection = activities['Seed Selection']
automated_plant = activities['Automated Plant']
sensor_setup = activities['Sensor Setup']
microclimate_mon = activities['Microclimate Mon']
health_monitor = activities['Health Monitor']
light_adjust = activities['Light Adjust']
irrigation_mod = activities['Irrigation Mod']
waste_recycle = activities['Waste Recycle']
energy_optimize = activities['Energy Optimize']
quality_check = activities['Quality Check']
crop_harvest = activities['Crop Harvest']
distribution_plan = activities['Distribution Plan']

# Define the control flow operators
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[microclimate_mon, health_monitor, light_adjust, irrigation_mod])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, energy_optimize])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[quality_check])
choice_1 = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, distribution_plan])

# Construct the POWL model
root = StrictPartialOrder(nodes=[site_analysis, structure_check, farm_design, env_control, nutrient_prep, seed_selection, automated_plant, sensor_setup, loop_1, loop_2, loop_3, choice_1])
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, farm_design)
root.order.add_edge(farm_design, env_control)
root.order.add_edge(env_control, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_selection)
root.order.add_edge(seed_selection, automated_plant)
root.order.add_edge(automated_plant, sensor_setup)
root.order.add_edge(sensor_setup, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, choice_1)
root.order.add_edge(choice_1, choice_1)

print(root)