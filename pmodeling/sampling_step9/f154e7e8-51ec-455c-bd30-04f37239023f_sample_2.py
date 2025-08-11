import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
flora_mapping = Transition(label='Flora Mapping')
hive_setup = Transition(label='Hive Setup')
sensor_install = Transition(label='Sensor Install')
health_check = Transition(label='Health Check')
pest_control = Transition(label='Pest Control')
data_logging = Transition(label='Data Logging')
community_meet = Transition(label='Community Meet')
workshop_plan = Transition(label='Workshop Plan')
honey_extract = Transition(label='Honey Extract')
quality_test = Transition(label='Quality Test')
packaging = Transition(label='Packaging')
market_setup = Transition(label='Market Setup')
sales_report = Transition(label='Sales Report')
regulation_check = Transition(label='Regulation Check')
waste_manage = Transition(label='Waste Manage')
seasonal_review = Transition(label='Seasonal Review')

# Define silent transitions
skip = SilentTransition()

# Define the partial order model
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, flora_mapping])
loop_hive_setup = OperatorPOWL(operator=Operator.LOOP, children=[hive_setup, sensor_install])
loop_health_check = OperatorPOWL(operator=Operator.LOOP, children=[health_check, pest_control, data_logging])
loop_community_meet = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, workshop_plan])
loop_honey_extract = OperatorPOWL(operator=Operator.LOOP, children=[honey_extract, quality_test, packaging, market_setup, sales_report, regulation_check, waste_manage, seasonal_review])

# Define the root node with all loops as children
root = StrictPartialOrder(nodes=[loop_site_survey, loop_hive_setup, loop_health_check, loop_community_meet, loop_honey_extract])
root.order.add_edge(loop_site_survey, loop_hive_setup)
root.order.add_edge(loop_hive_setup, loop_health_check)
root.order.add_edge(loop_health_check, loop_community_meet)
root.order.add_edge(loop_community_meet, loop_honey_extract)

print(root)