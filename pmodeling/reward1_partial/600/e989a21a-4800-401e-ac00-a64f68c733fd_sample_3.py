from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
visual_inspect = Transition(label='Visual Inspect')
document_gather = Transition(label='Document Gather')
material_test = Transition(label='Material Test')
pigment_analyze = Transition(label='Pigment Analyze')
style_compare = Transition(label='Style Compare')
provenance_trace = Transition(label='Provenance Trace')
data_crosscheck = Transition(label='Data Crosscheck')
infrared_scan = Transition(label='Infrared Scan')
xray_fluoresce = Transition(label='Xray Fluoresce')
expert_consult = Transition(label='Expert Consult')
forgeries_detect = Transition(label='Forgery Detect')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
final_approval = Transition(label='Final Approval')
archive_store = Transition(label='Archive Store')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        visual_inspect,
        document_gather,
        material_test,
        pigment_analyze,
        style_compare,
        provenance_trace,
        data_crosscheck,
        infrared_scan,
        xray_fluoresce,
        expert_consult,
        forgeries_detect,
        report_draft,
        stakeholder_review,
        final_approval,
        archive_store
    ],
    order=[
        (visual_inspect, document_gather),
        (document_gather, material_test),
        (material_test, pigment_analyze),
        (pigment_analyze, style_compare),
        (style_compare, provenance_trace),
        (provenance_trace, data_crosscheck),
        (data_crosscheck, infrared_scan),
        (infrared_scan, xray_fluoresce),
        (xray_fluoresce, expert_consult),
        (expert_consult, forgeries_detect),
        (forgeries_detect, report_draft),
        (report_draft, stakeholder_review),
        (stakeholder_review, final_approval),
        (final_approval, archive_store)
    ]
)

# Return the root of the POWL model
print(root)