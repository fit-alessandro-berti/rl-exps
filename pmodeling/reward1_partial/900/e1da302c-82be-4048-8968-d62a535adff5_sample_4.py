import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
colony_sourcing = Transition(label='Colony Sourcing')
hive_design = Transition(label='Hive Design')
site_survey = Transition(label='Site Survey')
installation_prep = Transition(label='Installation Prep')
hive_setup = Transition(label='Hive Setup')
sensor_install = Transition(label='Sensor Install')
health_monitor = Transition(label='Health Monitor')
pest_control = Transition(label='Pest Control')
honey_harvest = Transition(label='Honey Harvest')
wax_processing = Transition(label='Wax Processing')
product_packaging = Transition(label='Product Packaging')
order_dispatch = Transition(label='Order Dispatch')
workshop_setup = Transition(label='Workshop Setup')
community_outreach = Transition(label='Community Outreach')
regulation_check = Transition(label='Regulation Check')
data_analysis = Transition(label='Data Analysis')
maintenance_plan = Transition(label='Maintenance Plan')

# Define partial order nodes
sourcing_node = StrictPartialOrder(nodes=[colony_sourcing, hive_design, site_survey, installation_prep, hive_setup, sensor_install, health_monitor, pest_control, honey_harvest, wax_processing])
monitoring_node = StrictPartialOrder(nodes=[health_monitor, pest_control])
harvesting_node = StrictPartialOrder(nodes=[honey_harvest])
processing_node = StrictPartialOrder(nodes=[wax_processing])
packaging_node = StrictPartialOrder(nodes=[product_packaging])
dispatch_node = StrictPartialOrder(nodes=[order_dispatch])
workshop_node = StrictPartialOrder(nodes=[workshop_setup, community_outreach])
regulation_node = StrictPartialOrder(nodes=[regulation_check])
analysis_node = StrictPartialOrder(nodes=[data_analysis])
maintenance_node = StrictPartialOrder(nodes=[maintenance_plan])

# Define dependencies
sourcing_node.order.add_edge(colony_sourcing, hive_design)
sourcing_node.order.add_edge(hive_design, site_survey)
sourcing_node.order.add_edge(site_survey, installation_prep)
sourcing_node.order.add_edge(installation_prep, hive_setup)
sourcing_node.order.add_edge(hive_setup, sensor_install)
sourcing_node.order.add_edge(sensor_install, health_monitor)
sourcing_node.order.add_edge(health_monitor, pest_control)
sourcing_node.order.add_edge(pest_control, honey_harvest)
sourcing_node.order.add_edge(honey_harvest, wax_processing)
sourcing_node.order.add_edge(wax_processing, product_packaging)
sourcing_node.order.add_edge(product_packaging, order_dispatch)

monitoring_node.order.add_edge(health_monitor, pest_control)

harvesting_node.order.add_edge(honey_harvest, wax_processing)

processing_node.order.add_edge(wax_processing, product_packaging)

packaging_node.order.add_edge(product_packaging, order_dispatch)

dispatch_node.order.add_edge(order_dispatch, workshop_setup)
dispatch_node.order.add_edge(order_dispatch, community_outreach)

workshop_node.order.add_edge(workshop_setup, community_outreach)

regulation_node.order.add_edge(regulation_check, data_analysis)

analysis_node.order.add_edge(data_analysis, maintenance_plan)

maintenance_node.order.add_edge(maintenance_plan, colony_sourcing)

# Define root node
root = StrictPartialOrder(nodes=[sourcing_node, monitoring_node, harvesting_node, processing_node, packaging_node, dispatch_node, workshop_node, regulation_node, analysis_node, maintenance_node])