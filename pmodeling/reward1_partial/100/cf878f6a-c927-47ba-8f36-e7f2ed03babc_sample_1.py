import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for non-executed steps
skip = SilentTransition()

# Define sub-processes
site_zoning = OperatorPOWL(operator=Operator.XOR, children=[site_assess, zoning_check])
design_install = OperatorPOWL(operator=Operator.XOR, children=[design_farm, procure_gear])
sensor_systems = OperatorPOWL(operator=Operator.XOR, children=[install_systems, setup_sensors])
crop_selection = OperatorPOWL(operator=Operator.XOR, children=[select_crops, skip])
seed_mix = OperatorPOWL(operator=Operator.XOR, children=[prepare_seeds, mix_nutrients])
growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, adjust_climate])
harvest_assist = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, skip])
quality_grade = OperatorPOWL(operator=Operator.XOR, children=[grade_quality, skip])
produce_pack = OperatorPOWL(operator=Operator.XOR, children=[pack_produce, skip])
logistics_manage = OperatorPOWL(operator=Operator.XOR, children=[manage_logistics, skip])
market_products = OperatorPOWL(operator=Operator.XOR, children=[market_products, skip])
waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, skip])
system_audit = OperatorPOWL(operator=Operator.XOR, children=[audit_systems, skip])

# Define the root process
root = StrictPartialOrder(nodes=[site_zoning, design_install, sensor_systems, crop_selection, seed_mix, growth_monitor, harvest_assist, quality_grade, produce_pack, logistics_manage, market_products, waste_recycle, system_audit])
root.order.add_edge(site_zoning, design_install)
root.order.add_edge(design_install, sensor_systems)
root.order.add_edge(sensor_systems, crop_selection)
root.order.add_edge(crop_selection, seed_mix)
root.order.add_edge(seed_mix, growth_monitor)
root.order.add_edge(growth_monitor, harvest_assist)
root.order.add_edge(harvest_assist, quality_grade)
root.order.add_edge(quality_grade, produce_pack)
root.order.add_edge(produce_pack, logistics_manage)
root.order.add_edge(logistics_manage, market_products)
root.order.add_edge(market_products, waste_recycle)
root.order.add_edge(waste_recycle, system_audit)

print(root)