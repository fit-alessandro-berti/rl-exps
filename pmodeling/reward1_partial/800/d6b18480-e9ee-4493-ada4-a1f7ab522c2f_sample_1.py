import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = ['Material Sourcing', 'Forager Dispatch', 'Authenticity Check', 'Batch Scheduling', 'Artisan Allocation', 'Craft Assembly', 'Quality Inspection', 'Blockchain Update', 'Demand Forecast', 'Price Adjustment', 'Compliance Review', 'Logistics Planning', 'Distributor Sync', 'Customer Feedback', 'Product Refinement', 'Reputation Audit', 'Seasonal Review']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the process structure using POWL
# The process includes a loop for artisan allocation and batch scheduling
loop = OperatorPOWL(operator=Operator.LOOP, children=[transitions[4], transitions[5]])

xor = OperatorPOWL(operator=Operator.XOR, children=[transitions[6], SilentTransition()])

# The process also includes dynamic pricing and customer feedback loops
xor2 = OperatorPOWL(operator=Operator.XOR, children=[transitions[9], SilentTransition()])

xor3 = OperatorPOWL(operator=Operator.XOR, children=[transitions[12], SilentTransition()])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[transitions[14], SilentTransition()])

xor5 = OperatorPOWL(operator=Operator.XOR, children=[transitions[16], SilentTransition()])

xor6 = OperatorPOWL(operator=Operator.XOR, children=[transitions[17], SilentTransition()])

xor7 = OperatorPOWL(operator=Operator.XOR, children=[transitions[18], SilentTransition()])

xor8 = OperatorPOWL(operator=Operator.XOR, children=[transitions[19], SilentTransition()])

xor9 = OperatorPOWL(operator=Operator.XOR, children=[transitions[20], SilentTransition()])

xor10 = OperatorPOWL(operator=Operator.XOR, children=[transitions[21], SilentTransition()])

xor11 = OperatorPOWL(operator=Operator.XOR, children=[transitions[22], SilentTransition()])

xor12 = OperatorPOWL(operator=Operator.XOR, children=[transitions[23], SilentTransition()])

xor13 = OperatorPOWL(operator=Operator.XOR, children=[transitions[24], SilentTransition()])

xor14 = OperatorPOWL(operator=Operator.XOR, children=[transitions[25], SilentTransition()])

xor15 = OperatorPOWL(operator=Operator.XOR, children=[transitions[26], SilentTransition()])

xor16 = OperatorPOWL(operator=Operator.XOR, children=[transitions[27], SilentTransition()])

xor17 = OperatorPOWL(operator=Operator.XOR, children=[transitions[28], SilentTransition()])

xor18 = OperatorPOWL(operator=Operator.XOR, children=[transitions[29], SilentTransition()])

xor19 = OperatorPOWL(operator=Operator.XOR, children=[transitions[30], SilentTransition()])

xor20 = OperatorPOWL(operator=Operator.XOR, children=[transitions[31], SilentTransition()])

xor21 = OperatorPOWL(operator=Operator.XOR, children=[transitions[32], SilentTransition()])

xor22 = OperatorPOWL(operator=Operator.XOR, children=[transitions[33], SilentTransition()])

xor23 = OperatorPOWL(operator=Operator.XOR, children=[transitions[34], SilentTransition()])

xor24 = OperatorPOWL(operator=Operator.XOR, children=[transitions[35], SilentTransition()])

xor25 = OperatorPOWL(operator=Operator.XOR, children=[transitions[36], SilentTransition()])

xor26 = OperatorPOWL(operator=Operator.XOR, children=[transitions[37], SilentTransition()])

xor27 = OperatorPOWL(operator=Operator.XOR, children=[transitions[38], SilentTransition()])

xor28 = OperatorPOWL(operator=Operator.XOR, children=[transitions[39], SilentTransition()])

xor29 = OperatorPOWL(operator=Operator.XOR, children=[transitions[40], SilentTransition()])

xor30 = OperatorPOWL(operator=Operator.XOR, children=[transitions[41], SilentTransition()])

xor31 = OperatorPOWL(operator=Operator.XOR, children=[transitions[42], SilentTransition()])

xor32 = OperatorPOWL(operator=Operator.XOR, children=[transitions[43], SilentTransition()])

