import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Colony Sourcing', 'Hive Design', 'Site Survey', 'Installation Prep', 'Hive Setup', 'Sensor Install', 'Health Monitor', 'Pest Control', 'Honey Harvest', 'Wax Processing', 'Product Packaging', 'Order Dispatch', 'Workshop Setup', 'Community Outreach', 'Regulation Check', 'Data Analysis', 'Maintenance Plan']

# Create the POWL model
root = StrictPartialOrder()

# Add the activities as nodes
for activity in activities:
    root.add_node(Transition(label=activity))

# Define the process structure using POWL operators
colony_sourcing = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Colony Sourcing')])
hive_design = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Hive Design')])
site_survey = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Site Survey')])
installation_prep = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Installation Prep')])
hive_setup = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Hive Setup')])
sensor_install = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Sensor Install')])
health_monitor = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Health Monitor')])
pest_control = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Pest Control')])
honey_harvest = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Honey Harvest')])
wax_processing = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Wax Processing')])
product_packaging = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Product Packaging')])
order_dispatch = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Order Dispatch')])
workshop_setup = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Workshop Setup')])
community_outreach = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Community Outreach')])
regulation_check = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Regulation Check')])
data_analysis = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Data Analysis')])
maintenance_plan = OperatorPOWL(operator=Operator.CONCURRENT, children=[Transition(label='Maintenance Plan')])

# Add the nodes to the root
root.add_node(colony_sourcing)
root.add_node(hive_design)
root.add_node(site_survey)
root.add_node(installation_prep)
root.add_node(hive_setup)
root.add_node(sensor_install)
root.add_node(health_monitor)
root.add_node(pest_control)
root.add_node(honey_harvest)
root.add_node(wax_processing)
root.add_node(product_packaging)
root.add_node(order_dispatch)
root.add_node(workshop_setup)
root.add_node(community_outreach)
root.add_node(regulation_check)
root.add_node(data_analysis)
root.add_node(maintenance_plan)

# Define the dependencies
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