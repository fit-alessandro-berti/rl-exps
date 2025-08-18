from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the POWL model
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

# Define the loop for system build and test
system_build_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_build, test_systems])

# Define the exclusive choice for waste plan and market link
waste_plan_market_link = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, market_link])

# Define the root POWL model with the defined nodes and dependencies
root = StrictPartialOrder(nodes=[site_survey, design_layout, system_build_loop, install_sensors, select_crops, setup_lighting, configure_climate, nutrient_mix, automate_watering, train_staff, waste_plan_market_link, data_monitor, optimize_yield])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_build_loop)
root.order.add_edge(system_build_loop, install_sensors)
root.order.add_edge(install_sensors, select_crops)
root.order.add_edge(select_crops, setup_lighting)
root.order.add_edge(setup_lighting, configure_climate)
root.order.add_edge(configure_climate, nutrient_mix)
root.order.add_edge(nutrient_mix, automate_watering)
root.order.add_edge(automate_watering, test_systems)
root.order.add_edge(test_systems, system_build_loop)
root.order.add_edge(system_build_loop, train_staff)
root.order.add_edge(train_staff, waste_plan_market_link)
root.order.add_edge(waste_plan_market_link, data_monitor)
root.order.add_edge(data_monitor, optimize_yield)

print(root)