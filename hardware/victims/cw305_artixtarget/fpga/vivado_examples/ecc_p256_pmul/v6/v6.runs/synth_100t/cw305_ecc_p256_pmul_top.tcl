# 
# Synthesis run script generated by Vivado
# 

set TIME_start [clock seconds] 
proc create_report { reportName command } {
  set status "."
  append status $reportName ".fail"
  if { [file exists $status] } {
    eval file delete [glob $status]
  }
  send_msg_id runtcl-4 info "Executing : $command"
  set retval [eval catch { $command } msg]
  if { $retval != 0 } {
    set fp [open $status w]
    close $fp
    send_msg_id runtcl-5 warning "$msg"
  }
}
create_project -in_memory -part xc7a100tftg256-2

set_param project.singleFileAddWarning.threshold 0
set_param project.compositeFile.enableAutoGeneration 0
set_param synth.vivado.isSynthRun true
set_msg_config -source 4 -id {IP_Flow 19-2162} -severity warning -new_severity info
set_property webtalk.parent_dir Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.cache/wt [current_project]
set_property parent.project_path Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.xpr [current_project]
set_property XPM_LIBRARIES {XPM_CDC XPM_MEMORY} [current_project]
set_property default_lib xil_defaultlib [current_project]
set_property target_language Verilog [current_project]
set_property ip_cache_permissions {read write} [current_project]
set_property include_dirs {
  Y:/fpga/common
  Y:/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve
  Y:/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel
  Y:/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor
  Y:/fpga/vivado_examples/ecc_p256_pmul/hdl
} [current_fileset]
set_property verilog_define {ILA_REG ILA_CRYPTO} [current_fileset]
read_verilog -library xil_defaultlib {
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel/generic/adder32_generic.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel/adder32_wrapper.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel/generic/adder47_generic.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel/adder47_wrapper.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/util/bram_1rw_1ro_readfirst.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/rom/brom_p256_delta.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/rom/brom_p256_h_x.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/rom/brom_p256_h_y.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/rom/brom_p256_one.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/rom/brom_p256_q.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/rom/brom_p256_zero.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/common/cdc_pulse.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/common/clocks.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/curve_dbl_add_256.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/curve_mul_256.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/vivado_examples/ecc_p256_pmul/hdl/cw305_reg_pmul.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/common/cw305_usb_reg_fe.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel/generic/mac16_generic.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel/mac16_wrapper.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor/helper/modinv_helper_copy.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor/helper/modinv_helper_init.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor/helper/modinv_helper_invert_compare.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor/helper/modinv_helper_invert_precalc.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor/helper/modinv_helper_invert_update.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor/helper/modinv_helper_reduce_precalc.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor/helper/modinv_helper_reduce_update.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_adder.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_invertor/modular_invertor.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_multiplier_256.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_reductor_256.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/modular/modular_subtractor.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/multiword/mw_comparator.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/multiword/mw_mover.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel/generic/subtractor32_generic.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/lowlevel/subtractor32_wrapper.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/uop/uop_add_rom.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/uop/uop_conv_rom.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/uop/uop_dbl_rom.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/cryptosrc/cryptech/ecdsa256-v1/rtl/curve/uop/uop_init_rom.v
  Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/sources_1/imports/fpga/vivado_examples/ecc_p256_pmul/hdl/cw305_ecc_p256_pmul_top.v
}
read_ip -quiet Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_0/ip/ila_0/ila_0.xci
set_property used_in_synthesis false [get_files -all y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_0/ip/ila_0/ila_v6_2/constraints/ila_impl.xdc]
set_property used_in_implementation false [get_files -all y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_0/ip/ila_0/ila_v6_2/constraints/ila_impl.xdc]
set_property used_in_implementation false [get_files -all y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_0/ip/ila_0/ila_v6_2/constraints/ila.xdc]
set_property used_in_implementation false [get_files -all y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_0/ip/ila_0/ila_0_ooc.xdc]

read_ip -quiet Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_1/ip/ila_1/ila_1.xci
set_property used_in_synthesis false [get_files -all y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_1/ip/ila_1/ila_v6_2/constraints/ila_impl.xdc]
set_property used_in_implementation false [get_files -all y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_1/ip/ila_1/ila_v6_2/constraints/ila_impl.xdc]
set_property used_in_implementation false [get_files -all y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_1/ip/ila_1/ila_v6_2/constraints/ila.xdc]
set_property used_in_implementation false [get_files -all y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/ila_1/ip/ila_1/ila_1_ooc.xdc]

# Mark all dcp files as not used in implementation to prevent them from being
# stitched into the results of this synthesis run. Any black boxes in the
# design are intentionally left as such for best results. Dcp files will be
# stitched into the design at a later time, either when this synthesis run is
# opened, or when it is stitched into a dependent implementation run.
foreach dcp [get_files -quiet -all -filter file_type=="Design\ Checkpoint"] {
  set_property used_in_implementation false $dcp
}
read_xdc Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/constrs_1/imports/ecc_p256_pmul/cw305_main.xdc
set_property used_in_implementation false [get_files Y:/fpga/vivado_examples/ecc_p256_pmul/v6/v6.srcs/constrs_1/imports/ecc_p256_pmul/cw305_main.xdc]

set_param ips.enableIPCacheLiteLoad 1
close [open __synthesis_is_running__ w]

synth_design -top cw305_ecc_p256_pmul_top -part xc7a100tftg256-2


# disable binary constraint mode for synth run checkpoints
set_param constraints.enableBinaryConstraints false
write_checkpoint -force -noxdef cw305_ecc_p256_pmul_top.dcp
create_report "synth_100t_synth_report_utilization_0" "report_utilization -file cw305_ecc_p256_pmul_top_utilization_synth.rpt -pb cw305_ecc_p256_pmul_top_utilization_synth.pb"
file delete __synthesis_is_running__
close [open __synthesis_is_complete__ w]
