import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
flora_mapping    = Transition(label='Flora Mapping')
hive_setup       = Transition(label='Hive Setup')
sensor_install   = Transition(label='Sensor Install')
health_check     = Transition(label='Health Check')
data_logging     = Transition(label='Data Logging')
pest_control     = Transition(label='Pest Control')
community_meet   = Transition(label='Community Meet')
workshop_plan    = Transition(label='Workshop Plan')
honey_extract    = Transition(label='Honey Extract')
quality_test     = Transition(label='Quality Test')
packaging        = Transition(label='Packaging')
market_setup     = Transition(label='Market Setup')
sales_report     = Transition(label='Sales Report')
regulation_check = Transition(label='Regulation Check')
waste_manage     = Transition(label='Waste Manage')
seasonal_review  = Transition(label='Seasonal Review')

# Loop for ongoing monitoring: Data Logging -> Pest Control -> Health Check
loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_logging, pest_control, health_check]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    flora_mapping,
    hive_setup,
    sensor_install,
    loop_monitor,
    community_meet,
    workshop_plan,
    honey_extract,
    quality_test,
    packaging,
    market_setup,
    sales_report,
    regulation_check,
    waste_manage,
    seasonal_review
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, flora_mapping)
root.order.add_edge(site_survey, hive_setup)
root.order.add_edge(site_survey, sensor_install)
root.order.add_edge(flora_mapping, hive_setup)
root.order.add_edge(flora_mapping, sensor_install)
root.order.add_edge(hive_setup, loop_monitor)
root.order.add_edge(hive_setup, community_meet)
root.order.add_edge(hive_setup, workshop_plan)
root.order.add_edge(sensor_install, loop_monitor)
root.order.add_edge(sensor_install, community_meet)
root.order.add_edge(sensor_install, workshop_plan)
root.order.add_edge(loop_monitor, honey_extract)
root.order.add_edge(loop_monitor, quality_test)
root.order.add_edge(community_meet, workshop_plan)
root.order.add_edge(community_meet, regulation_check)
root.order.add_edge(community_meet, waste_manage)
root.order.add_edge(workshop_plan, regulation_check)
root.order.add_edge(workshop_plan, waste_manage)
root.order.add_edge(honey_extract, packaging)
root.order.add_edge(honey_extract, market_setup)
root.order.add_edge(honey_extract, sales_report)
root.order.add_edge(quality_test, packaging)
root.order.add_edge(quality_test, market_setup)
root.order.add_edge(quality_test, sales_report)
root.order.add_edge(packing, market_setup)
root.order.add_edge(market_setup, sales_report)
root.order.add_edge(regulation_check, seasonal_review)
root.order.add_edge(waste_manage, seasonal_review)
root.order.add_edge(seasonal_review, site_survey)