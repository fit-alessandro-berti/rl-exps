import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the urban vertical farm process
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

skip = SilentTransition()

# Define the process steps
site_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[impact_review, skip])
modular_design_choice = OperatorPOWL(operator=Operator.XOR, children=[system_integration, skip])
climate_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
light_config_choice = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
pest_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[drone_deploy, skip])
health_scan_choice = OperatorPOWL(operator=Operator.XOR, children=[data_logging, skip])
supply_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, skip])
waste_manage_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[site_analysis, impact_review, modular_design, system_integration, climate_setup, nutrient_mix, light_config, staff_training, pest_monitor, drone_deploy, health_scan, data_logging, supply_sync, maintenance_plan, waste_manage])
root.order.add_edge(site_analysis, modular_design_choice)
root.order.add_edge(site_analysis, climate_setup_choice)
root.order.add_edge(modular_design, modular_design_choice)
root.order.add_edge(system_integration, modular_design_choice)
root.order.add_edge(climate_setup, climate_setup_choice)
root.order.add_edge(nutrient_mix, climate_setup_choice)
root.order.add_edge(light_config, light_config_choice)
root.order.add_edge(staff_training, light_config_choice)
root.order.add_edge(pest_monitor, pest_monitor_choice)
root.order.add_edge(drone_deploy, pest_monitor_choice)
root.order.add_edge(health_scan, health_scan_choice)
root.order.add_edge(data_logging, health_scan_choice)
root.order.add_edge(supply_sync, supply_sync_choice)
root.order.add_edge(maintenance_plan, supply_sync_choice)
root.order.add_edge(waste_manage, waste_manage_choice)