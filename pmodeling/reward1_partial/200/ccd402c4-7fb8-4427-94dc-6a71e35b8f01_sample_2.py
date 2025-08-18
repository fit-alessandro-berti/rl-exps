from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the loop for the IoT install and sensor calibrate
iot_loop = OperatorPOWL(operator=Operator.LOOP, children=[iot_install, sensor_calibrate])

# Define the exclusive choice for the nutrient mix and seed sowing
nutrient_seed_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_sowing])

# Define the exclusive choice for the climate control and data monitor
climate_data_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_control, data_monitor])

# Define the exclusive choice for the yield forecast and energy plan
yield_energy_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, energy_plan])

# Define the exclusive choice for the maintenance plan and harvest prep
maintenance_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, harvest_prep])

# Define the exclusive choice for the supply dispatch and market launch
supply_market_choice = OperatorPOWL(operator=Operator.XOR, children=[supply_dispatch, market_launch])

# Define the root node with the defined nodes and order
root = StrictPartialOrder(nodes=[site_survey, permit_filing, stakeholder_meet, design_layout, iot_loop, nutrient_seed_choice, climate_data_choice, yield_energy_choice, maintenance_harvest_choice, supply_market_choice])
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(permit_filing, iot_loop)
root.order.add_edge(stakeholder_meet, nutrient_seed_choice)
root.order.add_edge(design_layout, climate_data_choice)
root.order.add_edge(iot_loop, yield_energy_choice)
root.order.add_edge(nutrient_seed_choice, maintenance_harvest_choice)
root.order.add_edge(climate_data_choice, supply_market_choice)