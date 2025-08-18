import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_assess = Transition(label='Site Assess')
plan_layout = Transition(label='Plan Layout')
install_racks = Transition(label='Install Racks')
mix_nutrients = Transition(label='Mix Nutrients')
calibrate_sensors = Transition(label='Calibrate Sensors')
setup_lighting = Transition(label='Setup Lighting')
configure_climate = Transition(label='Configure Climate')
select_seeds = Transition(label='Select Seeds')
monitor_germinate = Transition(label='Monitor Germinate')
apply_bio_controls = Transition(label='Apply Bio-controls')
maintain_systems = Transition(label='Maintain Systems')
analyze_data = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
quality_check = Transition(label='Quality Check')
package_produce = Transition(label='Package Produce')
distribute_goods = Transition(label='Distribute Goods')

skip = SilentTransition()

site_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_assess, plan_layout])
rack_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_racks, mix_nutrients, calibrate_sensors])
lighting_climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[setup_lighting, configure_climate])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[select_seeds, monitor_germinate, apply_bio_controls])
system_maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintain_systems])
data_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[analyze_data])
crop_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crops, quality_check, package_produce, distribute_goods])

root = StrictPartialOrder(nodes=[
    site_assess_loop,
    rack_install_loop,
    lighting_climate_loop,
    seed_selection_loop,
    system_maintenance_loop,
    data_analysis_loop,
    crop_harvest_loop
])

root.order.add_edge(site_assess_loop, rack_install_loop)
root.order.add_edge(rack_install_loop, lighting_climate_loop)
root.order.add_edge(lighting_climate_loop, seed_selection_loop)
root.order.add_edge(seed_selection_loop, system_maintenance_loop)
root.order.add_edge(system_maintenance_loop, data_analysis_loop)
root.order.add_edge(data_analysis_loop, crop_harvest_loop)