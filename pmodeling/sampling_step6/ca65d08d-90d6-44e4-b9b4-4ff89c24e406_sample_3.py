import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

root = StrictPartialOrder(nodes=[site_survey, design_layout, system_build, install_sensors, select_crops, setup_lighting, configure_climate, nutrient_mix, automate_watering, test_systems, train_staff, waste_plan, market_link, data_monitor, optimize_yield])

# Since there are no dependencies between activities, the order is not explicitly defined in this model.
# However, if there were dependencies, you would add them using root.order.add_edge(source, target).
# For example, if site_survey must happen before design_layout, you would add: root.order.add_edge(site_survey, design_layout).