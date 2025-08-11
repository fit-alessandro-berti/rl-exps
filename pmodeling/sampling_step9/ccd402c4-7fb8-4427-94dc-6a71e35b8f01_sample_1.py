import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define silent transitions
skip = SilentTransition()

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, energy_plan, maintenance_plan])
xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, permit_filing, stakeholder_meet, design_layout, iot_install, sensor_calibrate, hydroponic_setup, nutrient_mix, seed_sowing, climate_control, data_monitor, loop])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[harvest_prep, supply_dispatch, market_launch])
root = StrictPartialOrder(nodes=[xor, xor2])
root.order.add_edge(xor, xor2)

# Print the root POWL model
print(root)