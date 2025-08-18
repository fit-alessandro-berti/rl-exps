from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
culture_addition = Transition(label='Culture Addition')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
cheese_molding = Transition(label='Cheese Molding')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
health_certify = Transition(label='Health Certify')
custom_labeling = Transition(label='Custom Labeling')
cold_packaging = Transition(label='Cold Packaging')
logistics_setup = Transition(label='Logistics Setup')
export_docs = Transition(label='Export Docs')
customs_clearance = Transition(label='Customs Clearance')
shipment_track = Transition(label='Shipment Track')
client_feedback = Transition(label='Client Feedback')

# Define the process steps
root = StrictPartialOrder(
    nodes=[milk_sourcing, quality_testing, milk_pasteurize, culture_addition, curd_cutting, whey_drain, cheese_molding, controlled_aging, sensory_check, health_certify, custom_labeling, cold_packaging, logistics_setup, export_docs, customs_clearance, shipment_track, client_feedback],
    order={
        (milk_sourcing, quality_testing): None,
        (quality_testing, milk_pasteurize): None,
        (milk_pasteurize, culture_addition): None,
        (culture_addition, curd_cutting): None,
        (curd_cutting, whey_drain): None,
        (whey_drain, cheese_molding): None,
        (cheese_molding, controlled_aging): None,
        (controlled_aging, sensory_check): None,
        (sensory_check, health_certify): None,
        (health_certify, custom_labeling): None,
        (custom_labeling, cold_packaging): None,
        (cold_packaging, logistics_setup): None,
        (logistics_setup, export_docs): None,
        (export_docs, customs_clearance): None,
        (customs_clearance, shipment_track): None,
        (shipment_track, client_feedback): None
    }
)

print(root)