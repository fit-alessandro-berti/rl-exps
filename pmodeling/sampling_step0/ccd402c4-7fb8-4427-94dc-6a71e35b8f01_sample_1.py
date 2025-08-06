import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loop nodes
iot_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate, iot_install])
hydroponic_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, seed_sowing])
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, data_monitor])
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, energy_plan])

# Define exclusive choice nodes
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[harvest_prep, supply_dispatch])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[market_launch, maintenance_plan])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, permit_filing, stakeholder_meet, design_layout, iot_loop, hydroponic_loop, climate_loop, maintenance_loop, exclusive_choice1, exclusive_choice2])
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, stakeholder_meet)
root.order.add_edge(stakeholder_meet, design_layout)
root.order.add_edge(design_layout, iot_loop)
root.order.add_edge(iot_loop, hydroponic_loop)
root.order.add_edge(hydroponic_loop, climate_loop)
root.order.add_edge(climate_loop, maintenance_loop)
root.order.add_edge(maintenance_loop, exclusive_choice1)
root.order.add_edge(exclusive_choice1, exclusive_choice2)
root.order.add_edge(exclusive_choice2, root)  # End of the process

print(root)