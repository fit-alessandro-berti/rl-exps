from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their labels
Scan_Markets = Transition(label='Scan Markets')
Host_Workshops = Transition(label='Host Workshops')
Form_Teams = Transition(label='Form Teams')
Develop_Prototypes = Transition(label='Develop Prototypes')
Simulate_Tests = Transition(label='Simulate Tests')
Collect_Feedback = Transition(label='Collect Feedback')
Review_Ethics = Transition(label='Review Ethics')
Conduct_Analysis = Transition(label='Conduct Analysis')
Identify_Partners = Transition(label='Identify Partners')
Align_Strategy = Transition(label='Align Strategy')
Launch_Pilots = Transition(label='Launch Pilots')
Monitor_Trends = Transition(label='Monitor Trends')
AI_Analytics = Transition(label='AI Analytics')
Pivot_Plans = Transition(label='Pivot Plans')
Cycle_Renewal = Transition(label='Cycle Renewal')

# Define the partial order with its nodes and dependencies
root = StrictPartialOrder(nodes=[
    Scan_Markets, Host_Workshops, Form_Teams, Develop_Prototypes, Simulate_Tests,
    Collect_Feedback, Review_Ethics, Conduct_Analysis, Identify_Partners, Align_Strategy,
    Launch_Pilots, Monitor_Trends, AI_Analytics, Pivot_Plans, Cycle_Renewal
])

# Define the dependencies between the nodes
root.order.add_edge(Scan_Markets, Host_Workshops)
root.order.add_edge(Host_Workshops, Form_Teams)
root.order.add_edge(Form_Teams, Develop_Prototypes)
root.order.add_edge(Develop_Prototypes, Simulate_Tests)
root.order.add_edge(Simulate_Tests, Collect_Feedback)
root.order.add_edge(Collect_Feedback, Review_Ethics)
root.order.add_edge(Review_Ethics, Conduct_Analysis)
root.order.add_edge(Conduct_Analysis, Identify_Partners)
root.order.add_edge(Identify_Partners, Align_Strategy)
root.order.add_edge(Align_Strategy, Launch_Pilots)
root.order.add_edge(Launch_Pilots, Monitor_Trends)
root.order.add_edge(Monitor_Trends, AI_Analytics)
root.order.add_edge(AI_Analytics, Pivot_Plans)
root.order.add_edge(Pivot_Plans, Cycle_Renewal)

# Print the root model
print(root)