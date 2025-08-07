import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing    = Transition(label='Milk Sourcing')
curd_formation   = Transition(label='Curd Formation')
microbial_test   = Transition(label='Microbial Test')
whey_removal     = Transition(label='Whey Removal')
pressing_cheese  = Transition(label='Pressing Cheese')
salt_application = Transition(label='Salt Application')
aging_control    = Transition(label='Aging Control')
quality_check    = Transition(label='Quality Check')
eco_packaging    = Transition(label='Eco Packaging')
inventory_log    = Transition(label='Inventory Log')
temp_monitoring  = Transition(label='Temp Monitoring')
carrier_booking  = Transition(label='Carrier Booking')
trace_recording  = Transition(label='Trace Recording')
feedback_review  = Transition(label='Feedback Review')
compliance_audit = Transition(label='Compliance Audit')
batch_adjustment = Transition(label='Batch Adjustment')

# Define the core production sub‐process as a partial order
production_po = StrictPartialOrder(nodes=[
    milk_sourcing, curd_formation, microbial_test, whey_removal,
    pressing_cheese, salt_application, aging_control, quality_check
])
production_po.order.add_edge(milk_sourcing, curd_formation)
production_po.order.add_edge(curd_formation, microbial_test)
production_po.order.add_edge(microbial_test, whey_removal)
production_po.order.add_edge(whey_removal, pressing_cheese)
production_po.order.add_edge(pressing_cheese, salt_application)
production_po.order.add_edge(salt_application, aging_control)
production_po.order.add_edge(aging_control, quality_check)

# Define the final loop: Inventory Log -> Temp Monitoring -> Carrier Booking
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_log, temp_monitoring])
carrier_loop = OperatorPOWL(operator=Operator.LOOP, children=[carrier_loop, inventory_loop])

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    production_po, eco_packaging, quality_check,
    feedback_review, compliance_audit, batch_adjustment,
    trace_recording, carrier_loop
])
root.order.add_edge(production_po, eco_packaging)
root.order.add_edge(eco_packaging, quality_check)
root.order.add_edge(quality_check, feedback_review)
root.order.add_edge(feedback_review, compliance_audit)
root.order.add_edge(compliance_audit, batch_adjustment)
root.order.add_edge(batch_adjustment, trace_recording)
root.order.add_edge(trace_recording, carrier_loop)