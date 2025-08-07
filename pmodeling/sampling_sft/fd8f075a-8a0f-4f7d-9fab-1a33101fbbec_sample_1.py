import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
permit_filing    = Transition(label='Permit Filing')
structure_prep   = Transition(label='Structure Prep')
system_install   = Transition(label='System Install')
seed_sourcing    = Transition(label='Seed Sourcing')
energy_connect   = Transition(label='Energy Connect')
water_cycle      = Transition(label='Water Cycle')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_setup     = Transition(label='Sensor Setup')
ai_calibration   = Transition(label='AI Calibration')
staff_training   = Transition(label='Staff Training')
community_meet   = Transition(label='Community Meet')
growth_monitor   = Transition(label='Growth Monitor')
yield_forecast   = Transition(label='Yield Forecast')
waste_audit      = Transition(label='Waste Audit')
data_review      = Transition(label='Data Review')

# Loop for continuous monitoring and optimization
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, data_review]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    structure_prep,
    system_install,
    seed_sourcing,
    energy_connect,
    water_cycle,
    nutrient_mix,
    sensor_setup,
    ai_calibration,
    staff_training,
    community_meet,
    loop,
    yield_forecast,
    waste_audit
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, structure_prep)
root.order.add_edge(structure_prep, system_install)
root.order.add_edge(system_install, seed_sourcing)
root.order.add_edge(seed_sourcing, energy_connect)
root.order.add_edge(energy_connect, water_cycle)
root.order.add_edge(water_cycle, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, ai_calibration)
root.order.add_edge(ai_calibration, staff_training)
root.order.add_edge(staff_training, community_meet)
root.order.add_edge(community_meet, loop)
root.order.add_edge(loop, yield_forecast)
root.order.add_edge(loop, waste_audit)