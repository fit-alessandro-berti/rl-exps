import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop node for IoT Install
loop_iot = OperatorPOWL(operator=Operator.LOOP, children=[iot_install, sensor_calibrate])
# Define the loop node for Nutrient Mix
loop_nutrient = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
# Define the loop node for Seed Sowing
loop_seed = OperatorPOWL(operator=Operator.LOOP, children=[seed_sowing])
# Define the loop node for Climate Control
loop_climate = OperatorPOWL(operator=Operator.LOOP, children=[climate_control])
# Define the loop node for Data Monitor
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor])
# Define the loop node for Yield Forecast
loop_yield = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast])
# Define the loop node for Energy Plan
loop_energy = OperatorPOWL(operator=Operator.LOOP, children=[energy_plan])
# Define the loop node for Maintenance Plan
loop_maintenance = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan])
# Define the loop node for Harvest Prep
loop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[harvest_prep])
# Define the loop node for Supply Dispatch
loop_supply = OperatorPOWL(operator=Operator.LOOP, children=[supply_dispatch])
# Define the loop node for Market Launch
loop_market = OperatorPOWL(operator=Operator.LOOP, children=[market_launch])

# Define the exclusive choice nodes
xor_permit = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])
xor_stakeholder = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
xor_design = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
xor_iot = OperatorPOWL(operator=Operator.XOR, children=[loop_iot, skip])
xor_nutrient = OperatorPOWL(operator=Operator.XOR, children=[loop_nutrient, skip])
xor_seed = OperatorPOWL(operator=Operator.XOR, children=[loop_seed, skip])
xor_climate = OperatorPOWL(operator=Operator.XOR, children=[loop_climate, skip])
xor_data = OperatorPOWL(operator=Operator.XOR, children=[loop_data, skip])
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[loop_yield, skip])
xor_energy = OperatorPOWL(operator=Operator.XOR, children=[loop_energy, skip])
xor_maintenance = OperatorPOWL(operator=Operator.XOR, children=[loop_maintenance, skip])
xor_harvest = OperatorPOWL(operator=Operator.XOR, children=[loop_harvest, skip])
xor_supply = OperatorPOWL(operator=Operator.XOR, children=[loop_supply, skip])
xor_market = OperatorPOWL(operator=Operator.XOR, children=[loop_market, skip])

# Create the root node with all the nodes and their dependencies
root = StrictPartialOrder(nodes=[
    site_survey, permit_filing, stakeholder_meet, design_layout, iot_install, sensor_calibrate, hydroponic_setup, nutrient_mix, seed_sowing, climate_control, data_monitor, yield_forecast, energy_plan, maintenance_plan, harvest_prep, supply_dispatch, market_launch,
    xor_permit, xor_stakeholder, xor_design, xor_iot, xor_nutrient, xor_seed, xor_climate, xor_data, xor_yield, xor_energy, xor_maintenance, xor_harvest, xor_supply, xor_market
])

# Add dependencies between nodes
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(permit_filing, xor_permit)
root.order.add_edge(stakeholder_meet, xor_stakeholder)
root.order.add_edge(design_layout, xor_design)
root.order.add_edge(xor_permit, iot_install)
root.order.add_edge(xor_permit, sensor_calibrate)
root.order.add_edge(xor_stakeholder, hydroponic_setup)
root.order.add_edge(xor_stakeholder, nutrient_mix)
root.order.add_edge(xor_design, seed_sowing)
root.order.add_edge(xor_design, climate_control)
root.order.add_edge(xor_design, data_monitor)
root.order.add_edge(xor_design, yield_forecast)
root.order.add_edge(xor_design, energy_plan)
root.order.add_edge(xor_design, maintenance_plan)
root.order.add_edge(xor_design, harvest_prep)
root.order.add_edge(xor_design, supply_dispatch)
root.order.add_edge(xor_design, market_launch)
root.order.add_edge(iot_install, loop_iot)
root.order.add_edge(sensor_calibrate, loop_iot)
root.order.add_edge(hydroponic_setup, loop_nutrient)
root.order.add_edge(nutrient_mix, loop_nutrient)
root.order.add_edge(seed_sowing, loop_seed)
root.order.add_edge(climate_control, loop_climate)
root.order.add_edge(data_monitor, loop_data)
root.order.add_edge(yield_forecast, loop_yield)
root.order.add_edge(energy_plan, loop_energy)
root.order.add_edge(maintenance_plan, loop_maintenance)
root.order.add_edge(harvest_prep, loop_harvest)
root.order.add_edge(supply_dispatch, loop_supply)
root.order.add_edge(market_launch, loop_market)

# Print the root node
print(root)