xor33 = OperatorPOWL(operator=Operator.XOR, children=[transitions[44], SilentTransition()])

xor34 = OperatorPOWL(operator=Operator.XOR, children=[transitions[45], SilentTransition()])

xor35 = OperatorPOWL(operator=Operator.XOR, children=[transitions[46], SilentTransition()])

xor36 = OperatorPOWL(operator=Operator.XOR, children=[transitions[47], SilentTransition()])

xor37 = OperatorPOWL(operator=Operator.XOR, children=[transitions[48], SilentTransition()])

xor38 = OperatorPOWL(operator=Operator.XOR, children=[transitions[49], SilentTransition()])

xor39 = OperatorPOWL(operator=Operator.XOR, children=[transitions[50], SilentTransition()])

xor40 = OperatorPOWL(operator=Operator.XOR, children=[transitions[51], SilentTransition()])

xor41 = OperatorPOWL(operator=Operator.XOR, children=[transitions[52], SilentTransition()])

xor42 = OperatorPOWL(operator=Operator.XOR, children=[transitions[53], SilentTransition()])

xor43 = OperatorPOWL(operator=Operator.XOR, children=[transitions[54], SilentTransition()])

xor44 = OperatorPOWL(operator=Operator.XOR, children=[transitions[55], SilentTransition()])

xor45 = OperatorPOWL(operator=Operator.XOR, children=[transitions[56], SilentTransition()])

xor46 = OperatorPOWL(operator=Operator.XOR, children=[transitions[57], SilentTransition()])

xor47 = OperatorPOWL(operator=Operator.XOR, children=[transitions[58], SilentTransition()])

xor48 = OperatorPOWL(operator=Operator.XOR, children=[transitions[59], SilentTransition()])

xor49 = OperatorPOWL(operator=Operator.XOR, children=[transitions[60], SilentTransition()])

xor50 = OperatorPOWL(operator=Operator.XOR, children=[transitions[61], SilentTransition()])

xor51 = OperatorPOWL(operator=Operator.XOR, children=[transitions[62], SilentTransition()])

xor52 = OperatorPOWL(operator=Operator.XOR, children=[transitions[63], SilentTransition()])

xor53 = OperatorPOWL(operator=Operator.XOR, children=[transitions[64], SilentTransition()])

xor54 = OperatorPOWL(operator=Operator.XOR, children=[transitions[65], SilentTransition()])

xor55 = OperatorPOWL(operator=Operator.XOR, children=[transitions[66], SilentTransition()])

xor56 = OperatorPOWL(operator=Operator.XOR, children=[transitions[67], SilentTransition()])

xor57 = OperatorPOWL(operator=Operator.XOR, children=[transitions[68], SilentTransition()])

xor58 = OperatorPOWL(operator=Operator.XOR, children=[transitions[69], SilentTransition()])

xor59 = OperatorPOWL(operator=Operator.XOR, children=[transitions[70], SilentTransition()])

xor60 = OperatorPOWL(operator=Operator.XOR, children=[transitions[71], SilentTransition()])

xor61 = OperatorPOWL(operator=Operator.XOR, children=[transitions[72], SilentTransition()])

xor62 = OperatorPOWL(operator=Operator.XOR, children=[transitions[73], SilentTransition()])

xor63 = OperatorPOWL(operator=Operator.XOR, children=[transitions[74], SilentTransition()])

xor64 = OperatorPOWL(operator=Operator.XOR, children=[transitions[75], SilentTransition()])

xor65 = OperatorPOWL(operator=Operator.XOR, children=[transitions[76], SilentTransition()])

xor66 = OperatorPOWL(operator=Operator.XOR, children=[transitions[77], SilentTransition()])

xor67 = OperatorPOWL(operator=Operator.XOR, children=[transitions[78], SilentTransition()])

xor68 = OperatorPOWL(operator=Operator.XOR, children=[transitions[79], SilentTransition()])

xor69 = OperatorPOWL(operator=Operator.XOR, children=[transitions[80], SilentTransition()])

xor70 = OperatorPOWL(operator=Operator.XOR, children=[transitions[81], SilentTransition()])

xor71 = OperatorPOWL(operator=Operator.XOR, children=[transitions[82], SilentTransition()])

xor72 = OperatorPOWL(operator=Operator.XOR, children=[transitions[83], SilentTransition()])

