import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
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

# Define the partial order model
root = StrictPartialOrder(
    nodes=[site_survey, design_layout, modular_build, install_pumps, setup_sensors, calibrate_lights, nutrient_mix, 
           plant_seeding, water_cycling, energy_audit, pest_control, growth_monitor, data_analysis, yield_forecast, 
           supply_order, waste_recycle, system_upgrade],
    order={
        (site_survey, design_layout): None,
        (design_layout, modular_build): None,
        (modular_build, install_pumps): None,
        (install_pumps, setup_sensors): None,
        (setup_sensors, calibrate_lights): None,
        (calibrate_lights, nutrient_mix): None,
        (nutrient_mix, plant_seeding): None,
        (plant_seeding, water_cycling): None,
        (water_cycling, energy_audit): None,
        (energy_audit, pest_control): None,
        (pest_control, growth_monitor): None,
        (growth_monitor, data_analysis): None,
        (data_analysis, yield_forecast): None,
        (yield_forecast, supply_order): None,
        (supply_order, waste_recycle): None,
        (waste_recycle, system_upgrade): None
    }
)

# Print the model
print(root)