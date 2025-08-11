import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_setup = Transition(label='Sensor Setup')
ai_calibration = Transition(label='AI Calibration')
seed_sourcing = Transition(label='Seed Sourcing')
staff_training = Transition(label='Staff Training')
energy_connect = Transition(label='Energy Connect')
water_cycle = Transition(label='Water Cycle')
growth_monitor = Transition(label='Growth Monitor')
waste_audit = Transition(label='Waste Audit')
community_meet = Transition(label='Community Meet')
data_review = Transition(label='Data Review')
yield_forecast = Transition(label='Yield Forecast')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice between nutrient_mix and skip for Sensor Setup
sensor_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, skip])

# Define the loop for AI Calibration and Sensor Setup
ai_calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_calibration, sensor_setup_choice])

# Define the loop for Growth Monitor and Data Review
growth_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, data_review])

# Define the partial order for the process
root = StrictPartialOrder(nodes=[site_survey, permit_filing, structure_prep, system_install, nutrient_mix, sensor_setup_choice, energy_connect, water_cycle, ai_calibration_loop, growth_monitor_loop, seed_sourcing, staff_training, community_meet, waste_audit])

# Define the order dependencies
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, structure_prep)
root.order.add_edge(structure_prep, system_install)
root.order.add_edge(system_install, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup_choice)
root.order.add_edge(sensor_setup_choice, energy_connect)
root.order.add_edge(energy_connect, water_cycle)
root.order.add_edge(water_cycle, ai_calibration_loop)
root.order.add_edge(ai_calibration_loop, growth_monitor_loop)
root.order.add_edge(growth_monitor_loop, seed_sourcing)
root.order.add_edge(seed_sourcing, staff_training)
root.order.add_edge(staff_training, community_meet)
root.order.add_edge(community_meet, waste_audit)
root.order.add_edge(waste_audit, yield_forecast)

# Print the root
print(root)