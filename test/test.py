import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await Timer(20, unit="us")
    dut.rst_n.value = 1
    await Timer(20, unit="us")

    dut._log.info("Test project behavior")

    # CASE 1: 1 + 0 + 0 = 1 (Sum=1, Cout=0)
    # Binary: 00000001 (Decimal 1)
    dut.ui_in.value = 1 
    await Timer(10, unit="us")
    assert dut.uo_out.value == 1

    # CASE 2: 1 + 1 + 0 = 2 (Sum=0, Cout=1)
    # Binary: 00000010 (Decimal 2)
    dut.ui_in.value = 3 # bits 0 and 1 are high
    await Timer(10, unit="us")
    assert dut.uo_out.value == 2

    # CASE 3: 1 + 1 + 1 = 3 (Sum=1, Cout=1)
    # Binary: 00000011 (Decimal 3)
    dut.ui_in.value = 7 # bits 0, 1, and 2 are high
    await Timer(10, unit="us")
    assert dut.uo_out.value == 3

    dut._log.info("Finished all tests successfully!")
