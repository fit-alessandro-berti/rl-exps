import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_drain = Transition(label='Whey Drain')
cheese_press = Transition(label='Cheese Press')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
temperature_control = Transition(label='Temperature Control')
batch_labeling = Transition(label='Batch Labeling')
eco_packaging = Transition(label='Eco Packaging')
inventory_audit = Transition(label='Inventory Audit')
order_coordination = Transition(label='Order Coordination')
regulatory_check = Transition(label='Regulatory Check')
shipment_planning = Transition(label='Shipment Planning')
vendor_liaison = Transition(label='Vendor Liaison')
waste_reduction = Transition(label='Waste Reduction')
skip = SilentTransition()

# Define the POWL model
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
loop_starter_prep = OperatorPOWL(operator=Operator.LOOP, children=[starter_prep])
loop_milk_pasteurize = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasteurize])
loop_curd_formation = OperatorPOWL(operator=Operator.LOOP, children=[curd_formation, whey_drain])
loop_cheese_press = OperatorPOWL(operator=Operator.LOOP, children=[cheese_press])
loop_salting_process = OperatorPOWL(operator=Operator.LOOP, children=[salting_process])
loop_aging_setup = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, temperature_control])
loop_batch_labeling = OperatorPOWL(operator=Operator.LOOP, children=[batch_labeling])
loop_eco_packaging = OperatorPOWL(operator=Operator.LOOP, children=[eco_packaging])
loop_inventory_audit = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit])
loop_order_coordination = OperatorPOWL(operator=Operator.LOOP, children=[order_coordination])
loop_regulatory_check = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check])
loop_shipment_planning = OperatorPOWL(operator=Operator.LOOP, children=[shipment_planning])
loop_vendor_liaison = OperatorPOWL(operator=Operator.LOOP, children=[vendor_liaison])
loop_waste_reduction = OperatorPOWL(operator=Operator.LOOP, children=[waste_reduction])

xor_milk_sourcing = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, skip])
xor_starter_prep = OperatorPOWL(operator=Operator.XOR, children=[starter_prep, skip])
xor_milk_pasteurize = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, skip])
xor_curd_formation = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, skip])
xor_whey_drain = OperatorPOWL(operator=Operator.XOR, children=[whey_drain, skip])
xor_cheese_press = OperatorPOWL(operator=Operator.XOR, children=[cheese_press, skip])
xor_salting_process = OperatorPOWL(operator=Operator.XOR, children=[salting_process, skip])
xor_aging_setup = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, skip])
xor_temperature_control = OperatorPOWL(operator=Operator.XOR, children=[temperature_control, skip])
xor_batch_labeling = OperatorPOWL(operator=Operator.XOR, children=[batch_labeling, skip])
xor_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, skip])
xor_inventory_audit = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, skip])
xor_order_coordination = OperatorPOWL(operator=Operator.XOR, children=[order_coordination, skip])
xor_regulatory_check = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, skip])
xor_shipment_planning = OperatorPOWL(operator=Operator.XOR, children=[shipment_planning, skip])
xor_vendor_liaison = OperatorPOWL(operator=Operator.XOR, children=[vendor_liaison, skip])
xor_waste_reduction = OperatorPOWL(operator=Operator.XOR, children=[waste_reduction, skip])

root = StrictPartialOrder(nodes=[loop_milk_sourcing, xor_milk_sourcing,
                                 loop_starter_prep, xor_starter_prep,
                                 loop_milk_pasteurize, xor_milk_pasteurize,
                                 loop_curd_formation, xor_curd_formation, xor_whey_drain,
                                 loop_cheese_press, xor_cheese_press,
                                 loop_salting_process, xor_salting_process,
                                 loop_aging_setup, xor_aging_setup, xor_temperature_control,
                                 loop_batch_labeling, xor_batch_labeling,
                                 loop_eco_packaging, xor_eco_packaging,
                                 loop_inventory_audit, xor_inventory_audit,
                                 loop_order_coordination, xor_order_coordination,
                                 loop_regulatory_check, xor_regulatory_check,
                                 loop_shipment_planning, xor_shipment_planning,
                                 loop_vendor_liaison, xor_vendor_liaison,
                                 loop_waste_reduction, xor_waste_reduction])

root.order.add_edge(loop_milk_sourcing, xor_milk_sourcing)
root.order.add_edge(loop_starter_prep, xor_starter_prep)
root.order.add_edge(loop_milk_pasteurize, xor_milk_pasteurize)
root.order.add_edge(loop_curd_formation, xor_curd_formation)
root.order.add_edge(loop_cheese_press, xor_cheese_press)
root.order.add_edge(loop_salting_process, xor_salting_process)
root.order.add_edge(loop_aging_setup, xor_aging_setup)
root.order.add_edge(loop_batch_labeling, xor_batch_labeling)
root.order.add_edge(loop_eco_packaging, xor_eco_packaging)
root.order.add_edge(loop_inventory_audit, xor_inventory_audit)
root.order.add_edge(loop_order_coordination, xor_order_coordination)
root.order.add_edge(loop_regulatory_check, xor_regulatory_check)
root.order.add_edge(loop_shipment_planning, xor_shipment_planning)
root.order.add_edge(loop_vendor_liaison, xor_vendor_liaison)
root.order.add_edge(loop_waste_reduction, xor_waste_reduction)

print(root)