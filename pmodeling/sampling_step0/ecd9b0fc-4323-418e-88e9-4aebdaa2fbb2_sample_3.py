import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
hydroponic_install = Transition(label='Hydroponic Install')
lighting_setup = Transition(label='Lighting Setup')
climate_control = Transition(label='Climate Control')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
water_recycling = Transition(label='Water Recycling')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
delivery_route = Transition(label='Delivery Route')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')

# Define the silent transitions
skip = SilentTransition()

# Define the loop for pest control
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, skip])

# Define the XOR for monitoring and pest control
monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control_loop])

# Define the loop for harvest plan and delivery route
harvest_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, delivery_route])

# Define the XOR for packaging prep and yield forecast
package_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, yield_forecast])

# Define the final XOR for all processes
final_xor = OperatorPOWL(operator=Operator.XOR, children=[monitor_xor, package_xor])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[
    site_survey, structure_check, hydroponic_install, lighting_setup, climate_control,
    seed_selection, nutrient_mix, water_recycling, sensor_deploy, pest_control_loop,
    monitor_xor, harvest_plan_loop, harvest_plan, delivery_route, packaging_prep, package_xor,
    final_xor
])

# Add dependencies between nodes
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, hydroponic_install)
root.order.add_edge(hydroponic_install, lighting_setup)
root.order.add_edge(lighting_setup, climate_control)
root.order.add_edge(climate_control, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, water_recycling)
root.order.add_edge(water_recycling, sensor_deploy)
root.order.add_edge(sensor_deploy, pest_control_loop)
root.order.add_edge(pest_control_loop, monitor_xor)
root.order.add_edge(monitor_xor, harvest_plan_loop)
root.order.add_edge(harvest_plan_loop, harvest_plan)
root.order.add_edge(harvest_plan, delivery_route)
root.order.add_edge(delivery_route, packaging_prep)
root.order.add_edge(packaging_prep, package_xor)
root.order.add_edge(package_xor, final_xor)

print(root)