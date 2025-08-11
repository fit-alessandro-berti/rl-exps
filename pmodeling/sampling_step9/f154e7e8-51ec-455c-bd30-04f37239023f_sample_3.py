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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, flora_mapping, hive_setup, sensor_install, health_check, pest_control,
    data_logging, community_meet, workshop_plan, honey_extract, quality_test, packaging,
    market_setup, sales_report, regulation_check, waste_manage, seasonal_review
])

# Define the dependencies between nodes
root.order.add_edge(site_survey, flora_mapping)
root.order.add_edge(site_survey, hive_setup)
root.order.add_edge(site_survey, sensor_install)
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

# Add a loop for seasonal review
loop = OperatorPOWL(operator=Operator.LOOP, children=[seasonal_review])
root.order.add_edge(loop, seasonal_review)

# Add an exclusive choice between seasonal review and waste manage
xor = OperatorPOWL(operator=Operator.XOR, children=[loop, waste_manage])
root.order.add_edge(xor, seasonal_review)
root.order.add_edge(xor, waste_manage)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop_plan)
root.order.add_edge(xor, community_meet)

# Add a choice between honey extract and quality test
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
root.order.add_edge(xor, honey_extract)
root.order.add_edge(xor, quality_test)

# Add a choice between packaging and market setup
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, market_setup)

# Add a choice between sales report and regulation check
xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
root.order.add_edge(xor, sales_report)
root.order.add_edge(xor, regulation_check)

# Add a choice between hive setup and sensor install
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, sensor_install])
root.order.add_edge(xor, hive_setup)
root.order.add_edge(xor, sensor_install)

# Add a choice between health check and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
root.order.add_edge(xor, health_check)
root.order.add_edge(xor, pest_control)

# Add a choice between data logging and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, community_meet])
root.order.add_edge(xor, data_logging)
root.order.add_edge(xor, community_meet)

# Add a choice between workshop plan and community meet
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
root.order.add_edge(xor, workshop