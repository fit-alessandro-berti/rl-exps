import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
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

# Define the POWL model
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_filing, stakeholder_meet])
loop_design_layout = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, iot_install, sensor_calibrate])
loop_hydroponic_setup = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, nutrient_mix, seed_sowing, climate_control, data_monitor])
loop_yield_forecast = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, energy_plan, maintenance_plan])
loop_supply_dispatch = OperatorPOWL(operator=Operator.LOOP, children=[supply_dispatch, market_launch])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[loop_site_survey, loop_design_layout, loop_hydroponic_setup, loop_yield_forecast, loop_supply_dispatch])
root.order.add_edge(loop_site_survey, loop_design_layout)
root.order.add_edge(loop_design_layout, loop_hydroponic_setup)
root.order.add_edge(loop_hydroponic_setup, loop_yield_forecast)
root.order.add_edge(loop_yield_forecast, loop_supply_dispatch)

# Print the root POWL model
print(root)