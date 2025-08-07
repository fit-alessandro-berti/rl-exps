import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
flora_mapping    = Transition(label='Flora Mapping')
hive_setup       = Transition(label='Hive Setup')
sensor_install   = Transition(label='Sensor Install')
health_check     = Transition(label='Health Check')
pest_control     = Transition(label='Pest Control')
data_logging     = Transition(label='Data Logging')
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

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, flora_mapping, hive_setup, sensor_install,
    health_check, pest_control, data_logging,
    community_meet, workshop_plan,
    honey_extract, quality_test, packaging,
    market_setup, sales_report,
    regulation_check, waste_manage,
    seasonal_review
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, flora_mapping)
root.order.add_edge(flora_mapping, hive_setup)
root.order.add_edge(hive_setup, sensor_install)

# After sensor install, perform health check and pest control in parallel
root.order.add_edge(sensor_install, health_check)
root.order.add_edge(sensor_install, pest_control)

# Then, do data logging
root.order.add_edge(health_check, data_logging)
root.order.add_edge(pest_control, data_logging)

# After data logging, proceed to community meet and workshop plan in parallel
root.order.add_edge(data_logging, community_meet)
root.order.add_edge(data_logging, workshop_plan)

# Both community meet and workshop plan can be done concurrently
root.order.add_edge(community_meet, honey_extract)
root.order.add_edge(workshop_plan, honey_extract)

# After honey extraction, perform quality test and packaging in parallel
root.order.add_edge(honey_extract, quality_test)
root.order.add_edge(honey_extract, packaging)

# Packaging can then proceed to market setup and sales report in parallel
root.order.add_edge(quality_test, packaging)
root.order.add_edge(packaging, market_setup)
root.order.add_edge(packaging, sales_report)

# After market setup, perform regulation check and waste manage in parallel
root.order.add_edge(market_setup, regulation_check)
root.order.add_edge(market_setup, waste_manage)

# Finally, seasonal review is always the last step
root.order.add_edge(regulation_check, seasonal_review)
root.order.add_edge(waste_manage, seasonal_review)

# Optionally, add a loop for continuous seasonal review
# (this is optional and not shown in the initial process description)
# loop = OperatorPOWL(operator=Operator.LOOP, children=[seasonal_review, seasonal_review])
# root.order.add_edge(seasonal_review, loop)
# root.order.add_edge(loop, seasonal_review)

# The root of the process is now defined as 'root'