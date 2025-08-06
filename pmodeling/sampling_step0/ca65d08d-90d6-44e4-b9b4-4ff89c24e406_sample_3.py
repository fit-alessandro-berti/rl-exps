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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define loop nodes
loop_system_build = OperatorPOWL(operator=Operator.LOOP, children=[system_build, select_crops, setup_lighting, configure_climate, nutrient_mix, automate_watering, test_systems])
loop_training = OperatorPOWL(operator=Operator.LOOP, children=[train_staff, waste_plan, market_link, data_monitor])

# Define XOR nodes
xor_monitoring = OperatorPOWL(operator=Operator.XOR, children=[optimize_yield, skip])

# Define partial order
root = StrictPartialOrder(nodes=[loop_system_build, loop_training, xor_monitoring])
root.order.add_edge(loop_system_build, loop_training)
root.order.add_edge(loop_training, xor_monitoring)

print(root)