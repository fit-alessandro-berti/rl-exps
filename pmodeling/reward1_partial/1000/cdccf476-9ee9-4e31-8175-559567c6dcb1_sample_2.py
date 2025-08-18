import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
Milk_Sourcing = Transition(label='Milk Sourcing')
Curd_Formation = Transition(label='Curd Formation')
Microbial_Test = Transition(label='Microbial Test')
Whey_Removal = Transition(label='Whey Removal')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salt_Application = Transition(label='Salt Application')
Aging_Control = Transition(label='Aging Control')
Quality_Check = Transition(label='Quality Check')
Eco_Packaging = Transition(label='Eco Packaging')
Inventory_Log = Transition(label='Inventory Log')
Temp_Monitoring = Transition(label='Temp Monitoring')
Carrier_Booking = Transition(label='Carrier Booking')
Trace_Recording = Transition(label='Trace Recording')
Feedback_Review = Transition(label='Feedback Review')
Compliance_Audit = Transition(label='Compliance Audit')
Batch_Adjustment = Transition(label='Batch Adjustment')

# Define silent transitions for concurrent or no-operation
skip = SilentTransition()

# Define the process structure
# Milk Sourcing -> Curd Formation -> Microbial Test -> Whey Removal -> Pressing Cheese -> Salt Application
# -> Aging Control -> Quality Check -> Eco Packaging -> Inventory Log -> Temp Monitoring
# -> Carrier Booking -> Trace Recording -> Feedback Review -> Compliance Audit -> Batch Adjustment
root = StrictPartialOrder(nodes=[Milk_Sourcing, Curd_Formation, Microbial_Test, Whey_Removal, Pressing_Cheese, Salt_Application, Aging_Control, Quality_Check, Eco_Packaging, Inventory_Log, Temp_Monitoring, Carrier_Booking, Trace_Recording, Feedback_Review, Compliance_Audit, Batch_Adjustment])
root.order.add_edge(Milk_Sourcing, Curd_Formation)
root.order.add_edge(Curd_Formation, Microbial_Test)
root.order.add_edge(Microbial_Test, Whey_Removal)
root.order.add_edge(Whey_Removal, Pressing_Cheese)
root.order.add_edge(Pressing_Cheese, Salt_Application)
root.order.add_edge(Salt_Application, Aging_Control)
root.order.add_edge(Aging_Control, Quality_Check)
root.order.add_edge(Quality_Check, Eco_Packaging)
root.order.add_edge(Eco_Packaging, Inventory_Log)
root.order.add_edge(Inventory_Log, Temp_Monitoring)
root.order.add_edge(Temp_Monitoring, Carrier_Booking)
root.order.add_edge(Carrier_Booking, Trace_Recording)
root.order.add_edge(Trace_Recording, Feedback_Review)
root.order.add_edge(Feedback_Review, Compliance_Audit)
root.order.add_edge(Compliance_Audit, Batch_Adjustment)