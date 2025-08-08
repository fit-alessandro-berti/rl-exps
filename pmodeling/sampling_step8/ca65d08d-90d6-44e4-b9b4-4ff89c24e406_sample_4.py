import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_build = Transition(label='System Build')
install_sensors = Transition(label='Install Sensors')
select_crops = Transition(label='Select Crops')
setup_lighting = Transition(label='Setup Lighting')
configure_climate = Transition(label='Configure Climate')
nutrient_mix = Transition(label='Nutrient Mix')
automate_watering = Transition(label='Automate Watering')
test_systems = Transition(label='Test Systems')
train_staff = Transition(label='Train Staff')
waste_plan = Transition(label='Waste Plan')
market_link = Transition(label='Market Link')
data_monitor = Transition(label='Data Monitor')
optimize_yield = Transition(label='Optimize Yield')

# Define silent transitions (if any)
skip = SilentTransition()

# Define loops and choices
site_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
layout_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout])
build_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_build])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_sensors])
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[select_crops])
lighting_loop = OperatorPOWL(operator=Operator.LOOP, children=[setup_lighting])
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[configure_climate])
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
watering_loop = OperatorPOWL(operator=Operator.LOOP, children=[automate_watering])
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_systems])
train_loop = OperatorPOWL(operator=Operator.LOOP, children=[train_staff])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_plan])
market_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_link])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor])
optimize_loop = OperatorPOWL(operator=Operator.LOOP, children=[optimize_yield])

# Create the root node with all transitions
root = StrictPartialOrder(nodes=[
    site_loop, layout_loop, build_loop, sensor_loop, crop_loop,
    lighting_loop, climate_loop, nutrient_loop, watering_loop,
    test_loop, train_loop, waste_loop, market_loop, monitor_loop, optimize_loop
])

# Define the dependencies between transitions
root.order.add_edge(site_loop, layout_loop)
root.order.add_edge(layout_loop, build_loop)
root.order.add_edge(build_loop, sensor_loop)
root.order.add_edge(sensor_loop, crop_loop)
root.order.add_edge(crop_loop, lighting_loop)
root.order.add_edge(lighting_loop, climate_loop)
root.order.add_edge(climate_loop, nutrient_loop)
root.order.add_edge(nutrient_loop, watering_loop)
root.order.add_edge(watering_loop, test_loop)
root.order.add_edge(test_loop, train_loop)
root.order.add_edge(train_loop, waste_loop)
root.order.add_edge(waste_loop, market_loop)
root.order.add_edge(market_loop, monitor_loop)
root.order.add_edge(monitor_loop, optimize_loop)

# Print the root node to verify
print(root)