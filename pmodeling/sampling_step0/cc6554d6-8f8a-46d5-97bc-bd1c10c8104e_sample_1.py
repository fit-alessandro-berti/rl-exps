from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
demand_forecast = Transition(label='Demand Forecast')
risk_assess = Transition(label='Risk Assess')
supplier_audit = Transition(label='Supplier Audit')
inventory_scan = Transition(label='Inventory Scan')
route_optimize = Transition(label='Route Optimize')
order_prioritize = Transition(label='Order Prioritize')
contract_review = Transition(label='Contract Review')
delay_monitor = Transition(label='Delay Monitor')
shipment_reroute = Transition(label='Shipment Reroute')
cost_analyze = Transition(label='Cost Analyze')
compliance_check = Transition(label='Compliance Check')
alternative_engage = Transition(label='Alternative Engage')
inventory_reallocate = Transition(label='Inventory Reallocate')
performance_track = Transition(label='Performance Track')
feedback_loop = Transition(label='Feedback Loop')
strategy_update = Transition(label='Strategy Update')

# Define silent transitions
skip = SilentTransition()

# Define the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[delay_monitor, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[cost_analyze, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[alternative_engage, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[inventory_reallocate, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[performance_track, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[strategy_update, skip])

xor8 = OperatorPOWL(operator=Operator.XOR, children=[inventory_scan, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[order_prioritize, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[contract_review, skip])

xor12 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[supplier_audit, skip])

xor14 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor14, xor13])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor12, xor11])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor10, xor9])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor8, xor7])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor6, xor5])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[xor4, xor3])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[xor2, xor1])

# Define the root process
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, xor14, xor13, xor12, xor11, xor10, xor9, xor8, xor7, xor6, xor5, xor4, xor3, xor2, xor1])
root.order.add_edge(loop1, xor14)
root.order.add_edge(loop2, xor12)
root.order.add_edge(loop3, xor10)
root.order.add_edge(loop4, xor8)
root.order.add_edge(loop5, xor6)
root.order.add_edge(loop6, xor4)
root.order.add_edge(loop7, xor2)
root.order.add_edge(xor14, loop1)
root.order.add_edge(xor12, loop2)
root.order.add_edge(xor10, loop3)
root.order.add_edge(xor8, loop4)
root.order.add_edge(xor6, loop5)
root.order.add_edge(xor4, loop6)
root.order.add_edge(xor2, loop7)
root.order.add_edge(xor14, xor13)
root.order.add_edge(xor12, xor11)
root.order.add_edge(xor10, xor9)
root.order.add_edge(xor8, xor7)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor2, xor1)

print(root)