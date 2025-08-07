import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names
site_analysis = Transition(label='Site Analysis')
env_assessment = Transition(label='Env Assessment')
system_design = Transition(label='System Design')
equipment_order = Transition(label='Equipment Order')
seed_selection = Transition(label='Seed Selection')
install_modules = Transition(label='Install Modules')
calibrate_systems = Transition(label='Calibrate Systems')
staff_training = Transition(label='Staff Training')
plant_seeding = Transition(label='Plant Seeding')
iot_monitoring = Transition(label='IoT Monitoring')
data_analytics = Transition(label='Data Analytics')
nutrient_adjust = Transition(label='Nutrient Adjust')
pest_control = Transition(label='Pest Control')
maintenance_check = Transition(label='Maintenance Check')
market_launch = Transition(label='Market Launch')
logistics_setup = Transition(label='Logistics Setup')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_assessment,
    system_design,
    equipment_order,
    seed_selection,
    install_modules,
    calibrate_systems,
    staff_training,
    plant_seeding,
    iot_monitoring,
    data_analytics,
    nutrient_adjust,
    pest_control,
    maintenance_check,
    market_launch,
    logistics_setup
])

# Add dependencies if needed (if any)
# Example: Add dependency from 'Site Analysis' to 'Env Assessment'
root.order.add_edge(site_analysis, env_assessment)

# Now, 'root' contains the POWL model for the described process