import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Create a loop for hive maintenance
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    health_check, pest_control, data_logging
])

# Create an XOR for honey production and seasonal review
honey_production = OperatorPOWL(operator=Operator.XOR, children=[
    honey_extract, quality_test, packaging, market_setup, sales_report
])
seasonal_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    seasonal_review
])

# Connect the loops and other activities
root = StrictPartialOrder(nodes=[
    site_survey, flora_mapping, hive_setup, sensor_install, maintenance_loop, honey_production, seasonal_review_loop
])
root.order.add_edge(site_survey, flora_mapping)
root.order.add_edge(flora_mapping, hive_setup)
root.order.add_edge(hive_setup, sensor_install)
root.order.add_edge(sensor_install, maintenance_loop)
root.order.add_edge(maintenance_loop, honey_production)
root.order.add_edge(honey_production, seasonal_review_loop)
root.order.add_edge(seasonal_review_loop, seasonal_review)