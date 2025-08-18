import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loop for IoT Install, Sensor Calibrate, Hydroponic Setup, Nutrient Mix, Seed Sowing, Climate Control, Data Monitor, Yield Forecast, Energy Plan, and Maintenance Plan
iot_loop = OperatorPOWL(operator=Operator.LOOP, children=[iot_install, sensor_calibrate, hydroponic_setup, nutrient_mix, seed_sowing, climate_control, data_monitor, yield_forecast, energy_plan, maintenance_plan])

# Define the exclusive choice for Supply Dispatch and Market Launch
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[supply_dispatch, market_launch])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, permit_filing, stakeholder_meet, design_layout, iot_loop, exclusive_choice])
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, stakeholder_meet)
root.order.add_edge(stakeholder_meet, design_layout)
root.order.add_edge(design_layout, iot_loop)
root.order.add_edge(iot_loop, exclusive_choice)