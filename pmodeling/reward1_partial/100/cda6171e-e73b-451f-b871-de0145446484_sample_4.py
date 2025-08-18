from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
modify_layout = Transition(label='Modify Layout')
install_hvac = Transition(label='Install HVAC')
setup_hydroponics = Transition(label='Setup Hydroponics')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds = Transition(label='Select Seeds')
automate_planting = Transition(label='Automate Planting')
deploy_sensors = Transition(label='Deploy Sensors')
pest_control = Transition(label='Pest Control')
optimize_energy = Transition(label='Optimize Energy')
recycle_water = Transition(label='Recycle Water')
automate_harvest = Transition(label='Automate Harvest')
package_crops = Transition(label='Package Crops')
coordinate_delivery = Transition(label='Coordinate Delivery')
analyze_data = Transition(label='Analyze Data')

skip = SilentTransition()

site_analysis_xor_structure = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, structure_check])
modify_layout_xor_hvac = OperatorPOWL(operator=Operator.XOR, children=[modify_layout, install_hvac])
setup_hydroponics_xor_nutrients = OperatorPOWL(operator=Operator.XOR, children=[setup_hydroponics, prepare_nutrients])
select_seeds_xor_planting = OperatorPOWL(operator=Operator.XOR, children=[select_seeds, automate_planting])
deploy_sensors_xor_pest_control = OperatorPOWL(operator=Operator.XOR, children=[deploy_sensors, pest_control])
optimize_energy_xor_water_recycle = OperatorPOWL(operator=Operator.XOR, children=[optimize_energy, recycle_water])
automate_harvest_xor_package = OperatorPOWL(operator=Operator.XOR, children=[automate_harvest, package_crops])
coordinate_delivery_xor_analyze_data = OperatorPOWL(operator=Operator.XOR, children=[coordinate_delivery, analyze_data])

root = StrictPartialOrder(nodes=[
    site_analysis_xor_structure,
    modify_layout_xor_hvac,
    setup_hydroponics_xor_nutrients,
    select_seeds_xor_planting,
    deploy_sensors_xor_pest_control,
    optimize_energy_xor_water_recycle,
    automate_harvest_xor_package,
    coordinate_delivery_xor_analyze_data
])

root.order.add_edge(site_analysis_xor_structure, modify_layout_xor_hvac)
root.order.add_edge(modify_layout_xor_hvac, setup_hydroponics_xor_nutrients)
root.order.add_edge(setup_hydroponics_xor_nutrients, select_seeds_xor_planting)
root.order.add_edge(select_seeds_xor_planting, deploy_sensors_xor_pest_control)
root.order.add_edge(deploy_sensors_xor_pest_control, optimize_energy_xor_water_recycle)
root.order.add_edge(optimize_energy_xor_water_recycle, automate_harvest_xor_package)
root.order.add_edge(automate_harvest_xor_package, coordinate_delivery_xor_analyze_data)