project_steps_texts = [
    {
        "title": "Overview",
        "content": """**Designing a Voltage Divider: Reading High-Voltage Signals Safely**

**Project Objectives:**
- Learn how voltage dividers work and where they are used in electronics and sensor circuits.
- Apply Ohm’s Law and voltage division principles to reduce input voltages to safe levels.
- Evaluate design trade-offs such as power dissipation and output stability.
- Design and analyze a realistic voltage divider circuit for a sensor input scenario.
"""
    },
    {
        "title": "Part 1: Understanding Voltage Division (20%)",
        "content": """**Task 1:**
- Define a voltage divider and explain its purpose.
- Draw a basic voltage divider circuit with two resistors \( R_1 \) and \( R_2 \) in series across a voltage source \( V_{in} \).

**Formula:**
\[
V_{out} = V_{in} \\cdot \\frac{R_2}{R_1 + R_2}
\]

**Guiding Questions:**
- Why is \( V_{out} \) always less than \( V_{in} \)?
- What happens to \( V_{out} \) if \( R_2 \\gg R_1 \)? What about the opposite?
"""
    },
    {
        "title": "Part 2: Designing for a Target Output (25%)",
        "content": """**Task 2:**
- You are given a sensor that outputs up to 12 V, but your microcontroller can only read up to 5 V.
- Your job is to design a voltage divider that converts 12 V to 5 V at maximum input.

**Calculation Task:**
- Choose appropriate values for \( R_1 \) and \( R_2 \) such that:
  \[
  V_{out} = 5~\\text{V} \\text{ when } V_{in} = 12~\\text{V}
  \]

- Justify your resistor choices. You may assume common resistor values (e.g., 1 kΩ, 2.2 kΩ, 4.7 kΩ, 10 kΩ, etc.)

**Guiding Questions:**
- Does your divider meet the target exactly? What rounding or real-world resistor issues might arise?
- What happens if you reverse \( R_1 \) and \( R_2 \)?
"""
    },
    {
        "title": "Part 3: Power Dissipation and Safety (25%)",
        "content": """**Task 3:**
- Calculate the total current drawn from the voltage source:
  \[
  I = \\frac{V_{in}}{R_1 + R_2}
  \]

- Calculate the power dissipated in each resistor:
  \[
  P = I^2 R
  \]

**Design Task:**
- Check if the power rating of your resistors (e.g., 0.25 W) is sufficient.
- Propose safer or more efficient alternatives if necessary.

**Guiding Questions:**
- What are the risks of drawing too much current in this setup?
- How could you reduce power loss while keeping the voltage ratio?
"""
    },
    {
        "title": "Part 4: Application to Sensor Systems (20%)",
        "content": """**Task 4:**
- Describe a real-world scenario where a voltage divider is used to scale a sensor signal.
- For example, suppose you are measuring the voltage from a battery pack (up to 18 V) but your sensor input is limited to 3.3 V.

**Design Task:**
- Choose appropriate resistor values to meet this goal.
- Discuss stability and accuracy concerns, especially if the sensor input has a small internal resistance.

**Guiding Questions:**
- Why do voltage dividers become unreliable with variable load resistance?
- How can we protect the circuit if the input voltage spikes above expected levels?
"""
    },
    {
        "title": "Part 5: Synthesis & Reflection (10%)",
        "content": """**Task 5:**
- Summarize what you learned about voltage dividers and resistor-based circuit design.
- Reflect: How can understanding something this simple lead to better control systems and measurement tools?

**Bonus Consideration:**
- What alternative methods (e.g., Zener diodes, voltage regulators) could be used for voltage protection or conversion?
"""
    }
]