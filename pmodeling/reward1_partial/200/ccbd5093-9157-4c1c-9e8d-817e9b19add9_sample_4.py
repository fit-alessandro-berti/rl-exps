from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

scan_markets = Transition(label='Scan Markets')
host_workshops = Transition(label='Host Workshops')
form_teams = Transition(label='Form Teams')
develop_prototypes = Transition(label='Develop Prototypes')
simulate_tests = Transition(label='Simulate Tests')
collect_feedback = Transition(label='Collect Feedback')
review_ethics = Transition(label='Review Ethics')
conduct_analysis = Transition(label='Conduct Analysis')
identify_partners = Transition(label='Identify Partners')
align_strategy = Transition(label='Align Strategy')
launch_pilots = Transition(label='Launch Pilots')
monitor_trends = Transition(label='Monitor Trends')
ai_analytics = Transition(label='AI Analytics')
pivot_plans = Transition(label='Pivot Plans')
cycle_renewal = Transition(label='Cycle Renewal')

skip = SilentTransition()

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        scan_markets,
        host_workshops,
        form_teams,
        develop_prototypes,
        simulate_tests,
        collect_feedback,
        review_ethics,
        conduct_analysis,
        identify_partners,
        align_strategy,
        launch_pilots,
        monitor_trends,
        ai_analytics,
        pivot_plans,
        cycle_renewal
    ],
    order=[
        (scan_markets, host_workshops),
        (host_workshops, form_teams),
        (form_teams, develop_prototypes),
        (develop_prototypes, simulate_tests),
        (simulate_tests, collect_feedback),
        (collect_feedback, review_ethics),
        (review_ethics, conduct_analysis),
        (conduct_analysis, identify_partners),
        (identify_partners, align_strategy),
        (align_strategy, launch_pilots),
        (launch_pilots, monitor_trends),
        (monitor_trends, ai_analytics),
        (ai_analytics, pivot_plans),
        (pivot_plans, cycle_renewal)
    ]
)

# Print the root model
print(root)