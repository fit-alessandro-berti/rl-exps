import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the artisanal cheese production and export process
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Culture_Addition = Transition(label='Culture Addition')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Cheese_Molding = Transition(label='Cheese Molding')
Controlled_Aging = Transition(label='Controlled Aging')
Sensory_Check = Transition(label='Sensory Check')
Health_Certify = Transition(label='Health Certify')
Custom_Labeling = Transition(label='Custom Labeling')
Cold_Packaging = Transition(label='Cold Packaging')
Logistics_Setup = Transition(label='Logistics Setup')
Export_Docs = Transition(label='Export Docs')
Customs_Clearance = Transition(label='Customs Clearance')
Shipment_Track = Transition(label='Shipment Track')
Client_Feedback = Transition(label='Client Feedback')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Quality_Testing,
    Milk_Pasteurize,
    Culture_Addition,
    Curd_Cutting,
    Whey_Drain,
    Cheese_Molding,
    Controlled_Aging,
    Sensory_Check,
    Health_Certify,
    Custom_Labeling,
    Cold_Packaging,
    Logistics_Setup,
    Export_Docs,
    Customs_Clearance,
    Shipment_Track,
    Client_Feedback
])

# Define the dependencies between activities
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Culture_Addition)
root.order.add_edge(Culture_Addition, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Drain)
root.order.add_edge(Whey_Drain, Cheese_Molding)
root.order.add_edge(Cheese_Molding, Controlled_Aging)
root.order.add_edge(Controlled_Aging, Sensory_Check)
root.order.add_edge(Sensory_Check, Health_Certify)
root.order.add_edge(Health_Certify, Custom_Labeling)
root.order.add_edge(Custom_Labeling, Cold_Packaging)
root.order.add_edge(Cold_Packaging, Logistics_Setup)
root.order.add_edge(Logistics_Setup, Export_Docs)
root.order.add_edge(Export_Docs, Customs_Clearance)
root.order.add_edge(Customs_Clearance, Shipment_Track)
root.order.add_edge(Shipment_Track, Client_Feedback)

# Print the final POWL model
print(root)