xor73 = OperatorPOWL(operator=Operator.XOR, children=[transitions[84], SilentTransition()])

xor74 = OperatorPOWL(operator=Operator.XOR, children=[transitions[85], SilentTransition()])

xor75 = OperatorPOWL(operator=Operator.XOR, children=[transitions[86], SilentTransition()])

xor76 = OperatorPOWL(operator=Operator.XOR, children=[transitions[87], SilentTransition()])

xor77 = OperatorPOWL(operator=Operator.XOR, children=[transitions[88], SilentTransition()])

xor78 = OperatorPOWL(operator=Operator.XOR, children=[transitions[89], SilentTransition()])

xor79 = OperatorPOWL(operator=Operator.XOR, children=[transitions[90], SilentTransition()])

xor80 = OperatorPOWL(operator=Operator.XOR, children=[transitions[91], SilentTransition()])

xor81 = OperatorPOWL(operator=Operator.XOR, children=[transitions[92], SilentTransition()])

xor82 = OperatorPOWL(operator=Operator.XOR, children=[transitions[93], SilentTransition()])

xor83 = OperatorPOWL(operator=Operator.XOR, children=[transitions[94], SilentTransition()])

xor84 = OperatorPOWL(operator=Operator.XOR, children=[transitions[95], SilentTransition()])

xor85 = OperatorPOWL(operator=Operator.XOR, children=[transitions[96], SilentTransition()])

xor86 = OperatorPOWL(operator=Operator.XOR, children=[transitions[97], SilentTransition()])

xor87 = OperatorPOWL(operator=Operator.XOR, children=[transitions[98], SilentTransition()])

xor88 = OperatorPOWL(operator=Operator.XOR, children=[transitions[99], SilentTransition()])

xor89 = OperatorPOWL(operator=Operator.XOR, children=[transitions[100], SilentTransition()])

xor90 = OperatorPOWL(operator=Operator.XOR, children=[transitions[101], SilentTransition()])

xor91 = OperatorPOWL(operator=Operator.XOR, children=[transitions[102], SilentTransition()])

xor92 = OperatorPOWL(operator=Operator.XOR, children=[transitions[103], SilentTransition()])

xor93 = OperatorPOWL(operator=Operator.XOR, children=[transitions[104], SilentTransition()])

xor94 = OperatorPOWL(operator=Operator.XOR, children=[transitions[105], SilentTransition()])

xor95 = OperatorPOWL(operator=Operator.XOR, children=[transitions[106], SilentTransition()])

xor96 = OperatorPOWL(operator=Operator.XOR, children=[transitions[107], SilentTransition()])

xor97 = OperatorPOWL(operator=Operator.XOR, children=[transitions[108], SilentTransition()])

xor98 = OperatorPOWL(operator=Operator.XOR, children=[transitions[109], SilentTransition()])

xor99 = OperatorPOWL(operator=Operator.XOR, children=[transitions[110], SilentTransition()])

xor100 = OperatorPOWL(operator=Operator.XOR, children=[transitions[111], SilentTransition()])

xor101 = OperatorPOWL(operator=Operator.XOR, children=[transitions[112], SilentTransition()])

xor102 = OperatorPOWL(operator=Operator.XOR, children=[transitions[113], SilentTransition()])

xor103 = OperatorPOWL(operator=Operator.XOR, children=[transitions[114], SilentTransition()])

xor104 = OperatorPOWL(operator=Operator.XOR, children=[transitions[115], SilentTransition()])

xor105 = OperatorPOWL(operator=Operator.XOR, children=[transitions[116], SilentTransition()])

xor106 = OperatorPOWL(operator=Operator.XOR, children=[transitions[117], SilentTransition()])

xor107 = OperatorPOWL(operator=Operator.XOR, children=[transitions[118], SilentTransition()])

xor108 = OperatorPOWL(operator=Operator.XOR, children=[transitions[119], SilentTransition()])

xor109 = OperatorPOWL(operator=Operator.XOR, children=[transitions[120], SilentTransition()])

xor110 = OperatorPOWL(operator=Operator.XOR, children=[transitions[121], SilentTransition()])

xor111 = OperatorPOWL(operator=Operator.XOR, children=[transitions[122], SilentTransition()])

xor112 = OperatorPOWL(operator=Operator.XOR, children=[transitions[123], SilentTransition()])

