import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis    = Transition(label='Site Analysis')
env_assessment   = Transition(label='Env Assessment')
system_design    = Transition(label='System Design')
equipment_order  = Transition(label='Equipment Order')
seed_selection   = Transition(label='Seed Selection')
install_modules  = Transition(label='Install Modules')
calibrate_systems= Transition(label='Calibrate Systems')
staff_training   = Transition(label='Staff Training')
plant_seeding    = Transition(label='Plant Seeding')
iot_monitoring   = Transition(label='IoT Monitoring')
data_analytics   = Transition(label='Data Analytics')
nutrient_adjust  = Transition(label='Nutrient Adjust')
pest_control     = Transition(label='Pest Control')
maintenance_check= Transition(label='Maintenance Check')
market_launch    = Transition(label='Market Launch')
logistics_setup  = Transition(label='Logistics Setup')

# Define the monitoring & optimization loop:
# A = IoT Monitoring -> Data Analytics -> Nutrient Adjust -> Pest Control
monitoring_po = StrictPartialOrder(nodes=[iot_monitoring, data_analytics, nutrient_adjust, pest_control])
monitoring_po.order.add_edge(iot_monitoring, data_analytics)
monitoring_po.order.add_edge(data_analytics, nutrient_adjust)
monitoring_po.order.add_edge(data_analytics, pest_control)

# B = Maintenance Check
maintenance_po = StrictPartialOrder(nodes=[maintenance_check])
# No edges, they are concurrent

# LOOP(A, B): IoT Monitoring -> Data Analytics -> Nutrient Adjust -> Pest Control,
# then optionally Maintenance Check and back to A
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_po, maintenance_po])

# Assemble the full process
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
    monitor_loop,
    market_launch,
    logistics_setup
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis, env_assessment)
root.order.add_edge(env_assessment, system_design)
root.order.add_edge(system_design, equipment_order)
root.order.add_edge(system_design, seed_selection)
root.order.add_edge(equipment_order, install_modules)
root.order.add_edge(seed_selection, install_modules)
root.order.add_edge(install_modules, calibrate_systems)
root.order.add_edge(calibrate_systems, staff_training)
root.order.add_edge(staff_training, plant_seeding)
root.order.add_edge(plant_seeding, monitor_loop)
root.order.add_edge(monitor_loop, market_launch)
root.order.add_edge(market_launch, logistics_setup)