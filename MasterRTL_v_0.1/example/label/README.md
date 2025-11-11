There is no labeled data to train the model. This issue was raised and the writers mentioned that they did not provide the data due to copyright issues. The labeled data is produced after running logic synthesis using the synopsys DC.
Since we do not have access to the Design Compiler, we are using Yosys and ABC for performing synthesis to get the labeled data. (also used abc tool to perform combinational and sequential logic optimization).
Since Yosys doesn’t have the infrastructure for producing timing and power information, we are using OpenSTA to generate the timing and power.

## Steps to follow to obtain label data:

```
$ change control to the design directory
$ yosys
$ read_verilog *.v
$ dump {top_module}
$ proc
$ hierarchy -top {top_module}
$ opt
$ synth
$ stat
$ write_verilog sub/postsynth.v
$ write_rtlil sub/postsynth.rtlil
$ design -reset
$ read_verilog *.v
$ hierarchy -top {top_module}
$ flatten
$ prep
$ synth
$ dfflibmap -liberty sg13g2_typ_1p20V_25C.lib
$ abc -D 4000 -liberty sg13g2_typ_1p20V_25C.lib
$ opt_clean
$ stat -liberty sg13g2_typ_1p20V_25C.lib
$ write_verilog sub/postmap.v
$ exit
$ sta
$ read_verilog sub/postmap.v
$ read_liberty sg13g2_typ_1p20V_25C.lib
$ link_design {top_module}
$ create_clock -name clock -period 1 {clock}
$ write_sdf sub/postmap.sdf
$ report_checks
$ report_power
$ exit

```
