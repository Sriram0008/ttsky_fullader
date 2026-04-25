## How it works
This project is a hardware implementation of a 1-bit full adder. It uses combinational logic to perform binary addition. 
- **Logic:** It calculates the Sum using $A \oplus B \oplus Cin$ and the Carry-out (Cout) using $(A \cdot B) + (Cin \cdot (A \oplus B))$.
- **Inputs:** The bits to be added are mapped to the first three input pins ($ui[0]$, $ui[1]$, $ui[2]$).
- **Outputs:** The results are sent to the first two output pins ($uo[0]$ for Sum, $uo[1]$ for Cout).

## How to test
After power-on and reset:
1. Apply logic levels to the input pins:
   - `ui[0]`: Input A
   - `ui[1]`: Input B
   - `ui[2]`: Carry-in (Cin)
2. Observe the output pins:
   - `uo[0]`: Sum bit
   - `uo[1]`: Carry-out bit
3. Verify against the Full Adder truth table (e.g., if all three inputs are 1, both Sum and Cout should be 1).

## External hardware
No external hardware is required. You can test this using the onboard switches and LEDs on the Tiny Tapeout demo board.
