from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loop for hive maintenance
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    health_check, pest_control, data_logging
])

# Define exclusive choice for community engagement
community_engagement = OperatorPOWL(operator=Operator.XOR, children=[
    community_meet, workshop_plan
])

# Define exclusive choice for honey production
honey_production = OperatorPOWL(operator=Operator.XOR, children=[
    honey_extract, quality_test, packaging, market_setup
])

# Define exclusive choice for market setup and sales report
market_setup_sales = OperatorPOWL(operator=Operator.XOR, children=[
    market_setup, sales_report
])

# Define exclusive choice for regulation check and waste manage
regulation_waste = OperatorPOWL(operator=Operator.XOR, children=[
    regulation_check, waste_manage
])

# Define exclusive choice for seasonal review and maintenance loop
seasonal_review_loop = OperatorPOWL(operator=Operator.XOR, children=[
    seasonal_review, maintenance_loop
])

# Define root model
root = StrictPartialOrder(nodes=[
    site_survey, flora_mapping, hive_setup, sensor_install,
    community_engagement, honey_production, market_setup_sales,
    regulation_waste, seasonal_review_loop
])
root.order.add_edge(site_survey, flora_mapping)
root.order.add_edge(site_survey, hive_setup)
root.order.add_edge(hive_setup, sensor_install)
root.order.add_edge(sensor_install, health_check)
root.order.add_edge(sensor_install, pest_control)
root.order.add_edge(health_check, data_logging)
root.order.add_edge(health_check, maintenance_loop)
root.order.add_edge(pest_control, maintenance_loop)
root.order.add_edge(maintenance_loop, community_engagement)
root.order.add_edge(community_engagement, honey_production)
root.order.add_edge(honey_production, market_setup_sales)
root.order.add_edge(market_setup_sales, regulation_waste)
root.order.add_edge(regulation_waste, seasonal_review_loop)
root.order.add_edge(seasonal_review_loop, site_survey)

# Print the root model
print(root)