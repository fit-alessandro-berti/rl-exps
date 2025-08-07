import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    structure_prep,
    system_install,
    nutrient_mix,
    sensor_setup,
    ai_calibration,
    seed_sourcing,
    staff_training,
    energy_connect,
    water_cycle,
    growth_monitor,
    waste_audit,
    community_meet,
    data_review,
    yield_forecast
])

# Add dependencies between activities (if any)
# For example, if 'Permit Filing' must occur before 'Structure Prep':
root.order.add_edge(permit_filing, structure_prep)

# If 'Site Survey' is concurrent with other activities:
# root.order.add_edge(site_survey, permit_filing)

# If 'Staff Training' occurs after 'AI Calibration' and 'Seed Sourcing':
# root.order.add_edge(ai_calibration, staff_training)
# root.order.add_edge(seed_sourcing, staff_training)

# If 'Energy Connect' and 'Water Cycle' are concurrent:
# root.order.add_edge(energy_connect, water_cycle)

# If 'Growth Monitor' and 'Data Review' are concurrent:
# root.order.add_edge(growth_monitor, data_review)

# If 'Waste Audit' is concurrent with 'Community Meet':
# root.order.add_edge(waste_audit, community_meet)

# If 'Data Review' is concurrent with 'Yield Forecast':
# root.order.add_edge(data_review, yield_forecast)

# Now 'root' contains the POWL model for the process.