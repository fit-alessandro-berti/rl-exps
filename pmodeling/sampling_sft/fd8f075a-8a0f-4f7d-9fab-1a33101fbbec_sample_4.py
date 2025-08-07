import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
permit_filing     = Transition(label='Permit Filing')
structure_prep    = Transition(label='Structure Prep')
system_install    = Transition(label='System Install')
energy_connect    = Transition(label='Energy Connect')
water_cycle       = Transition(label='Water Cycle')
sensor_setup      = Transition(label='Sensor Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
staff_training    = Transition(label='Staff Training')
community_meet    = Transition(label='Community Meet')
data_review       = Transition(label='Data Review')
growth_monitor    = Transition(label='Growth Monitor')
yield_forecast    = Transition(label='Yield Forecast')
waste_audit       = Transition(label='Waste Audit')
ai_calibration    = Transition(label='AI Calibration')

# Loop for continuous monitoring and data review
loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, data_review]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    structure_prep,
    system_install,
    energy_connect,
    water_cycle,
    sensor_setup,
    nutrient_mix,
    staff_training,
    community_meet,
    ai_calibration,
    loop_monitor,
    yield_forecast,
    waste_audit
])

# Sequence of setup and calibration before monitoring
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, structure_prep)
root.order.add_edge(structure_prep, system_install)
root.order.add_edge(system_install, energy_connect)
root.order.add_edge(energy_connect, water_cycle)
root.order.add_edge(water_cycle, sensor_setup)
root.order.add_edge(sensor_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, staff_training)
root.order.add_edge(staff_training, community_meet)
root.order.add_edge(community_meet, ai_calibration)

# After calibration, enter the monitoring loop
root.order.add_edge(ai_calibration, loop_monitor)

# After monitoring, branch for forecast and audit
root.order.add_edge(loop_monitor, yield_forecast)
root.order.add_edge(loop_monitor, waste_audit)