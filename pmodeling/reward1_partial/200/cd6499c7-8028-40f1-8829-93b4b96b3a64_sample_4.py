from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

milk_sourcing_to_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip])
quality_testing_to_starter_prep = OperatorPOWL(operator=Operator.XOR, children=[starter_prep, skip])
starter_prep_to_milk_pasteurize = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, skip])
milk_pasteurize_to_curd_formation = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, skip])
curd_formation_to_whey_drain = OperatorPOWL(operator=Operator.XOR, children=[whey_drain, skip])
whey_drain_to_cheese_press = OperatorPOWL(operator=Operator.XOR, children=[cheese_press, skip])
cheese_press_to_salting_process = OperatorPOWL(operator=Operator.XOR, children=[salting_process, skip])
salting_process_to_aging_setup = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, skip])
aging_setup_to_temperature_control = OperatorPOWL(operator=Operator.XOR, children=[temperature_control, skip])
temperature_control_to_batch_labeling = OperatorPOWL(operator=Operator.XOR, children=[batch_labeling, skip])
batch_labeling_to_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, skip])
eco_packaging_to_inventory_audit = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, skip])
inventory_audit_to_order_coordination = OperatorPOWL(operator=Operator.XOR, children=[order_coordination, skip])
order_coordination_to_regulatory_check = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, skip])
regulatory_check_to_shipment_planning = OperatorPOWL(operator=Operator.XOR, children=[shipment_planning, skip])
shipment_planning_to_vendor_liaison = OperatorPOWL(operator=Operator.XOR, children=[vendor_liaison, skip])
vendor_liaison_to_waste_reduction = OperatorPOWL(operator=Operator.XOR, children=[waste_reduction, skip])

root = StrictPartialOrder(nodes=[
    milk_sourcing,
    milk_sourcing_to_quality_testing,
    quality_testing_to_starter_prep,
    starter_prep_to_milk_pasteurize,
    milk_pasteurize_to_curd_formation,
    curd_formation_to_whey_drain,
    whey_drain_to_cheese_press,
    cheese_press_to_salting_process,
    salting_process_to_aging_setup,
    aging_setup_to_temperature_control,
    temperature_control_to_batch_labeling,
    batch_labeling_to_eco_packaging,
    eco_packaging_to_inventory_audit,
    inventory_audit_to_order_coordination,
    order_coordination_to_regulatory_check,
    regulatory_check_to_shipment_planning,
    shipment_planning_to_vendor_liaison,
    vendor_liaison_to_waste_reduction
])

root.order.add_edge(milk_sourcing, milk_sourcing_to_quality_testing)
root.order.add_edge(milk_sourcing_to_quality_testing, quality_testing_to_starter_prep)
root.order.add_edge(quality_testing_to_starter_prep, starter_prep_to_milk_pasteurize)
root.order.add_edge(starter_prep_to_milk_pasteurize, milk_pasteurize_to_curd_formation)
root.order.add_edge(milk_pasteurize_to_curd_formation, curd_formation_to_whey_drain)
root.order.add_edge(curd_formation_to_whey_drain, whey_drain_to_cheese_press)
root.order.add_edge(whey_drain_to_cheese_press, cheese_press_to_salting_process)
root.order.add_edge(cheese_press_to_salting_process, salting_process_to_aging_setup)
root.order.add_edge(salting_process_to_aging_setup, aging_setup_to_temperature_control)
root.order.add_edge(aging_setup_to_temperature_control, temperature_control_to_batch_labeling)
root.order.add_edge(temperature_control_to_batch_labeling, batch_labeling_to_eco_packaging)
root.order.add_edge(batch_labeling_to_eco_packaging, eco_packaging_to_inventory_audit)
root.order.add_edge(eco_packaging_to_inventory_audit, inventory_audit_to_order_coordination)
root.order.add_edge(inventory_audit_to_order_coordination, order_coordination_to_regulatory_check)
root.order.add_edge(order_coordination_to_regulatory_check, regulatory_check_to_shipment_planning)
root.order.add_edge(regulatory_check_to_shipment_planning, shipment_planning_to_vendor_liaison)
root.order.add_edge(shipment_planning_to_vendor_liaison, vendor_liaison_to_waste_reduction)