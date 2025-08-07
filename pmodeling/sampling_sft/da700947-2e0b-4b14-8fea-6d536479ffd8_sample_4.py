import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey    = Transition(label='Site Survey')
structural     = Transition(label='Structural Audit')
climate        = Transition(label='Climate Design')
lighting       = Transition(label='Lighting Setup')
irrigation     = Transition(label='Irrigation Plan')
nutrient       = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
ai_calibration = Transition(label='AI Calibration')
pest_scan      = Transition(label='Pest Scan')
energy_audit   = Transition(label='Energy Audit')
renewable_sync = Transition(label='Renewable Sync')
data_modeling  = Transition(label='Data Modeling')
staff_briefing = Transition(label='Staff Briefing')
compliance     = Transition(label='Compliance Check')
community      = Transition(label='Community Meet')
yield_review   = Transition(label='Yield Review')
feedback_loop  = Transition(label='Feedback Loop')

# Define the choice for pest monitoring: either pest scan or skip
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, Transition(label='tau')])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    structural,
    climate,
    lighting,
    irrigation,
    nutrient,
    sensor_install,
    ai_calibration,
    pest_choice,
    energy_audit,
    renewable_sync,
    data_modeling,
    staff_briefing,
    compliance,
    community,
    yield_review,
    feedback_loop
])

# Define the sequential dependencies
root.order.add_edge(site_survey, structural)
root.order.add_edge(structural, climate)
root.order.add_edge(climate, lighting)
root.order.add_edge(lighting, irrigation)
root.order.add_edge(irrigation, nutrient)
root.order.add_edge(nutrient, sensor_install)
root.order.add_edge(sensor_install, ai_calibration)
root.order.add_edge(ai_calibration, pest_choice)
root.order.add_edge(pest_choice, energy_audit)
root.order.add_edge(energy_audit, renewable_sync)
root.order.add_edge(renewable_sync, data_modeling)
root.order.add_edge(data_modeling, staff_briefing)
root.order.add_edge(staff_briefing, compliance)
root.order.add_edge(compliance, community)
root.order.add_edge(community, yield_review)
root.order.add_edge(yield_review, feedback_loop)

# The feedback loop is a special case of a loop:
# it executes the yield review, then optionally does the feedback_loop again
root.order.add_edge(yield_review, feedback_loop)
root.order.add_edge(feedback_loop, feedback_loop)  # this forms the loop body

print(root)