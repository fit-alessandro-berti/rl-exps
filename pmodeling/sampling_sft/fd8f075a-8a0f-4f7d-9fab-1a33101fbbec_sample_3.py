import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
seed_sourcing = Transition(label='Seed Sourcing')
energy_connect = Transition(label='Energy Connect')
water_cycle = Transition(label='Water Cycle')
sensor_setup = Transition(label='Sensor Setup')
ai_calibration = Transition(label='AI Calibration')
staff_training = Transition(label='Staff Training')
data_review = Transition(label='Data Review')
yield_forecast = Transition(label='Yield Forecast')
growth_monitor = Transition(label='Growth Monitor')
waste_audit = Transition(label='Waste Audit')
community_meet = Transition(label='Community Meet')

# Define the loop for continuous monitoring and optimization
loop_body = StrictPartialOrder(nodes=[growth_monitor, data_review, yield_forecast])
loop_body.order.add_edge(growth_monitor, data_review)
loop_body.order.add_edge(data_review, yield_forecast)

loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, ai_calibration])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    structure_prep,
    system_install,
    seed_sourcing,
    energy_connect,
    water_cycle,
    loop,
    staff_training,
    community_meet,
    waste_audit
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, structure_prep)
root.order.add_edge(structure_prep, system_install)
root.order.add_edge(system_install, seed_sourcing)
root.order.add_edge(seed_sourcing, energy_connect)
root.order.add_edge(energy_connect, water_cycle)
root.order.add_edge(water_cycle, loop)
root.order.add_edge(loop, staff_training)
root.order.add_edge(staff_training, community_meet)
root.order.add_edge(community_meet, waste_audit)