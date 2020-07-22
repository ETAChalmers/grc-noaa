#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: udp-recive
# Generated: Wed Jul 22 11:23:11 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
import threading
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "udp-recive")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("udp-recive")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 850e3
        self.dec = dec = 25
        self.freq_0 = freq_0 = 137.50625e6
        self.channel_nr = channel_nr = 0
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

        def _channel_nr_probe():
            while True:
                val = self.Probe_channel.get_value()
                try:
                    self.set_channel_nr(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _channel_nr_thread = threading.Thread(target=_channel_nr_probe)
        _channel_nr_thread.daemon = True
        _channel_nr_thread.start()

        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=11025,
                decimation=34000,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_short,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.1)
        self.qtgui_number_sink_0.set_title("Selected channel")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 2)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.probe_channel = blocks.probe_signal_s()
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('/home/david/Music/foobar', 1, 11025, 16)
        self.blocks_udp_source_0_2 = blocks.udp_source(gr.sizeof_gr_complex*1, '0.0.0.0', 1232, 1472, True)
        self.blocks_udp_source_0_1 = blocks.udp_source(gr.sizeof_gr_complex*1, '0.0.0.0', 1230, 1472, True)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, '0.0.0.0', 1231, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_float*1, 'localhost', 7355, 1316, True)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_float*1, 3)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_moving_average_2_0 = blocks.moving_average_ff(4000, 1, 4000)
        self.blocks_moving_average_2 = blocks.moving_average_ff(4000, 1, 4000)
        self.blocks_moving_average_1 = blocks.moving_average_ff(4000, 1, 4000)
        self.blocks_complex_to_mag_squared_0_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(3)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=channel_nr,
        	output_index=0,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=bandwidth,
        	audio_decimation=1,
        )
        self.NOAA19_fall = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq_0+NOAA19, #fc
        	Out_samprate, #bw
        	"NOAA19 (stream 0)", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	False, #plottime
        	False, #plotconst
        )
        self.NOAA19_fall.set_update_time(1.0/10)
        self._NOAA19_fall_win = sip.wrapinstance(self.NOAA19_fall.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._NOAA19_fall_win)

        self.NOAA19_fall.enable_rf_freq(True)



        self.NOAA18_fall = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq_0+NOAA18, #fc
        	Out_samprate, #bw
        	"NOAA18 (stream 1)", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	False, #plottime
        	False, #plotconst
        )
        self.NOAA18_fall.set_update_time(1.0/10)
        self._NOAA18_fall_win = sip.wrapinstance(self.NOAA18_fall.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._NOAA18_fall_win)

        self.NOAA18_fall.enable_rf_freq(True)



        self.NOAA15_fall = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq_0+NOAA15, #fc
        	samp_rate, #bw
        	"NOAA15 (stream 2)", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	False, #plottime
        	False, #plotconst
        )
        self.NOAA15_fall.set_update_time(1.0/10)
        self._NOAA15_fall_win = sip.wrapinstance(self.NOAA15_fall.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._NOAA15_fall_win)

        self.NOAA15_fall.enable_rf_freq(True)




        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.probe_channel, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_moving_average_2, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.blocks_moving_average_2_0, 0))
        self.connect((self.blocks_moving_average_1, 0), (self.blocks_streams_to_vector_0, 0))
        self.connect((self.blocks_moving_average_2, 0), (self.blocks_streams_to_vector_0, 1))
        self.connect((self.blocks_moving_average_2_0, 0), (self.blocks_streams_to_vector_0, 2))
        self.connect((self.blocks_streams_to_vector_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.NOAA19_fall, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_udp_source_0_1, 0), (self.NOAA18_fall, 0))
        self.connect((self.blocks_udp_source_0_1, 0), (self.blks2_selector_0, 1))
        self.connect((self.blocks_udp_source_0_1, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.blocks_udp_source_0_2, 0), (self.NOAA15_fall, 0))
        self.connect((self.blocks_udp_source_0_2, 0), (self.blks2_selector_0, 2))
        self.connect((self.blocks_udp_source_0_2, 0), (self.blocks_complex_to_mag_squared_0_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_wavfile_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Out_samprate(self.samp_rate/self.dec)
        self.NOAA15_fall.set_frequency_range(self.freq_0+self.NOAA15, self.samp_rate)

    def get_dec(self):
        return self.dec

    def set_dec(self, dec):
        self.dec = dec
        self.set_Out_samprate(self.samp_rate/self.dec)

    def get_freq_0(self):
        return self.freq_0

    def set_freq_0(self, freq_0):
        self.freq_0 = freq_0
        self.NOAA19_fall.set_frequency_range(self.freq_0+self.NOAA19, self.Out_samprate)
        self.NOAA18_fall.set_frequency_range(self.freq_0+self.NOAA18, self.Out_samprate)
        self.NOAA15_fall.set_frequency_range(self.freq_0+self.NOAA15, self.samp_rate)

    def get_channel_nr(self):
        return self.channel_nr

    def set_channel_nr(self, channel_nr):
        self.channel_nr = channel_nr
        self.blks2_selector_0.set_input_index(int(self.channel_nr))

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth

    def get_RF_gain(self):
        return self.RF_gain

    def set_RF_gain(self, RF_gain):
        self.RF_gain = RF_gain

    def get_Out_samprate(self):
        return self.Out_samprate

    def set_Out_samprate(self, Out_samprate):
        self.Out_samprate = Out_samprate
        self.NOAA19_fall.set_frequency_range(self.freq_0+self.NOAA19, self.Out_samprate)
        self.NOAA18_fall.set_frequency_range(self.freq_0+self.NOAA18, self.Out_samprate)

    def get_NOAA19(self):
        return self.NOAA19

    def set_NOAA19(self, NOAA19):
        self.NOAA19 = NOAA19
        self.NOAA19_fall.set_frequency_range(self.freq_0+self.NOAA19, self.Out_samprate)

    def get_NOAA18(self):
        return self.NOAA18

    def set_NOAA18(self, NOAA18):
        self.NOAA18 = NOAA18
        self.NOAA18_fall.set_frequency_range(self.freq_0+self.NOAA18, self.Out_samprate)

    def get_NOAA15(self):
        return self.NOAA15

    def set_NOAA15(self, NOAA15):
        self.NOAA15 = NOAA15
        self.NOAA15_fall.set_frequency_range(self.freq_0+self.NOAA15, self.samp_rate)

    def get_IF_gain(self):
        return self.IF_gain

    def set_IF_gain(self, IF_gain):
        self.IF_gain = IF_gain


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
