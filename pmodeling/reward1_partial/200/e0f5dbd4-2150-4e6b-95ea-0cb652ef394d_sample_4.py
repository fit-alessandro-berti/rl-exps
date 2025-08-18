from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
drone_design = Transition(label='Drone Design')
regulatory_check = Transition(label='Regulatory Check')
nav_system = Transition(label='Nav System')
partner_setup = Transition(label='Partner Setup')
operator_training = Transition(label='Operator Training')
test_flights = Transition(label='Test Flights')
weather_review = Transition(label='Weather Review')
route_optimize = Transition(label='Route Optimize')
parts_logistics = Transition(label='Parts Logistics')
feedback_loop = Transition(label='Feedback Loop')
risk_assess = Transition(label='Risk Assess')
emergency_plan = Transition(label='Emergency Plan')
compliance_audit = Transition(label='Compliance Audit')
data_sync = Transition(label='Data Sync')
service_launch = Transition(label='Service Launch')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        drone_design,
        regulatory_check,
        nav_system,
        partner_setup,
        operator_training,
        test_flights,
        weather_review,
        route_optimize,
        parts_logistics,
        feedback_loop,
        risk_assess,
        emergency_plan,
        compliance_audit,
        data_sync,
        service_launch
    ],
    order=[
        # Define dependencies between activities
        (drone_design, regulatory_check),
        (regulatory_check, nav_system),
        (nav_system, partner_setup),
        (partner_setup, operator_training),
        (operator_training, test_flights),
        (test_flights, weather_review),
        (weather_review, route_optimize),
        (route_optimize, parts_logistics),
        (parts_logistics, feedback_loop),
        (feedback_loop, risk_assess),
        (risk_assess, emergency_plan),
        (emergency_plan, compliance_audit),
        (compliance_audit, data_sync),
        (data_sync, service_launch)
    ]
)