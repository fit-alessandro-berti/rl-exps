import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
colony_sourcing = Transition(label='Colony Sourcing')
hive_design = Transition(label='Hive Design')
site_survey = Transition(label='Site Survey')
installation_prep = Transition(label='Installation Prep')
hive_setup = Transition(label='Hive Setup')
sensor_install = Transition(label='Sensor Install')
health_monitor = Transition(label='Health Monitor')
pest_control = Transition(label='Pest Control')
honey_harvest = Transition(label='Honey Harvest')
wax_processing = Transition(label='Wax Processing')
product_packaging = Transition(label='Product Packaging')
order_dispatch = Transition(label='Order Dispatch')
workshop_setup = Transition(label='Workshop Setup')
community_outreach = Transition(label='Community Outreach')
regulation_check = Transition(label='Regulation Check')
data_analysis = Transition(label='Data Analysis')
maintenance_plan = Transition(label='Maintenance Plan')

# Define silent transitions
skip = SilentTransition()

# Define the workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[honey_harvest, pest_control])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[product_packaging, order_dispatch])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[workshop_setup, community_outreach])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, data_analysis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, skip])

root = StrictPartialOrder(nodes=[colony_sourcing, hive_design, site_survey, installation_prep, hive_setup, sensor_install, health_monitor, loop, xor1, xor2, xor3, xor4])
root.order.add_edge(colony_sourcing, hive_design)
root.order.add_edge(hive_design, site_survey)
root.order.add_edge(site_survey, installation_prep)
root.order.add_edge(installation_prep, hive_setup)
root.order.add_edge(hive_setup, sensor_install)
root.order.add_edge(sensor_install, health_monitor)
root.order.add_edge(health_monitor, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(xor1, product_packaging)
root.order.add_edge(xor1, order_dispatch)
root.order.add_edge(xor2, workshop_setup)
root.order.add_edge(xor2, community_outreach)
root.order.add_edge(xor3, regulation_check)
root.order.add_edge(xor3, data_analysis)
root.order.add_edge(xor4, maintenance_plan)
root.order.add_edge(xor4, skip)

# Print the root
print(root)