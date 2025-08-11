import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop node for maintenance plan
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, skip])

# Define the exclusive choice for yield forecast
yield_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, permit_filing, stakeholder_meet, design_layout, iot_install, sensor_calibrate, hydroponic_setup, nutrient_mix, seed_sowing, climate_control, data_monitor, yield_forecast_choice, energy_plan, maintenance_loop, harvest_prep, supply_dispatch, market_launch])

# Define the dependencies between activities
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(permit_filing, iot_install)
root.order.add_edge(stakeholder_meet, design_layout)
root.order.add_edge(design_layout, iot_install)
root.order.add_edge(design_layout, sensor_calibrate)
root.order.add_edge(design_layout, hydroponic_setup)
root.order.add_edge(design_layout, nutrient_mix)
root.order.add_edge(design_layout, seed_sowing)
root.order.add_edge(design_layout, climate_control)
root.order.add_edge(design_layout, data_monitor)
root.order.add_edge(iot_install, sensor_calibrate)
root.order.add_edge(sensor_calibrate, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_sowing)
root.order.add_edge(seed_sowing, climate_control)
root.order.add_edge(climate_control, data_monitor)
root.order.add_edge(data_monitor, yield_forecast_choice)
root.order.add_edge(yield_forecast_choice, energy_plan)
root.order.add_edge(energy_plan, maintenance_loop)
root.order.add_edge(maintenance_loop, harvest_prep)
root.order.add_edge(harvest_prep, supply_dispatch)
root.order.add_edge(supply_dispatch, market_launch)

print(root)