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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, system_build, install_sensors, select_crops,
    setup_lighting, configure_climate, nutrient_mix, automate_watering, test_systems,
    train_staff, waste_plan, market_link, data_monitor, optimize_yield
])

# Add dependencies if any (in this case, there are no explicit dependencies mentioned)
# If there were dependencies, you would add them like this:
# root.order.add_edge(site_survey, design_layout)
# root.order.add_edge(site_survey, system_build)
# root.order.add_edge(design_layout, install_sensors)
# root.order.add_edge(design_layout, select_crops)
# root.order.add_edge(design_layout, setup_lighting)
# root.order.add_edge(design_layout, configure_climate)
# root.order.add_edge(design_layout, nutrient_mix)
# root.order.add_edge(design_layout, automate_watering)
# root.order.add_edge(design_layout, test_systems)
# root.order.add_edge(design_layout, train_staff)
# root.order.add_edge(design_layout, waste_plan)
# root.order.add_edge(design_layout, market_link)
# root.order.add_edge(design_layout, data_monitor)
# root.order.add_edge(design_layout, optimize_yield)

# The root variable now contains the POWL model for the urban vertical farming process