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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, flora_mapping, hive_setup, sensor_install, health_check, pest_control, data_logging,
    community_meet, workshop_plan, honey_extract, quality_test, packaging, market_setup, sales_report,
    regulation_check, waste_manage, seasonal_review
])

# Define the partial order dependencies
root.order.add_edge(site_survey, flora_mapping)
root.order.add_edge(flora_mapping, hive_setup)
root.order.add_edge(hive_setup, sensor_install)
root.order.add_edge(sensor_install, health_check)
root.order.add_edge(health_check, pest_control)
root.order.add_edge(pest_control, data_logging)
root.order.add_edge(data_logging, community_meet)
root.order.add_edge(community_meet, workshop_plan)
root.order.add_edge(workshop_plan, honey_extract)
root.order.add_edge(honey_extract, quality_test)
root.order.add_edge(quality_test, packaging)
root.order.add_edge(packaging, market_setup)
root.order.add_edge(market_setup, sales_report)
root.order.add_edge(sales_report, regulation_check)
root.order.add_edge(regulation_check, waste_manage)
root.order.add_edge(waste_manage, seasonal_review)

print(root)