from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
Farm_Selection = Transition(label='Farm Selection')
Sample_Testing = Transition(label='Sample Testing')
Trade_Negotiation = Transition(label='Trade Negotiation')
Micro_Lot_Sorting = Transition(label='Micro-Lot Sorting')
Fermentation_Control = Transition(label='Fermentation Control')
Sensory_Profiling = Transition(label='Sensory Profiling')
Roast_Calibration = Transition(label='Roast Calibration')
Blend_Creation = Transition(label='Blend Creation')
Sustainability_Audit = Transition(label='Sustainability Audit')
Packaging_Design = Transition(label='Packaging Design')
Quality_Inspection = Transition(label='Quality Inspection')
Inventory_Sync = Transition(label='Inventory Sync')
Logistics_Planning = Transition(label='Logistics Planning')
Cafe_Training = Transition(label='Cafe Training')
Dynamic_Pricing = Transition(label='Dynamic Pricing')
Customer_Feedback = Transition(label='Customer Feedback')
Traceability_Logging = Transition(label='Traceability Logging')

# Define the process model using POWL operators
root = StrictPartialOrder(nodes=[
    Farm_Selection,
    Sample_Testing,
    Trade_Negotiation,
    Micro_Lot_Sorting,
    Fermentation_Control,
    Sensory_Profiling,
    Roast_Calibration,
    Blend_Creation,
    Sustainability_Audit,
    Packaging_Design,
    Quality_Inspection,
    Inventory_Sync,
    Logistics_Planning,
    Cafe_Training,
    Dynamic_Pricing,
    Customer_Feedback,
    Traceability_Logging
])

# Define the dependencies between nodes
root.order.add_edge(Farm_Selection, Sample_Testing)
root.order.add_edge(Sample_Testing, Trade_Negotiation)
root.order.add_edge(Trade_Negotiation, Micro_Lot_Sorting)
root.order.add_edge(Micro_Lot_Sorting, Fermentation_Control)
root.order.add_edge(Fermentation_Control, Sensory_Profiling)
root.order.add_edge(Sensory_Profiling, Roast_Calibration)
root.order.add_edge(Roast_Calibration, Blend_Creation)
root.order.add_edge(Blend_Creation, Sustainability_Audit)
root.order.add_edge(Sustainability_Audit, Packaging_Design)
root.order.add_edge(Packaging_Design, Quality_Inspection)
root.order.add_edge(Quality_Inspection, Inventory_Sync)
root.order.add_edge(Inventory_Sync, Logistics_Planning)
root.order.add_edge(Logistics_Planning, Cafe_Training)
root.order.add_edge(Cafe_Training, Dynamic_Pricing)
root.order.add_edge(Dynamic_Pricing, Customer_Feedback)
root.order.add_edge(Customer_Feedback, Traceability_Logging)

# Print the POWL model
print(root)