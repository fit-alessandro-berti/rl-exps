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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define the workflow structure
loop_structure = OperatorPOWL(operator=Operator.LOOP, children=[
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

xor_structure = OperatorPOWL(operator=Operator.XOR, children=[
    skip,
    loop_structure
])

# Create the root POWL model
root = StrictPartialOrder(nodes=[xor_structure])
root.order.add_edge(xor_structure, loop_structure)

# Print the final POWL model
print(root)