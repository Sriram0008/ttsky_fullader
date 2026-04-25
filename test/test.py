import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await Timer(20, units="us")
    dut.rst_n.value = 1
    await Timer(20, units="us")

    dut._log.info("Test project behavior")

    # Test Case 1: 1 + 1 + 0 (Cin) = 2 (Binary 10)
    # A=ui[0], B=ui[1], Cin=ui[2]
    dut.ui_in.value = 0b00000011 # A=1, B=1, Cin=0
    await Timer(10, units="us")
    # Expected: Sum=0 (uo[0]), Cout=1 (uo[1]) -> Binary 00000010 (Decimal 2)
    assert dut.uo_out.value == 2

    # Test Case 2: 1 + 1 + 1 (Cin) = 3 (Binary 11)
    dut.ui_in.value = 0b00000111 # A=1, B=1, Cin=1
    await Timer(10, units="us")
    # Expected: Sum=1 (uo[0]), Cout=1 (uo[1]) -> Binary 00000011 (Decimal 3)
    assert dut.uo_out.value == 3

    dut._log.info("Finished test!")
