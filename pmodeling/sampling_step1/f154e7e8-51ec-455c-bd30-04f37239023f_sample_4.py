import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and exclusive choices
site_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, flora_mapping, hive_setup, sensor_install])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, data_logging])
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, workshop_plan])
hive_loop = OperatorPOWL(operator=Operator.LOOP, children=[honey_extract, quality_test, packaging, market_setup, sales_report])
regulation_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, waste_manage, seasonal_review])

# Define the root process
root = StrictPartialOrder(nodes=[site_setup_loop, pest_control_loop, community_loop, hive_loop, regulation_loop])

# Define dependencies between nodes
root.order.add_edge(site_setup_loop, pest_control_loop)
root.order.add_edge(site_setup_loop, community_loop)
root.order.add_edge(pest_control_loop, hive_loop)
root.order.add_edge(community_loop, hive_loop)
root.order.add_edge(hive_loop, regulation_loop)

print(root)