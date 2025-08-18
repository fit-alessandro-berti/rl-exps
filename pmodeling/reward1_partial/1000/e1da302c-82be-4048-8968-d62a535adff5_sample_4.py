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

# Define the control-flow operators
# Colony Sourcing
root = StrictPartialOrder(nodes=[colony_sourcing])
# Hive Design
root.order.add_edge(colony_sourcing, hive_design)
# Site Survey
root.order.add_edge(hive_design, site_survey)
# Installation Prep
root.order.add_edge(site_survey, installation_prep)
# Hive Setup
root.order.add_edge(installation_prep, hive_setup)
# Sensor Install
root.order.add_edge(hive_setup, sensor_install)
# Health Monitor
root.order.add_edge(sensor_install, health_monitor)
# Pest Control
root.order.add_edge(health_monitor, pest_control)
# Honey Harvest
root.order.add_edge(pest_control, honey_harvest)
# Wax Processing
root.order.add_edge(honey_harvest, wax_processing)
# Product Packaging
root.order.add_edge(wax_processing, product_packaging)
# Order Dispatch
root.order.add_edge(product_packaging, order_dispatch)
# Workshop Setup
root.order.add_edge(order_dispatch, workshop_setup)
# Community Outreach
root.order.add_edge(workshop_setup, community_outreach)
# Regulation Check
root.order.add_edge(community_outreach, regulation_check)
# Data Analysis
root.order.add_edge(regulation_check, data_analysis)
# Maintenance Plan
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive_setup)
# Hive Setup
root.order.add_edge(hive_setup, sensor_install)
# Sensor Install
root.order.add_edge(sensor_install, health_monitor)
# Health Monitor
root.order.add_edge(health_monitor, pest_control)
# Pest Control
root.order.add_edge(pest_control, honey_harvest)
# Honey Harvest
root.order.add_edge(honey_harvest, wax_processing)
# Wax Processing
root.order.add_edge(wax_processing, product_packaging)
# Product Packaging
root.order.add_edge(product_packaging, order_dispatch)
# Order Dispatch
root.order.add_edge(order_dispatch, workshop_setup)
# Workshop Setup
root.order.add_edge(workshop_setup, community_outreach)
# Community Outreach
root.order.add_edge(community_outreach, regulation_check)
# Regulation Check
root.order.add_edge(regulation_check, data_analysis)
# Data Analysis
root.order.add_edge(data_analysis, maintenance_plan)

# Define the control-flow operators
# Colony Sourcing
root.order.add_edge(colony_sourcing, hive_design)
# Hive Design
root.order.add_edge(hive_design, site_survey)
# Site Survey
root.order.add_edge(site_survey, installation_prep)
# Installation Prep
root.order.add_edge(installation_prep, hive