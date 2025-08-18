import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define process steps
sensor_installation = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, health_monitor, pest_control])
hive_setup_process = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, skip])
honey_harvest_process = OperatorPOWL(operator=Operator.XOR, children=[honey_harvest, skip])
wax_processing_process = OperatorPOWL(operator=Operator.XOR, children=[wax_processing, skip])
product_packaging_process = OperatorPOWL(operator=Operator.XOR, children=[product_packaging, skip])
order_dispatch_process = OperatorPOWL(operator=Operator.XOR, children=[order_dispatch, skip])
workshop_setup_process = OperatorPOWL(operator=Operator.XOR, children=[workshop_setup, skip])
community_outreach_process = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, skip])
regulation_check_process = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, skip])
data_analysis_process = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])
maintenance_plan_process = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, skip])

# Define the root process
root = StrictPartialOrder(nodes=[
    colony_sourcing, hive_design, site_survey, installation_prep, hive_setup_process, sensor_installation,
    honey_harvest_process, wax_processing_process, product_packaging_process, order_dispatch_process,
    workshop_setup_process, community_outreach_process, regulation_check_process, data_analysis_process,
    maintenance_plan_process
])

# Define dependencies
root.order.add_edge(colony_sourcing, hive_design)
root.order.add_edge(hive_design, site_survey)
root.order.add_edge(site_survey, installation_prep)
root.order.add_edge(installation_prep, hive_setup_process)
root.order.add_edge(hive_setup_process, sensor_installation)
root.order.add_edge(sensor_installation, health_monitor)
root.order.add_edge(health_monitor, pest_control)
root.order.add_edge(pest_control, honey_harvest_process)
root.order.add_edge(honey_harvest_process, wax_processing_process)
root.order.add_edge(wax_processing_process, product_packaging_process)
root.order.add_edge(product_packaging_process, order_dispatch_process)
root.order.add_edge(order_dispatch_process, workshop_setup_process)
root.order.add_edge(workshop_setup_process, community_outreach_process)
root.order.add_edge(community_outreach_process, regulation_check_process)
root.order.add_edge(regulation_check_process, data_analysis_process)
root.order.add_edge(data_analysis_process, maintenance_plan_process)

# Print the root POWL model
print(root)