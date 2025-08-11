import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

farm_sourcing = Transition(label='Farm Sourcing')
lot_selection = Transition(label='Lot Selection')
bean_sorting = Transition(label='Bean Sorting')
fermentation = Transition(label='Fermentation')
drying_process = Transition(label='Drying Process')
quality_control = Transition(label='Quality Control')
chemical_testing = Transition(label='Chemical Testing')
sensory_analysis = Transition(label='Sensory Analysis')
roast_profiling = Transition(label='Roast Profiling')
eco_packaging = Transition(label='Eco Packaging')
traceability_qr = Transition(label='Traceability QR')
cold_transport = Transition(label='Cold Transport')
env_monitoring = Transition(label='Env Monitoring')
customer_feedback = Transition(label='Customer Feedback')
subscription_adjust = Transition(label='Subscription Adjust')

skip = SilentTransition()
loop_farm_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[farm_sourcing])
loop_lot_selection = OperatorPOWL(operator=Operator.LOOP, children=[lot_selection])
loop_quality_control = OperatorPOWL(operator=Operator.LOOP, children=[quality_control])
loop_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback])

xor_bean_sorting = OperatorPOWL(operator=Operator.XOR, children=[bean_sorting, skip])
xor_chemical_testing = OperatorPOWL(operator=Operator.XOR, children=[chemical_testing, skip])
xor_sensory_analysis = OperatorPOWL(operator=Operator.XOR, children=[sensory_analysis, skip])

xor_roast_profiling = OperatorPOWL(operator=Operator.XOR, children=[roast_profiling, skip])
xor_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, skip])
xor_traceability_qr = OperatorPOWL(operator=Operator.XOR, children=[traceability_qr, skip])

xor_env_monitoring = OperatorPOWL(operator=Operator.XOR, children=[env_monitoring, skip])
xor_subscription_adjust = OperatorPOWL(operator=Operator.XOR, children=[subscription_adjust, skip])

loop_farm_sourcing.order.add_edge(loop_farm_sourcing, xor_bean_sorting)
loop_lot_selection.order.add_edge(loop_lot_selection, xor_chemical_testing)
loop_quality_control.order.add_edge(loop_quality_control, xor_sensory_analysis)
loop_customer_feedback.order.add_edge(loop_customer_feedback, xor_roast_profiling)

xor_bean_sorting.order.add_edge(xor_bean_sorting, loop_quality_control)
xor_chemical_testing.order.add_edge(xor_chemical_testing, loop_customer_feedback)
xor_sensory_analysis.order.add_edge(xor_sensory_analysis, loop_farm_sourcing)

xor_roast_profiling.order.add_edge(xor_roast_profiling, xor_eco_packaging)
xor_eco_packaging.order.add_edge(xor_eco_packaging, xor_traceability_qr)
xor_traceability_qr.order.add_edge(xor_traceability_qr, xor_env_monitoring)
xor_env_monitoring.order.add_edge(xor_env_monitoring, xor_subscription_adjust)

xor_subscription_adjust.order.add_edge(xor_subscription_adjust, loop_lot_selection)
xor_env_monitoring.order.add_edge(xor_env_monitoring, loop_lot_selection)
xor_traceability_qr.order.add_edge(xor_traceability_qr, loop_lot_selection)
xor_eco_packaging.order.add_edge(xor_eco_packaging, loop_lot_selection)
xor_roast_profiling.order.add_edge(xor_roast_profiling, loop_lot_selection)
xor_sensory_analysis.order.add_edge(xor_sensory_analysis, loop_lot_selection)
xor_chemical_testing.order.add_edge(xor_chemical_testing, loop_lot_selection)
xor_bean_sorting.order.add_edge(xor_bean_sorting, loop_lot_selection)

root = StrictPartialOrder(nodes=[loop_farm_sourcing, loop_lot_selection, loop_quality_control, loop_customer_feedback, xor_bean_sorting, xor_chemical_testing, xor_sensory_analysis, xor_roast_profiling, xor_eco_packaging, xor_traceability_qr, xor_env_monitoring, xor_subscription_adjust])