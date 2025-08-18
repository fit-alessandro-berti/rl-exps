import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
stakeholder_meet = Transition(label='Stakeholder Meet')
design_layout = Transition(label='Design Layout')
iot_install = Transition(label='IoT Install')
sensor_calibrate = Transition(label='Sensor Calibrate')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_sowing = Transition(label='Seed Sowing')
climate_control = Transition(label='Climate Control')
data_monitor = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_plan = Transition(label='Energy Plan')
maintenance_plan = Transition(label='Maintenance Plan')
harvest_prep = Transition(label='Harvest Prep')
supply_dispatch = Transition(label='Supply Dispatch')
market_launch = Transition(label='Market Launch')

# Define exclusive choice for IoT Install and Sensor Calibrate
xor_iot_sensor = OperatorPOWL(operator=Operator.XOR, children=[iot_install, sensor_calibrate])

# Define loop for Hydroponic Setup and Nutrient Mix
loop_hydro_nutrient = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, nutrient_mix])

# Define loop for Seed Sowing and Climate Control
loop_seed_control = OperatorPOWL(operator=Operator.LOOP, children=[seed_sowing, climate_control])

# Define loop for Data Monitor and Yield Forecast
loop_data_forecast = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, yield_forecast])

# Define loop for Energy Plan and Maintenance Plan
loop_energy_maintenance = OperatorPOWL(operator=Operator.LOOP, children=[energy_plan, maintenance_plan])

# Define loop for Harvest Prep and Supply Dispatch
loop_harvest_supply = OperatorPOWL(operator=Operator.LOOP, children=[harvest_prep, supply_dispatch])

# Define loop for Market Launch
loop_market_launch = OperatorPOWL(operator=Operator.LOOP, children=[market_launch])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    stakeholder_meet,
    design_layout,
    xor_iot_sensor,
    loop_hydro_nutrient,
    loop_seed_control,
    loop_data_forecast,
    loop_energy_maintenance,
    loop_harvest_supply,
    loop_market_launch
])