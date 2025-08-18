import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[colony_sourcing, hive_design, site_survey, installation_prep, hive_setup, sensor_install, health_monitor, pest_control, honey_harvest, wax_processing, product_packaging, order_dispatch, workshop_setup, community_outreach, regulation_check, data_analysis, maintenance_plan])

# Add dependencies between nodes
root.order.add_edge(colony_sourcing, hive_design)
root.order.add_edge(hive_design, site_survey)
root.order.add_edge(site_survey, installation_prep)
root.order.add_edge(installation_prep, hive_setup)
root.order.add_edge(hive_setup, sensor_install)
root.order.add_edge(sensor_install, health_monitor)
root.order.add_edge(health_monitor, pest_control)
root.order.add_edge(pest_control, honey_harvest)
root.order.add_edge(honey_harvest, wax_processing)
root.order.add_edge(wax_processing, product_packaging)
root.order.add_edge(product_packaging, order_dispatch)
root.order.add_edge(order_dispatch, workshop_setup)
root.order.add_edge(workshop_setup, community_outreach)
root.order.add_edge(community_outreach, regulation_check)
root.order.add_edge(regulation_check, data_analysis)
root.order.add_edge(data_analysis, maintenance_plan)

# Print the root of the POWL model
print(root)