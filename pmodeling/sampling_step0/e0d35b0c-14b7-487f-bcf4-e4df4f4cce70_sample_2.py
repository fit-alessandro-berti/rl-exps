import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the urban rooftop farm process
root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Check'),
        Transition(label='Resource Sourcing'),
        Transition(label='System Install'),
        Transition(label='Lighting Setup'),
        Transition(label='Irrigation Setup'),
        Transition(label='Stakeholder Meet'),
        Transition(label='Volunteer Train'),
        Transition(label='Regulation Review'),
        Transition(label='Crop Selection'),
        Transition(label='Planting Phase'),
        Transition(label='Climate Control'),
        Transition(label='Growth Monitor'),
        Transition(label='Data Logging'),
        Transition(label='Harvest Event'),
        Transition(label='Waste Manage'),
        Transition(label='Feedback Collect'),
        Transition(label='Exit')  # Add an 'Exit' transition to complete the workflow
    ],
    order={
        ('Site Survey', 'Structural Check'): OperatorPOWL(operator=Operator.PO),
        ('Structural Check', 'Resource Sourcing'): OperatorPOWL(operator=Operator.PO),
        ('Resource Sourcing', 'System Install'): OperatorPOWL(operator=Operator.PO),
        ('System Install', 'Lighting Setup'): OperatorPOWL(operator=Operator.PO),
        ('Lighting Setup', 'Irrigation Setup'): OperatorPOWL(operator=Operator.PO),
        ('Irrigation Setup', 'Stakeholder Meet'): OperatorPOWL(operator=Operator.PO),
        ('Stakeholder Meet', 'Volunteer Train'): OperatorPOWL(operator=Operator.PO),
        ('Volunteer Train', 'Regulation Review'): OperatorPOWL(operator=Operator.PO),
        ('Regulation Review', 'Crop Selection'): OperatorPOWL(operator=Operator.PO),
        ('Crop Selection', 'Planting Phase'): OperatorPOWL(operator=Operator.PO),
        ('Planting Phase', 'Climate Control'): OperatorPOWL(operator=Operator.PO),
        ('Climate Control', 'Growth Monitor'): OperatorPOWL(operator=Operator.PO),
        ('Growth Monitor', 'Data Logging'): OperatorPOWL(operator=Operator.PO),
        ('Data Logging', 'Harvest Event'): OperatorPOWL(operator=Operator.PO),
        ('Harvest Event', 'Waste Manage'): OperatorPOWL(operator=Operator.PO),
        ('Waste Manage', 'Feedback Collect'): OperatorPOWL(operator=Operator.PO),
        ('Feedback Collect', 'Exit'): OperatorPOWL(operator=Operator.PO)
    }
)

# Add edges for the partial order relationships
root.order.add_edge('Site Survey', 'Structural Check')
root.order.add_edge('Structural Check', 'Resource Sourcing')
root.order.add_edge('Resource Sourcing', 'System Install')
root.order.add_edge('System Install', 'Lighting Setup')
root.order.add_edge('Lighting Setup', 'Irrigation Setup')
root.order.add_edge('Irrigation Setup', 'Stakeholder Meet')
root.order.add_edge('Stakeholder Meet', 'Volunteer Train')
root.order.add_edge('Volunteer Train', 'Regulation Review')
root.order.add_edge('Regulation Review', 'Crop Selection')
root.order.add_edge('Crop Selection', 'Planting Phase')
root.order.add_edge('Planting Phase', 'Climate Control')
root.order.add_edge('Climate Control', 'Growth Monitor')
root.order.add_edge('Growth Monitor', 'Data Logging')
root.order.add_edge('Data Logging', 'Harvest Event')
root.order.add_edge('Harvest Event', 'Waste Manage')
root.order.add_edge('Waste Manage', 'Feedback Collect')
root.order.add_edge('Feedback Collect', 'Exit')

# Now the POWL model is defined in the 'root' variable