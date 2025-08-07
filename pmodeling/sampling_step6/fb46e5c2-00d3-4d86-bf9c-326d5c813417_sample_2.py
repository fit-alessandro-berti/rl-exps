import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    site_analysis, impact_review, modular_design, system_integration,
    climate_setup, nutrient_mix, light_config, staff_training,
    pest_monitor, drone_deploy, health_scan, data_logging, supply_sync,
    maintenance_plan, waste_manage
])

# Define dependencies between activities (if any)
# In this case, there are no direct dependencies between activities, so we don't need to define any edges.

# Now 'root' contains the POWL model for the urban vertical farm process.