import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the workflow as a strict partial order
root = StrictPartialOrder(nodes=[site_survey, permit_filing, structure_prep, system_install, nutrient_mix, sensor_setup, ai_calibration, seed_sourcing, staff_training, energy_connect, water_cycle, growth_monitor, waste_audit, community_meet, data_review, yield_forecast])

# Define the dependencies between activities
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, structure_prep)
root.order.add_edge(structure_prep, system_install)
root.order.add_edge(system_install, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, ai_calibration)
root.order.add_edge(ai_calibration, seed_sourcing)
root.order.add_edge(seed_sourcing, staff_training)
root.order.add_edge(staff_training, energy_connect)
root.order.add_edge(energy_connect, water_cycle)
root.order.add_edge(water_cycle, growth_monitor)
root.order.add_edge(growth_monitor, waste_audit)
root.order.add_edge(waste_audit, community_meet)
root.order.add_edge(community_meet, data_review)
root.order.add_edge(data_review, yield_forecast)

print(root)