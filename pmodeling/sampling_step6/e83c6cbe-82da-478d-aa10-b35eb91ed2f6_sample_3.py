import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names as specified in the problem
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
stylistic_review = Transition(label='Stylistic Review')
expert_panel = Transition(label='Expert Panel')
legal_clearance = Transition(label='Legal Clearance')
ethics_audit = Transition(label='Ethics Audit')
insurance_quote = Transition(label='Insurance Quote')
risk_assess = Transition(label='Risk Assess')
digital_archive = Transition(label='Digital Archive')
replica_build = Transition(label='Replica Build')
transport_prep = Transition(label='Transport Prep')
final_review = Transition(label='Final Review')
catalog_entry = Transition(label='Catalog Entry')
public_notice = Transition(label='Public Notice')
condition_report = Transition(label='Condition Report')

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_testing,
    stylistic_review,
    expert_panel,
    legal_clearance,
    ethics_audit,
    insurance_quote,
    risk_assess,
    digital_archive,
    replica_build,
    transport_prep,
    final_review,
    catalog_entry,
    public_notice,
    condition_report
])

# Since there are no dependencies in the problem statement, no edges need to be added
# If there were dependencies, they would be added here using root.order.add_edge(source, target)