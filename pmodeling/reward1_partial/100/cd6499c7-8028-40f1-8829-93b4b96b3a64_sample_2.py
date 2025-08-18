import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Prep = Transition(label='Starter Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Whey_Drain = Transition(label='Whey Drain')
Cheese_Press = Transition(label='Cheese Press')
Salting_Process = Transition(label='Salting Process')
Aging_Setup = Transition(label='Aging Setup')
Temperature_Control = Transition(label='Temperature Control')
Batch_Labeling = Transition(label='Batch Labeling')
Eco_Packaging = Transition(label='Eco Packaging')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Coordination = Transition(label='Order Coordination')
Regulatory_Check = Transition(label='Regulatory Check')
Shipment_Planning = Transition(label='Shipment Planning')
Vendor_Liaison = Transition(label='Vendor Liaison')
Waste_Reduction = Transition(label='Waste Reduction')

# Define the POWL graph
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Quality_Testing,
    Starter_Prep,
    Milk_Pasteurize,
    Curd_Formation,
    Whey_Drain,
    Cheese_Press,
    Salting_Process,
    Aging_Setup,
    Temperature_Control,
    Batch_Labeling,
    Eco_Packaging,
    Inventory_Audit,
    Order_Coordination,
    Regulatory_Check,
    Shipment_Planning,
    Vendor_Liaison,
    Waste_Reduction
])

# Define the control flow
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Starter_Prep)
root.order.add_edge(Starter_Prep, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Formation)
root.order.add_edge(Curd_Formation, Whey_Drain)
root.order.add_edge(Whey_Drain, Cheese_Press)
root.order.add_edge(Cheese_Press, Salting_Process)
root.order.add_edge(Salting_Process, Aging_Setup)
root.order.add_edge(Aging_Setup, Temperature_Control)
root.order.add_edge(Temperature_Control, Batch_Labeling)
root.order.add_edge(Batch_Labeling, Eco_Packaging)
root.order.add_edge(Eco_Packaging, Inventory_Audit)
root.order.add_edge(Inventory_Audit, Order_Coordination)
root.order.add_edge(Order_Coordination, Regulatory_Check)
root.order.add_edge(Regulatory_Check, Shipment_Planning)
root.order.add_edge(Shipment_Planning, Vendor_Liaison)
root.order.add_edge(Vendor_Liaison, Waste_Reduction)

print(root)