xor113 = OperatorPOWL(operator=Operator.XOR, children=[transitions[124], SilentTransition()])

xor114 = OperatorPOWL(operator=Operator.XOR, children=[transitions[125], SilentTransition()])

xor115 = OperatorPOWL(operator=Operator.XOR, children=[transitions[126], SilentTransition()])

xor116 = OperatorPOWL(operator=Operator.XOR, children=[transitions[127], SilentTransition()])

xor117 = OperatorPOWL(operator=Operator.XOR, children=[transitions[128], SilentTransition()])

xor118 = OperatorPOWL(operator=Operator.XOR, children=[transitions[129], SilentTransition()])

xor119 = OperatorPOWL(operator=Operator.XOR, children=[transitions[130], SilentTransition()])

xor120 = OperatorPOWL(operator=Operator.XOR, children=[transitions[131], SilentTransition()])

xor121 = OperatorPOWL(operator=Operator.XOR, children=[transitions[132], SilentTransition()])

xor122 = OperatorPOWL(operator=Operator.XOR, children=[transitions[133], SilentTransition()])

xor123 = OperatorPOWL(operator=Operator.XOR, children=[transitions[134], SilentTransition()])

xor124 = OperatorPOWL(operator=Operator.XOR, children=[transitions[135], SilentTransition()])

xor125 = OperatorPOWL(operator=Operator.XOR, children=[transitions[136], SilentTransition()])

xor126 = OperatorPOWL(operator=Operator.XOR, children=[transitions[137], SilentTransition()])

xor127 = OperatorPOWL(operator=Operator.XOR, children=[transitions[138], SilentTransition()])

xor128 = OperatorPOWL(operator=Operator.XOR, children=[transitions[139], SilentTransition()])

xor129 = OperatorPOWL(operator=Operator.XOR, children=[transitions[140], SilentTransition()])

xor130 = OperatorPOWL(operator=Operator.XOR, children=[transitions[141], SilentTransition()])

xor131 = OperatorPOWL(operator=Operator.XOR, children=[transitions[142], SilentTransition()])

xor132 = OperatorPOWL(operator=Operator.XOR, children=[transitions[143], SilentTransition()])

xor133 = OperatorPOWL(operator=Operator.XOR, children=[transitions[144], SilentTransition()])

xor134 = OperatorPOWL(operator=Operator.XOR, children=[transitions[145], SilentTransition()])

xor135 = OperatorPOWL(operator=Operator.XOR, children=[transitions[146], SilentTransition()])

xor136 = OperatorPOWL(operator=Operator.XOR, children=[transitions[147], SilentTransition()])

xor137 = OperatorPOWL(operator=Operator.XOR, children=[transitions[148], SilentTransition()])

xor138 = OperatorPOWL(operator=Operator.XOR, children=[transitions[149], SilentTransition()])

xor139 = OperatorPOWL(operator=Operator.XOR, children=[transitions[150], SilentTransition()])

xor140 = OperatorPOWL(operator=Operator.XOR, children=[transitions[151], SilentTransition()])

xor141 = OperatorPOWL(operator=Operator.XOR, children=[transitions[152], SilentTransition()])

xor142 = OperatorPOWL(operator=Operator.XOR, children=[transitions[153], SilentTransition()])

xor143 = OperatorPOWL(operator=Operator.XOR, children=[transitions[154], SilentTransition()])

xor144 = OperatorPOWL(operator=Operator.XOR, children=[transitions[155], SilentTransition()])

xor145 = OperatorPOWL(operator=Operator.XOR, children=[transitions[156], SilentTransition()])

xor146 = OperatorPOWL(operator=Operator.XOR, children=[transitions[157], SilentTransition()])

xor147 = OperatorPOWL(operator=Operator.XOR, children=[transitions[158], SilentTransition()])

xor148 = OperatorPOWL(operator=Operator.XOR, children=[transitions[159], SilentTransition()])

xor149 = OperatorPOWL(operator=Operator.XOR, children=[transitions[160], SilentTransition()])

xor150 = OperatorPOWL(operator=Operator.XOR, children=[transitions[161], SilentTransition()])

xor151 = OperatorPOWL(operator=Operator.XOR, children=[transitions[162], SilentTransition()])

xor152 = OperatorPOWL(operator