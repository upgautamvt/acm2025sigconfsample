import matplotlib.pyplot as plt

participants = ["Central A" + "\n\n" + "paired with B share the same shared key PK (aka Link Key)", "Peripheral B" + "\n\n" + "paired with A share the same shared key PK (aka Link Key)"]
x_pos = [0.5, 4.5]  # moved much farther apart

messages = [
    ("A", "B", "$1.\\ \\mathrm{BA}_{A}$ (48 bits long Bluetooth Address of A), LSC (i.e., request LSC capabilities)"),
    ("B", "A", "$2.\\ \\mathrm{BA}_{B}$ (48 bits long Bluetooth Address of B), LSC/SC (i.e., B supports both LSC and SC, but has to agree on LSC)"),
    ("A", "B", "$3.\\ \\mathrm{AC}_{A}$ = random_128bit() (A's Authentication Challenge (aka AU_RAND or authentication nonce) to B)"),
    ("B", "", "                                                  " + "$\\mathrm{X} = \\mathrm{e}_1(PK, \\mathrm{AC}_A, \\mathrm{BA}_B)$ (128-bits)" + "\n" + "                                   " + "$\\mathrm{CR}_B = \\mathrm{MSB}_{32}(X)$"),
    ("A", "", "                                                  " + "$\\mathrm{X} = \\mathrm{e}_1(PK, \\mathrm{AC}_A, \\mathrm{BA}_B)$ (128-bits)" + "\n" + "                                   " + "$\\overline{\\mathrm{CR}_B} = \\mathrm{MSB}_{32}(X)$"),    
    ("B", "A", "$4.\\ \\mathrm{CR}_{B}$ (Challenge Response (aka SRES) from B)"),
    ("A", "", "A verifies $\\mathrm{CR}_{B}$ if $\\overline{\\mathrm{CR}_B} = \\mathrm{CR}_B$"),
    ("A", "B", "$5.\\ \\mathrm{SE}_{A}$ (A's Session Entropy needed for SK)" + "\n" + " " + "calculated using (in pseudocode) controller.RNG.generate(128), also 128-bits)"),
    ("B", "A", "$6.$ Accept Entropy"),
    ("A", "B", "$7.\\ \\mathrm{SD}_{A}$ (A's Session Diversifier (aka EN_RAND or Nonce))" + "\n" + "calculated using (in pseudocode) controller.RNG.generate(128), also 128-bits"),
    ("B", "A", "$8.$ Accept Diversifier"),
    ("A", "", "$\\mathrm{SK} = \\mathrm{f}_{KDF-LSC}(PK,\\ \\mathrm{BA}_{B},\\ \\mathrm{AC}_{A},\\ \\mathrm{SE}_{A},\\ \\mathrm{SD}_{A})$" + "\n\n                             " + "$COF =  \\mathrm{LSB}_{96}(X)$" + "\n                                        " + "$ISK = e_3(PK, SD_A, COF)$" + "\n                               " + "$SK = e_s(ISK, SE_A)$"),
    ("B", "", "$\\mathrm{SK} = \\mathrm{f}_{KDF-LSC}(PK,\\ \\mathrm{BA}_{B},\\ \\mathrm{AC}_{A},\\ \\mathrm{SE}_{A},\\ \\mathrm{SD}_{A})$" + "\n\n                             " + "$COF =  \\mathrm{LSB}_{96}(X)$" + "\n                                        " + "$ISK = e_3(PK, SD_A, COF)$" + "\n                               " + "$SK = e_s(ISK, SE_A)$"),
    ("A", "B", "$9.\\ \\text{ciphertext}\\ \\mathrm{ct}_1 = E_0(m_1, \\mathrm{SK})$" + "\n" + "where m₁ message, E₀ encryption algorithm"),
    ("B", "A", "$10.\\ \\text{ciphertext}\\ \\mathrm{ct}_2 = E_0(m_2, \\mathrm{SK})$" + "\n" + "where m₂ message, E₀ encryption algorithm"),
]

fig, ax = plt.subplots(figsize=(10, 12))

# Draw lifelines with smaller font for participant names
for i, p in enumerate(participants):
    color = 'blue' if i == 1 else 'black'
    ax.plot([x_pos[i], x_pos[i]], [0, -42], color=color, lw=1)  # Reduced line width from 2 to 1, increased height more
    
    # Split the text by newline and format differently
    parts = p.split('\n')
    if len(parts) == 3:  # Now we have 3 parts due to double newline
        # Main title (Central A / Peripheral B) - bold and larger
        ax.text(x_pos[i], 0.3, parts[0], ha='center', fontsize=10, weight='bold', color=color)
        # Empty line (parts[1] is empty due to double newline)
        # Subtitle (paired with...) - normal weight and smaller
        ax.text(x_pos[i], 0.0, parts[2], ha='center', fontsize=6, weight='normal', color=color)
    elif len(parts) == 2:
        # Main title (Central A / Peripheral B) - bold and larger
        ax.text(x_pos[i], 0.3, parts[0], ha='center', fontsize=10, weight='bold', color=color)
        # Subtitle (paired with...) - normal weight and smaller
        ax.text(x_pos[i], 0.1, parts[1], ha='center', fontsize=6, weight='normal', color=color)
    else:
        # Fallback if no newline
        ax.text(x_pos[i], 0.3, p, ha='center', fontsize=10, weight='bold', color=color)

y = 0
y_step = -2

for idx, (sender, receiver, msg) in enumerate(messages):
    y += y_step
    # Add extra offset for the last message (step 12) to move it down
    extra_offset = -0.3 if idx == len(messages) - 1 else 0
    
    # Set colors based on sender
    if sender == "A":
        arrow_color = 'black'
        text_color = 'black'
    else:  # sender == "B"
        arrow_color = 'blue'
        text_color = 'blue'
    
    if sender == receiver:
        x = x_pos[0] if sender == "A" else x_pos[1]
        ax.text(x + 0.1, y + 0.5 + extra_offset, msg, fontsize=8, va='center', color=text_color)
    elif receiver == "":  # no arrow, label centered below lifeline A
        x = x_pos[0] if sender == "A" else x_pos[1]
        ax.text(x, y + 0.5 + extra_offset, msg, fontsize=8, va='center', ha='center', color=text_color)
    else:
        x_start = x_pos[0] if sender == "A" else x_pos[1]
        x_end = x_pos[0] if receiver == "A" else x_pos[1]
        ax.annotate(
            '',
            xy=(x_end, y),
            xytext=(x_start, y),
            arrowprops=dict(arrowstyle="->", lw=1.5, color=arrow_color)
        )
        ax.text((x_start + x_end) / 2, y + 0.5 + extra_offset, msg, ha='center', fontsize=8, color=text_color)

ax.set_xlim(0, 4.5)
ax.set_ylim(y_step * (len(messages) + 2), 1)
ax.axis('off')


plt.savefig('../figures/lsc.png', bbox_inches='tight', dpi=600)

