import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the relationships between activities
# Colony Sourcing
colony_sourcing_out = [hive_design]
colony_sourcing_out.append(site_survey)
colony_sourcing_out.append(installation_prep)

# Hive Design
hive_design_out = [hive_setup]
hive_design_out.append(sensor_install)

# Site Survey
site_survey_out = [hive_setup]

# Installation Prep
installation_prep_out = [hive_setup]

# Hive Setup
hive_setup_out = [health_monitor]
hive_setup_out.append(pest_control)

# Sensor Install
sensor_install_out = [health_monitor]

# Health Monitor
health_monitor_out = [pest_control]

# Pest Control
pest_control_out = [honey_harvest]
pest_control_out.append(wax_processing)

# Honey Harvest
honey_harvest_out = [product_packaging]
honey_harvest_out.append(order_dispatch)

# Wax Processing
wax_processing_out = [product_packaging]

# Product Packaging
product_packaging_out = [order_dispatch]
product_packaging_out.append(workshop_setup)

# Order Dispatch
order_dispatch_out = [workshop_setup]

# Workshop Setup
workshop_setup_out = [community_outreach]
workshop_setup_out.append(regulation_check)

# Community Outreach
community_outreach_out = [regulation_check]

# Regulation Check
regulation_check_out = [data_analysis]

# Data Analysis
data_analysis_out = [maintenance_plan]

# Maintenance Plan
maintenance_plan_out = [data_analysis]

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    colony_sourcing,
    hive_design,
    site_survey,
    installation_prep,
    hive_setup,
    sensor_install,
    health_monitor,
    pest_control,
    honey_harvest,
    wax_processing,
    product_packaging,
    order_dispatch,
    workshop_setup,
    community_outreach,
    regulation_check,
    data_analysis,
    maintenance_plan
])

# Define the dependencies between activities
root.order.add_edge(colony_sourcing, hive_design)
root.order.add_edge(colony_sourcing, site_survey)
root.order.add_edge(colony_sourcing, installation_prep)
root.order.add_edge(hive_design, hive_setup)
root.order.add_edge(hive_design, sensor_install)
root.order.add_edge(site_survey, hive_setup)
root.order.add_edge(installation_prep, hive_setup)
root.order.add_edge(hive_setup, health_monitor)
root.order.add_edge(hive_setup, pest_control)
root.order.add_edge(health_monitor, pest_control)
root.order.add_edge(pest_control, honey_harvest)
root.order.add_edge(pest_control, wax_processing)
root.order.add_edge(honey_harvest, product_packaging)
root.order.add_edge(honey_harvest, order_dispatch)
root.order.add_edge(wax_processing, product_packaging)
root.order.add_edge(product_packaging, order_dispatch)
root.order.add_edge(product_packaging, workshop_setup)
root.order.add_edge(order_dispatch, workshop_setup)
root.order.add_edge(workshop_setup, community_outreach)
root.order.add_edge(workshop_setup, regulation_check)
root.order.add_edge(community_outreach, regulation_check)
root.order.add_edge(regulation_check, data_analysis)
root.order.add_edge(data_analysis, maintenance_plan)

# Return the root POWL model
return root