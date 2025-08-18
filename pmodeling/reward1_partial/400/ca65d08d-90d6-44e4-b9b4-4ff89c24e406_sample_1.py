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

# Define partial order nodes
site_survey_node = OperatorPOWL(operator=Operator.PARALLEL, children=[site_survey, design_layout])
design_layout_node = OperatorPOWL(operator=Operator.PARALLEL, children=[system_build, install_sensors])
system_build_node = OperatorPOWL(operator=Operator.PARALLEL, children=[select_crops, setup_lighting])
install_sensors_node = OperatorPOWL(operator=Operator.PARALLEL, children=[configure_climate, nutrient_mix])
select_crops_node = OperatorPOWL(operator=Operator.PARALLEL, children=[automate_watering, test_systems])
setup_lighting_node = OperatorPOWL(operator=Operator.PARALLEL, children=[train_staff, waste_plan])
configure_climate_node = OperatorPOWL(operator=Operator.PARALLEL, children=[market_link, data_monitor])
nutrient_mix_node = OperatorPOWL(operator=Operator.PARALLEL, children=[optimize_yield, waste_plan])
automate_watering_node = OperatorPOWL(operator=Operator.PARALLEL, children=[market_link, data_monitor])
test_systems_node = OperatorPOWL(operator=Operator.PARALLEL, children=[optimize_yield, waste_plan])

# Define partial order graph
root = StrictPartialOrder(nodes=[site_survey_node, design_layout_node, system_build_node, install_sensors_node, select_crops_node, setup_lighting_node, configure_climate_node, nutrient_mix_node, automate_watering_node, test_systems_node, train_staff, waste_plan, market_link, data_monitor, optimize_yield])
root.order.add_edge(site_survey_node, design_layout_node)
root.order.add_edge(design_layout_node, system_build_node)
root.order.add_edge(system_build_node, install_sensors_node)
root.order.add_edge(install_sensors_node, configure_climate_node)
root.order.add_edge(configure_climate_node, nutrient_mix_node)
root.order.add_edge(nutrient_mix_node, automate_watering_node)
root.order.add_edge(automate_watering_node, test_systems_node)
root.order.add_edge(test_systems_node, train_staff)
root.order.add_edge(train_staff, waste_plan)
root.order.add_edge(waste_plan, market_link)
root.order.add_edge(market_link, data_monitor)
root.order.add_edge(data_monitor, optimize_yield)

print(root)