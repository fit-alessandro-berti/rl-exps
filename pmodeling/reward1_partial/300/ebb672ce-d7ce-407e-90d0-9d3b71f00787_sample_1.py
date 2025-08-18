from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
modular_build = Transition(label='Modular Build')
install_pumps = Transition(label='Install Pumps')
setup_sensors = Transition(label='Setup Sensors')
calibrate_lights = Transition(label='Calibrate Lights')
nutrient_mix = Transition(label='Nutrient Mix')
plant_seeding = Transition(label='Plant Seeding')
water_cycling = Transition(label='Water Cycling')
energy_audit = Transition(label='Energy Audit')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')
supply_order = Transition(label='Supply Order')
waste_recycle = Transition(label='Waste Recycle')
system_upgrade = Transition(label='System Upgrade')

skip = SilentTransition()

site_survey_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
design_layout_to_modular_build = OperatorPOWL(operator=Operator.XOR, children=[modular_build, skip])
modular_build_to_install_pumps = OperatorPOWL(operator=Operator.XOR, children=[install_pumps, skip])
install_pumps_to_setup_sensors = OperatorPOWL(operator=Operator.XOR, children=[setup_sensors, skip])
setup_sensors_to_calibrate_lights = OperatorPOWL(operator=Operator.XOR, children=[calibrate_lights, skip])
calibrate_lights_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
nutrient_mix_to_plant_seeding = OperatorPOWL(operator=Operator.XOR, children=[plant_seeding, skip])
plant_seeding_to_water_cycling = OperatorPOWL(operator=Operator.XOR, children=[water_cycling, skip])
water_cycling_to_energy_audit = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
energy_audit_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
pest_control_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])
growth_monitor_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])
data_analysis_to_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])
yield_forecast_to_supply_order = OperatorPOWL(operator=Operator.XOR, children=[supply_order, skip])
supply_order_to_waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, skip])
waste_recycle_to_system_upgrade = OperatorPOWL(operator=Operator.XOR, children=[system_upgrade, skip])

root = StrictPartialOrder(nodes=[
    site_survey_to_design_layout,
    design_layout_to_modular_build,
    modular_build_to_install_pumps,
    install_pumps_to_setup_sensors,
    setup_sensors_to_calibrate_lights,
    calibrate_lights_to_nutrient_mix,
    nutrient_mix_to_plant_seeding,
    plant_seeding_to_water_cycling,
    water_cycling_to_energy_audit,
    energy_audit_to_pest_control,
    pest_control_to_growth_monitor,
    growth_monitor_to_data_analysis,
    data_analysis_to_yield_forecast,
    yield_forecast_to_supply_order,
    supply_order_to_waste_recycle,
    waste_recycle_to_system_upgrade
])

root.order.add_edge(site_survey_to_design_layout, design_layout_to_modular_build)
root.order.add_edge(design_layout_to_modular_build, modular_build_to_install_pumps)
root.order.add_edge(modular_build_to_install_pumps, install_pumps_to_setup_sensors)
root.order.add_edge(install_pumps_to_setup_sensors, setup_sensors_to_calibrate_lights)
root.order.add_edge(setup_sensors_to_calibrate_lights, calibrate_lights_to_nutrient_mix)
root.order.add_edge(calibrate_lights_to_nutrient_mix, nutrient_mix_to_plant_seeding)
root.order.add_edge(nutrient_mix_to_plant_seeding, plant_seeding_to_water_cycling)
root.order.add_edge(plant_seeding_to_water_cycling, water_cycling_to_energy_audit)
root.order.add_edge(water_cycling_to_energy_audit, energy_audit_to_pest_control)
root.order.add_edge(energy_audit_to_pest_control, pest_control_to_growth_monitor)
root.order.add_edge(pest_control_to_growth_monitor, growth_monitor_to_data_analysis)
root.order.add_edge(growth_monitor_to_data_analysis, data_analysis_to_yield_forecast)
root.order.add_edge(data_analysis_to_yield_forecast, yield_forecast_to_supply_order)
root.order.add_edge(yield_forecast_to_supply_order, supply_order_to_waste_recycle)
root.order.add_edge(supply_order_to_waste_recycle, waste_recycle_to_system_upgrade)