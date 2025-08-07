import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_assess     = Transition(label='Site Assess')
plan_layout     = Transition(label='Plan Layout')
install_racks   = Transition(label='Install Racks')
mix_nutrients   = Transition(label='Mix Nutrients')
calibrate_sensors = Transition(label='Calibrate Sensors')
setup_lighting  = Transition(label='Setup Lighting')
configure_climate = Transition(label='Configure Climate')
select_seeds    = Transition(label='Select Seeds')
monitor_germinate = Transition(label='Monitor Germinate')
apply_biocontrols = Transition(label='Apply Bio-controls')
maintain_systems = Transition(label='Maintain Systems')
analyze_data    = Transition(label='Analyze Data')
harvest_crops   = Transition(label='Harvest Crops')
quality_check   = Transition(label='Quality Check')
package_produce = Transition(label='Package Produce')
distribute_goods = Transition(label='Distribute Goods')

# Define the maintenance loop: repeat system maintenance until exit
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintain_systems, analyze_data]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    plan_layout,
    install_racks,
    mix_nutrients,
    calibrate_sensors,
    setup_lighting,
    configure_climate,
    select_seeds,
    monitor_germinate,
    apply_biocontrols,
    maintenance_loop,
    harvest_crops,
    quality_check,
    package_produce,
    distribute_goods
])

# Sequential ordering
root.order.add_edge(site_assess, plan_layout)
root.order.add_edge(plan_layout, install_racks)
root.order.add_edge(install_racks, mix_nutrients)
root.order.add_edge(mix_nutrients, calibrate_sensors)
root.order.add_edge(calibrate_sensors, setup_lighting)
root.order.add_edge(setup_lighting, configure_climate)
root.order.add_edge(configure_climate, select_seeds)
root.order.add_edge(select_seeds, monitor_germinate)
root.order.add_edge(monitor_germinate, apply_biocontrols)
root.order.add_edge(apply_biocontrols, maintenance_loop)

# Maintenance loop follows both germination and bio-control applications
root.order.add_edge(maintenance_loop, harvest_crops)

# Harvesting precedes quality check and packaging
root.order.add_edge(harvest_crops, quality_check)
root.order.add_edge(harvest_crops, package_produce)

# Quality check precedes distribution
root.order.add_edge(quality_check, distribute_goods)

# Packaging precedes distribution
root.order.add_edge(package_produce, distribute_goods)