import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[hive_design, site_survey, installation_prep, hive_setup])
inclusive_choice = OperatorPOWL(operator=Operator.INCLUSIVE, children=[sensor_install, health_monitor, pest_control])
loop = OperatorPOWL(operator=Operator.LOOP, children=[honey_harvest, wax_processing, product_packaging])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[order_dispatch, workshop_setup, community_outreach])
inclusive_choice2 = OperatorPOWL(operator=Operator.INCLUSIVE, children=[regulation_check, data_analysis])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, inclusive_choice2])

# Define the root
root = StrictPartialOrder(nodes=[exclusive_choice, inclusive_choice, loop, exclusive_choice2, inclusive_choice2, exclusive_choice3])
root.order.add_edge(exclusive_choice, inclusive_choice)
root.order.add_edge(inclusive_choice, loop)
root.order.add_edge(loop, exclusive_choice2)
root.order.add_edge(exclusive_choice2, inclusive_choice2)
root.order.add_edge(inclusive_choice2, exclusive_choice3)