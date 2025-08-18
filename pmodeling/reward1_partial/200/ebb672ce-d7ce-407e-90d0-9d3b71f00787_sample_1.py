from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        modular_build,
        install_pumps,
        setup_sensors,
        calibrate_lights,
        nutrient_mix,
        plant_seeding,
        water_cycling,
        energy_audit,
        pest_control,
        growth_monitor,
        data_analysis,
        yield_forecast,
        supply_order,
        waste_recycle,
        system_upgrade
    ],
    order={
        site_survey: [design_layout],
        design_layout: [modular_build],
        modular_build: [install_pumps, setup_sensors],
        install_pumps: [calibrate_lights],
        setup_sensors: [nutrient_mix],
        calibrate_lights: [plant_seeding],
        nutrient_mix: [water_cycling],
        plant_seeding: [energy_audit, pest_control],
        water_cycling: [growth_monitor],
        energy_audit: [supply_order, waste_recycle],
        pest_control: [system_upgrade],
        growth_monitor: [data_analysis],
        data_analysis: [yield_forecast]
    }
)

# Define the edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, modular_build)
root.order.add_edge(modular_build, install_pumps)
root.order.add_edge(modular_build, setup_sensors)
root.order.add_edge(install_pumps, calibrate_lights)
root.order.add_edge(setup_sensors, nutrient_mix)
root.order.add_edge(nutrient_mix, plant_seeding)
root.order.add_edge(plant_seeding, energy_audit)
root.order.add_edge(plant_seeding, pest_control)
root.order.add_edge(energy_audit, supply_order)
root.order.add_edge(energy_audit, waste_recycle)
root.order.add_edge(pest_control, system_upgrade)
root.order.add_edge(growth_monitor, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)

# Return the root node
print(root)