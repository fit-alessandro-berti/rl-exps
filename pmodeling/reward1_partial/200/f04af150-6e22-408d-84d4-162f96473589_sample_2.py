from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = ['Material Sourcing', 'Supplier Vetting', 'Design Review', 'Prototype Build', 'Quality Audit', 'Batch Scheduling', 'Handcrafting', 'Packaging Design', 'Custom Labeling', 'Sustainability Check', 'Inventory Sync', 'Market Analysis', 'Order Aggregation', 'Distribution Plan', 'Customer Feedback']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[transitions['Material Sourcing'], transitions['Supplier Vetting'], transitions['Design Review'], transitions['Prototype Build'], transitions['Quality Audit'], transitions['Batch Scheduling'], transitions['Handcrafting'], transitions['Packaging Design'], transitions['Custom Labeling'], transitions['Sustainability Check'], transitions['Inventory Sync'], transitions['Market Analysis'], transitions['Order Aggregation'], transitions['Distribution Plan'], transitions['Customer Feedback']],
    order=[
        # Add the necessary edges to define the partial order
        # For example, if 'Material Sourcing' must happen before 'Supplier Vetting':
        (transitions['Material Sourcing'], transitions['Supplier Vetting']),
        # Similarly, add edges for other dependencies as needed
    ]
)