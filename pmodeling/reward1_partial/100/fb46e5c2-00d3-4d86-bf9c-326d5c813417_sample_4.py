from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
impact_review = Transition(label='Impact Review')
modular_design = Transition(label='Modular Design')
system_integration = Transition(label='System Integration')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
light_config = Transition(label='Light Config')
staff_training = Transition(label='Staff Training')
pest_monitor = Transition(label='Pest Monitor')
drone_deploy = Transition(label='Drone Deploy')
health_scan = Transition(label='Health Scan')
data_logging = Transition(label='Data Logging')
supply_sync = Transition(label='Supply Sync')
maintenance_plan = Transition(label='Maintenance Plan')
waste_manage = Transition(label='Waste Manage')

# Define partial order for each activity
site_analysis_order = StrictPartialOrder(nodes=[site_analysis, impact_review])
modular_design_order = StrictPartialOrder(nodes=[modular_design, system_integration])
climate_setup_order = StrictPartialOrder(nodes=[climate_setup, nutrient_mix, light_config])
staff_training_order = StrictPartialOrder(nodes=[staff_training])
pest_monitor_order = StrictPartialOrder(nodes=[pest_monitor, drone_deploy])
health_scan_order = StrictPartialOrder(nodes=[health_scan, data_logging])
supply_sync_order = StrictPartialOrder(nodes=[supply_sync])
maintenance_plan_order = StrictPartialOrder(nodes=[maintenance_plan])
waste_manage_order = StrictPartialOrder(nodes=[waste_manage])

# Define loops for pest monitoring and health scanning
pest_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, drone_deploy])
health_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_scan, data_logging])

# Define exclusive choices for system integration and staff training
system_integration_choice = OperatorPOWL(operator=Operator.XOR, children=[system_integration, staff_training])

# Define the root partial order with all the nodes and dependencies
root = StrictPartialOrder(nodes=[site_analysis, impact_review, modular_design, system_integration_choice, climate_setup, nutrient_mix, light_config, staff_training, pest_monitor_loop, health_scan_loop, supply_sync, maintenance_plan, waste_manage])
root.order.add_edge(site_analysis, impact_review)
root.order.add_edge(modular_design, system_integration_choice)
root.order.add_edge(system_integration_choice, pest_monitor_loop)
root.order.add_edge(system_integration_choice, health_scan_loop)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(climate_setup, light_config)
root.order.add_edge(pest_monitor_loop, drone_deploy)
root.order.add_edge(health_scan_loop, data_logging)
root.order.add_edge(system_integration_choice, supply_sync)
root.order.add_edge(system_integration_choice, maintenance_plan)
root.order.add_edge(system_integration_choice, waste_manage)