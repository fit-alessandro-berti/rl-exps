import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_assess = Transition(label='Site Assess')
zoning_check = Transition(label='Zoning Check')
design_farm = Transition(label='Design Farm')
procure_gear = Transition(label='Procure Gear')
install_systems = Transition(label='Install Systems')
setup_sensors = Transition(label='Setup Sensors')
select_crops = Transition(label='Select Crops')
prepare_seeds = Transition(label='Prepare Seeds')
mix_nutrients = Transition(label='Mix Nutrients')
monitor_growth = Transition(label='Monitor Growth')
adjust_climate = Transition(label='Adjust Climate')
robotic_harvest = Transition(label='Robotic Harvest')
grade_quality = Transition(label='Grade Quality')
pack_produce = Transition(label='Pack Produce')
manage_logistics = Transition(label='Manage Logistics')
market_products = Transition(label='Market Products')
recycle_waste = Transition(label='Recycle Waste')
audit_systems = Transition(label='Audit Systems')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_assess, zoning_check, design_farm, procure_gear, install_systems,
    setup_sensors, select_crops, prepare_seeds, mix_nutrients, monitor_growth,
    adjust_climate, robotic_harvest, grade_quality, pack_produce, manage_logistics,
    market_products, recycle_waste, audit_systems
])

# Define the order of execution
root.order.add_edge(site_assess, zoning_check)
root.order.add_edge(zoning_check, design_farm)
root.order.add_edge(design_farm, procure_gear)
root.order.add_edge(procure_gear, install_systems)
root.order.add_edge(install_systems, setup_sensors)
root.order.add_edge(setup_sensors, select_crops)
root.order.add_edge(select_crops, prepare_seeds)
root.order.add_edge(prepare_seeds, mix_nutrients)
root.order.add_edge(mix_nutrients, monitor_growth)
root.order.add_edge(monitor_growth, adjust_climate)
root.order.add_edge(adjust_climate, robotic_harvest)
root.order.add_edge(robotic_harvest, grade_quality)
root.order.add_edge(grade_quality, pack_produce)
root.order.add_edge(pack_produce, manage_logistics)
root.order.add_edge(manage_logistics, market_products)
root.order.add_edge(market_products, recycle_waste)
root.order.add_edge(recycle_waste, audit_systems)

# Print the root to verify
print(root)