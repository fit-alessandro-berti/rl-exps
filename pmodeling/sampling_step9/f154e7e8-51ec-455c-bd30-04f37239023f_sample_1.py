import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define loops and choices
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, health_check, data_logging])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, hive_setup])
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, workshop_plan])
seasonal_loop = OperatorPOWL(operator=Operator.LOOP, children=[seasonal_review, hive_setup, hive_setup])

# Define the root POWL model
root = StrictPartialOrder(nodes=[sensor_loop, pest_loop, community_loop, seasonal_loop])
root.order.add_edge(sensor_loop, health_check)
root.order.add_edge(pest_loop, hive_setup)
root.order.add_edge(community_loop, workshop_plan)
root.order.add_edge(seasonal_loop, hive_setup)
root.order.add_edge(seasonal_loop, hive_setup)