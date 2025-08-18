from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
client_meet = Transition(label='Client Meet')
vision_capture = Transition(label='Vision Capture')
concept_draft = Transition(label='Concept Draft')
feedback_loop = Transition(label='Feedback Loop')
material_sourcing = Transition(label='Material Sourcing')
vendor_selection = Transition(label='Vendor Selection')
artisan_assign = Transition(label='Artisan Assign')
prototype_build = Transition(label='Prototype Build')
quality_review = Transition(label='Quality Review')
technical_check = Transition(label='Technical Check')
final_approval = Transition(label='Final Approval')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
secure_transport = Transition(label='Secure Transport')
installation_set = Transition(label='Installation Set')
client_support = Transition(label='Client Support')
archival_record = Transition(label='Archival Record')

# Define the exclusive choice for feedback loop
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, SilentTransition()])

# Define the exclusive choice for material sourcing
xor_material = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, SilentTransition()])

# Define the exclusive choice for vendor selection
xor_vendor = OperatorPOWL(operator=Operator.XOR, children=[vendor_selection, SilentTransition()])

# Define the exclusive choice for artisan assignment
xor_artisan = OperatorPOWL(operator=Operator.XOR, children=[artisan_assign, SilentTransition()])

# Define the exclusive choice for prototype build
xor_prototype = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, SilentTransition()])

# Define the exclusive choice for quality review
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_review, SilentTransition()])

# Define the exclusive choice for technical check
xor_technical = OperatorPOWL(operator=Operator.XOR, children=[technical_check, SilentTransition()])

# Define the exclusive choice for final approval
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_approval, SilentTransition()])

# Define the exclusive choice for packaging preparation
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, SilentTransition()])

# Define the exclusive choice for logistics plan
xor_logistics = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, SilentTransition()])

# Define the exclusive choice for secure transport
xor_transport = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, SilentTransition()])

# Define the exclusive choice for installation set
xor_installation = OperatorPOWL(operator=Operator.XOR, children=[installation_set, SilentTransition()])

# Define the exclusive choice for client support
xor_client = OperatorPOWL(operator=Operator.XOR, children=[client_support, SilentTransition()])

# Define the exclusive choice for archival record
xor_archival = OperatorPOWL(operator=Operator.XOR, children=[archival_record, SilentTransition()])

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        client_meet,
        vision_capture,
        concept_draft,
        xor_feedback,
        material_sourcing,
        xor_material,
        vendor_selection,
        xor_vendor,
        artisan_assign,
        xor_artisan,
        prototype_build,
        xor_prototype,
        quality_review,
        xor_quality,
        technical_check,
        xor_technical,
        final_approval,
        xor_final,
        packaging_prep,
        xor_packaging,
        logistics_plan,
        xor_logistics,
        secure_transport,
        xor_transport,
        installation_set,
        xor_installation,
        client_support,
        xor_client,
        archival_record,
        xor_archival
    ],
    order=[
        (client_meet, vision_capture),
        (vision_capture, concept_draft),
        (concept_draft, xor_feedback),
        (xor_feedback, xor_feedback),
        (xor_feedback, xor_material),
        (xor_material, xor_material),
        (xor_material, xor_vendor),
        (xor_vendor, xor_vendor),
        (xor_vendor, xor_artisan),
        (xor_artisan, xor_artisan),
        (xor_artisan, xor_prototype),
        (xor_prototype, xor_prototype),
        (xor_prototype, quality_review),
        (quality_review, xor_quality),
        (xor_quality, xor_quality),
        (xor_quality, technical_check),
        (technical_check, xor_technical),
        (xor_technical, xor_technical),
        (xor_technical, final_approval),
        (final_approval, xor_final),
        (xor_final, xor_final),
        (xor_final, packaging_prep),
        (packaging_prep, xor_packaging),
        (xor_packaging, xor_packaging),
        (xor_packaging, logistics_plan),
        (logistics_plan, xor_logistics),
        (xor_logistics, xor_logistics),
        (xor_logistics, secure_transport),
        (secure_transport, xor_transport),
        (xor_transport, xor_transport),
        (xor_transport, installation_set),
        (installation_set, xor_installation),
        (xor_installation, xor_installation),
        (xor_installation, client_support),
        (client_support, xor_client),
        (xor_client, xor_client),
        (xor_client, archival_record),
        (archival_record, xor_archival),
        (xor_archival, xor_archival)
    ]
)