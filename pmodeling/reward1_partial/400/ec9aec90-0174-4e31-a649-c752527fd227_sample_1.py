import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
assess_artifact = Transition(label='Assess Artifact')
verify_provenance = Transition(label='Verify Provenance')
analyze_condition = Transition(label='Analyze Condition')
plan_conservation = Transition(label='Plan Conservation')
clean_surface = Transition(label='Clean Surface')
stabilize_structure = Transition(label='Stabilize Structure')
source_materials = Transition(label='Source Materials')
fabricate_parts = Transition(label='Fabricate Parts')
perform_repairs = Transition(label='Perform Repairs')
apply_patina = Transition(label='Apply Patina')
match_colors = Transition(label='Match Colors')
document_process = Transition(label='Document Process')
review_quality = Transition(label='Review Quality')
obtain_approval = Transition(label='Obtain Approval')
package_securely = Transition(label='Package Securely')
arrange_transport = Transition(label='Arrange Transport')

# Define the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[
    assess_artifact, verify_provenance, analyze_condition, plan_conservation,
    clean_surface, stabilize_structure, source_materials, fabricate_parts,
    perform_repairs, apply_patina, match_colors, document_process, review_quality,
    obtain_approval, package_securely, arrange_transport])

root = StrictPartialOrder(nodes=[xor])