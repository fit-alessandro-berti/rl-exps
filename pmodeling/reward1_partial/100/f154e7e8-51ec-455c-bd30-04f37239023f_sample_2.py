import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
site_survey_flora_mapping = OperatorPOWL(operator=Operator.XOR, children=[site_survey, flora_mapping])
hive_setup_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
health_check_pest_control = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
data_logging_community_meet = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
workshop_plan_honey_extract = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, honey_extract])
quality_test_packaging = OperatorPOWL(operator=Operator.XOR, children=[quality_test, packaging])
market_setup_sales_report = OperatorPOWL(operator=Operator.XOR, children=[market_setup, sales_report])
regulation_check_waste_manage = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, waste_manage])
seasonal_review = OperatorPOWL(operator=Operator.LOOP, children=[seasonal_review])

# Define root
root = StrictPartialOrder(nodes=[site_survey_flora_mapping, hive_setup_sensor_install, health_check_pest_control, data_logging_community_meet, workshop_plan_honey_extract, quality_test_packaging, market_setup_sales_report, regulation_check_waste_manage, seasonal_review])
root.order.add_edge(site_survey_flora_mapping, hive_setup_sensor_install)
root.order.add_edge(hive_setup_sensor_install, health_check_pest_control)
root.order.add_edge(health_check_pest_control, data_logging_community_meet)
root.order.add_edge(data_logging_community_meet, workshop_plan_honey_extract)
root.order.add_edge(workshop_plan_honey_extract, quality_test_packaging)
root.order.add_edge(quality_test_packaging, market_setup_sales_report)
root.order.add_edge(market_setup_sales_report, regulation_check_waste_manage)
root.order.add_edge(regulation_check_waste_manage, seasonal_review)
root.order.add_edge(seasonal_review, seasonal_review)