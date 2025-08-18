from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the operators
micro_lot_selection = OperatorPOWL(operator=Operator.MICRO_LOT_SELECTION, children=[bean_sorting])
specialized_fermentation = OperatorPOWL(operator=Operator.SPECIALIZED_FERMENTATION, children=[fermentation])
specialized_drying = OperatorPOWL(operator=Operator.SPECIALIZED_DRYING, children=[drying_process])
quality_control_analysis = OperatorPOWL(operator=Operator.ANALYSIS, children=[chemical_testing, sensory_analysis])
eco_packaging_process = OperatorPOWL(operator=Operator.ECO_PACKAGING, children=[eco_packaging, traceability_qr])
cold_transport_process = OperatorPOWL(operator=Operator.COLD_TRANSPORT, children=[cold_transport, env_monitoring])
subscription_adjustment = OperatorPOWL(operator=Operator.SUBSCRIPTION_ADJUST, children=[subscription_adjust])

# Define the partial order
root = StrictPartialOrder(nodes=[
    farm_sourcing,
    micro_lot_selection,
    specialized_fermentation,
    specialized_drying,
    quality_control_analysis,
    roast_profiling,
    eco_packaging_process,
    cold_transport_process,
    customer_feedback,
    subscription_adjustment
])

# Define the dependencies
root.order.add_edge(farm_sourcing, micro_lot_selection)
root.order.add_edge(micro_lot_selection, specialized_fermentation)
root.order.add_edge(micro_lot_selection, specialized_drying)
root.order.add_edge(specialized_fermentation, quality_control_analysis)
root.order.add_edge(specialized_drying, quality_control_analysis)
root.order.add_edge(quality_control_analysis, roast_profiling)
root.order.add_edge(roast_profiling, eco_packaging_process)
root.order.add_edge(eco_packaging_process, cold_transport_process)
root.order.add_edge(cold_transport_process, customer_feedback)
root.order.add_edge(customer_feedback, subscription_adjustment)

print(root)