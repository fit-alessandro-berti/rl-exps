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

# Define silent transitions
skip = SilentTransition()

# Define workflow structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[structure_prep, system_install])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ai_calibration, data_review])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[waste_audit, community_meet])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, permit_filing])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[energy_connect, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

root = StrictPartialOrder(nodes=[site_survey, xor1, xor2, xor3, xor4, xor5, loop1, loop2, loop3, loop4])
root.order.add_edge(site_survey, xor1)
root.order.add_edge(site_survey, xor2)
root.order.add_edge(site_survey, xor3)
root.order.add_edge(site_survey, xor4)
root.order.add_edge(site_survey, xor5)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)
root.order.add_edge(xor5, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop1, loop4)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop3, loop4)