import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the control flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[select_crops, waste_plan])
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_build, install_sensors, setup_lighting, configure_climate, nutrient_mix, automate_watering, test_systems, train_staff, exclusive_choice, market_link, data_monitor, optimize_yield])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, select_crops)
root.order.add_edge(loop, waste_plan)
root.order.add_edge(select_crops, system_build)
root.order.add_edge(system_build, install_sensors)
root.order.add_edge(install_sensors, setup_lighting)
root.order.add_edge(setup_lighting, configure_climate)
root.order.add_edge(configure_climate, nutrient_mix)
root.order.add_edge(nutrient_mix, automate_watering)
root.order.add_edge(automate_watering, test_systems)
root.order.add_edge(test_systems, train_staff)
root.order.add_edge(train_staff, exclusive_choice)
root.order.add_edge(exclusive_choice, market_link)
root.order.add_edge(market_link, data_monitor)
root.order.add_edge(data_monitor, optimize_yield)