import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
site_analysis = Transition(label='Site Analysis')
env_assessment = Transition(label='Env Assessment')
system_design = Transition(label='System Design')
equipment_order = Transition(label='Equipment Order')
seed_selection = Transition(label='Seed Selection')
install_modules = Transition(label='Install Modules')
calibrate_systems = Transition(label='Calibrate Systems')
staff_training = Transition(label='Staff Training')
plant_seeding = Transition(label='Plant Seeding')
iot_monitoring = Transition(label='IoT Monitoring')
data_analytics = Transition(label='Data Analytics')
nutrient_adjust = Transition(label='Nutrient Adjust')
pest_control = Transition(label='Pest Control')
maintenance_check = Transition(label='Maintenance Check')
market_launch = Transition(label='Market Launch')
logistics_setup = Transition(label='Logistics Setup')

# Define silent transitions
skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, env_assessment])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[system_design, equipment_order])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, install_modules])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[calibrate_systems, staff_training])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[plant_seeding, iot_monitoring])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[data_analytics, nutrient_adjust])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, maintenance_check])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[market_launch, logistics_setup])

# Create the root
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])

# Add edges to the root
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop1)

print(root)