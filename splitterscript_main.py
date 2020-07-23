#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: NOAA_freq_splitter
# Generated: Sun Apr 12 12:54:49 2020
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "NOAA_freq_splitter")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 850e3
        self.dec = dec = 25
        self.freq_0 = freq_0 = 137.50625e6
        self.bandwidth = bandwidth = 34e3
        self.RF_gain = RF_gain = 40
        self.Out_samprate = Out_samprate = samp_rate/dec
        self.NOAA19 = NOAA19 = -0.40625e6
        self.NOAA18 = NOAA18 = 0.40625e6
        self.NOAA15 = NOAA15 = 0.11375e6
        self.IF_gain = IF_gain = 40

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq_0, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(RF_gain, 0)
        self.osmosdr_source_0.set_if_gain(IF_gain, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0_1 = filter.fir_filter_ccf(dec, firdes.low_pass(
        	1, samp_rate, bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(dec, firdes.low_pass(
        	1, samp_rate, bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(dec, firdes.low_pass(
        	1, samp_rate, bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_udp_sink_0_0_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, '192.168.30.64', 1232, 4000, True)
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, '192.168.30.64', 1231, 4000, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, '192.168.30.64', 1230, 4000, True)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -NOAA15, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -NOAA18, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -NOAA19, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_udp_sink_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_udp_sink_0_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1, 1))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.set_Out_samprate(self.samp_rate/self.dec)

    def get_dec(self):
        return self.dec

    def set_dec(self, dec):
        self.dec = dec
        self.set_Out_samprate(self.samp_rate/self.dec)

    def get_freq_0(self):
        return self.freq_0

    def set_freq_0(self, freq_0):
        self.freq_0 = freq_0
        self.osmosdr_source_0.set_center_freq(self.freq_0, 0)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth, 3e3, firdes.WIN_HAMMING, 6.76))

    def get_RF_gain(self):
        return self.RF_gain

    def set_RF_gain(self, RF_gain):
        self.RF_gain = RF_gain
        self.osmosdr_source_0.set_gain(self.RF_gain, 0)

    def get_Out_samprate(self):
        return self.Out_samprate

    def set_Out_samprate(self, Out_samprate):
        self.Out_samprate = Out_samprate

    def get_NOAA19(self):
        return self.NOAA19

    def set_NOAA19(self, NOAA19):
        self.NOAA19 = NOAA19
        self.analog_sig_source_x_0.set_frequency(-self.NOAA19)

    def get_NOAA18(self):
        return self.NOAA18

    def set_NOAA18(self, NOAA18):
        self.NOAA18 = NOAA18
        self.analog_sig_source_x_0_0.set_frequency(-self.NOAA18)

    def get_NOAA15(self):
        return self.NOAA15

    def set_NOAA15(self, NOAA15):
        self.NOAA15 = NOAA15
        self.analog_sig_source_x_0_1.set_frequency(-self.NOAA15)

    def get_IF_gain(self):
        return self.IF_gain

    def set_IF_gain(self, IF_gain):
        self.IF_gain = IF_gain
        self.osmosdr_source_0.set_if_gain(self.IF_gain, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
