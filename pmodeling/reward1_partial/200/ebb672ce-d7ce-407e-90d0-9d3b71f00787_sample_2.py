from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
modular_build_choice = OperatorPOWL(operator=Operator.XOR, children=[modular_build, skip])
install_pumps_choice = OperatorPOWL(operator=Operator.XOR, children=[install_pumps, skip])
setup_sensors_choice = OperatorPOWL(operator=Operator.XOR, children=[setup_sensors, skip])
calibrate_lights_choice = OperatorPOWL(operator=Operator.XOR, children=[calibrate_lights, skip])
nutrient_mix_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
plant_seeding_choice = OperatorPOWL(operator=Operator.XOR, children=[plant_seeding, skip])
water_cycling_choice = OperatorPOWL(operator=Operator.XOR, children=[water_cycling, skip])
energy_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
growth_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])
data_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])
yield_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])
supply_order_choice = OperatorPOWL(operator=Operator.XOR, children=[supply_order, skip])
waste_recycle_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, skip])
system_upgrade_choice = OperatorPOWL(operator=Operator.XOR, children=[system_upgrade, skip])

root = StrictPartialOrder(nodes=[
    site_survey_choice,
    modular_build_choice,
    install_pumps_choice,
    setup_sensors_choice,
    calibrate_lights_choice,
    nutrient_mix_choice,
    plant_seeding_choice,
    water_cycling_choice,
    energy_audit_choice,
    pest_control_choice,
    growth_monitor_choice,
    data_analysis_choice,
    yield_forecast_choice,
    supply_order_choice,
    waste_recycle_choice,
    system_upgrade_choice
])

root.order.add_edge(site_survey_choice, modular_build_choice)
root.order.add_edge(modular_build_choice, install_pumps_choice)
root.order.add_edge(install_pumps_choice, setup_sensors_choice)
root.order.add_edge(setup_sensors_choice, calibrate_lights_choice)
root.order.add_edge(calibrate_lights_choice, nutrient_mix_choice)
root.order.add_edge(nutrient_mix_choice, plant_seeding_choice)
root.order.add_edge(plant_seeding_choice, water_cycling_choice)
root.order.add_edge(water_cycling_choice, energy_audit_choice)
root.order.add_edge(energy_audit_choice, pest_control_choice)
root.order.add_edge(pest_control_choice, growth_monitor_choice)
root.order.add_edge(growth_monitor_choice, data_analysis_choice)
root.order.add_edge(data_analysis_choice, yield_forecast_choice)
root.order.add_edge(yield_forecast_choice, supply_order_choice)
root.order.add_edge(supply_order_choice, waste_recycle_choice)
root.order.add_edge(waste_recycle_choice, system_upgrade_choice)