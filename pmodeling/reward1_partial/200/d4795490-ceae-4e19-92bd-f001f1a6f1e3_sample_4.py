from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip_fermentation = SilentTransition()
skip_drying = SilentTransition()
skip_chemical = SilentTransition()
skip_sensory = SilentTransition()
skip_roast = SilentTransition()
skip_packaging = SilentTransition()
skip_qr = SilentTransition()
skip_transport = SilentTransition()
skip_monitoring = SilentTransition()
skip_feedback = SilentTransition()
skip_adjust = SilentTransition()

# Define loops and exclusive choices
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation, skip_fermentation])
drying_loop = OperatorPOWL(operator=Operator.LOOP, children=[drying_process, skip_drying])
chemical_loop = OperatorPOWL(operator=Operator.LOOP, children=[chemical_testing, skip_chemical])
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_analysis, skip_sensory])
roast_loop = OperatorPOWL(operator=Operator.LOOP, children=[roast_profiling, skip_roast])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[eco_packaging, skip_packaging])
qr_loop = OperatorPOWL(operator=Operator.LOOP, children=[traceability_qr, skip_qr])
transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_transport, skip_transport])
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_monitoring, skip_monitoring])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, skip_feedback])
adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[subscription_adjust, skip_adjust])

# Define the root model
root = StrictPartialOrder(
    nodes=[
        farm_sourcing,
        lot_selection,
        bean_sorting,
        fermentation_loop,
        drying_loop,
        quality_control,
        chemical_loop,
        sensory_loop,
        roast_loop,
        packaging_loop,
        qr_loop,
        transport_loop,
        monitoring_loop,
        feedback_loop,
        adjust_loop
    ]
)

# Define dependencies
root.order.add_edge(farm_sourcing, lot_selection)
root.order.add_edge(lot_selection, bean_sorting)
root.order.add_edge(bean_sorting, fermentation_loop)
root.order.add_edge(fermentation_loop, drying_loop)
root.order.add_edge(drying_loop, quality_control)
root.order.add_edge(quality_control, chemical_loop)
root.order.add_edge(chemical_loop, sensory_loop)
root.order.add_edge(sensory_loop, roast_loop)
root.order.add_edge(roast_loop, packaging_loop)
root.order.add_edge(packaging_loop, qr_loop)
root.order.add_edge(qr_loop, transport_loop)
root.order.add_edge(transport_loop, monitoring_loop)
root.order.add_edge(monitoring_loop, feedback_loop)
root.order.add_edge(feedback_loop, adjust_loop)

# Print the root model
print(root)