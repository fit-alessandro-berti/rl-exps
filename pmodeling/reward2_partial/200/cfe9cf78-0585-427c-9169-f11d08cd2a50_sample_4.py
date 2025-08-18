from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the dependencies
root.order.add_edge(site_analysis, env_assessment)
root.order.add_edge(env_assessment, system_design)
root.order.add_edge(system_design, equipment_order)
root.order.add_edge(equipment_order, seed_selection)
root.order.add_edge(seed_selection, install_modules)
root.order.add_edge(install_modules, calibrate_systems)
root.order.add_edge(calibrate_systems, staff_training)
root.order.add_edge(staff_training, plant_seeding)
root.order.add_edge(plant_seeding, iot_monitoring)
root.order.add_edge(iot_monitoring, data_analytics)
root.order.add_edge(data_analytics, nutrient_adjust)
root.order.add_edge(nutrient_adjust, pest_control)
root.order.add_edge(pest_control, maintenance_check)
root.order.add_edge(maintenance_check, market_launch)
root.order.add_edge(market_launch, logistics_setup)

print(root)