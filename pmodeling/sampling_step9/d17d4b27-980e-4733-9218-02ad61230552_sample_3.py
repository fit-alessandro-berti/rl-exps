import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
zoning_review = Transition(label='Zoning Review')
modular_design = Transition(label='Modular Design')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
ai_monitoring = Transition(label='AI Monitoring')
lighting_control = Transition(label='Lighting Control')
energy_audit = Transition(label='Energy Audit')
water_reclaim = Transition(label='Water Reclaim')
waste_sorting = Transition(label='Waste Sorting')
community_meet = Transition(label='Community Meet')
staff_training = Transition(label='Staff Training')
yield_forecast = Transition(label='Yield Forecast')
market_sync = Transition(label='Market Sync')
supply_chain = Transition(label='Supply Chain')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[lighting_control, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[water_reclaim, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[market_sync, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[supply_chain, skip])

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, xor8])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor9, xor10])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor5)
root.order.add_edge(loop3, xor6)
root.order.add_edge(loop4, xor7)
root.order.add_edge(loop4, xor8)
root.order.add_edge(loop5, xor9)
root.order.add_edge(loop5, xor10)