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

# Define transitions for the XOR (exclusive choice) of Select Crops and Waste Plan
xor = OperatorPOWL(operator=Operator.XOR, children=[select_crops, waste_plan])

# Define the root POWL model with the defined activities and XOR
root = StrictPartialOrder(nodes=[site_survey, design_layout, system_build, install_sensors, xor, test_systems, train_staff, market_link, data_monitor, optimize_yield])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, system_build)
root.order.add_edge(design_layout, system_build)
root.order.add_edge(system_build, install_sensors)
root.order.add_edge(install_sensors, test_systems)
root.order.add_edge(test_systems, train_staff)
root.order.add_edge(train_staff, market_link)
root.order.add_edge(market_link, data_monitor)
root.order.add_edge(data_monitor, optimize_yield)

print(root)