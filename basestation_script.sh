#Script to be run by the basestation receiving the signal
#This script does the following
#Recives 3 UDP streams from the splitterscript
#processes these with gnuradio selecting the signal with highest power
#  and then runs it through a WBFM converter sending audio to udp://localhost:7355
#netcat pipes the audio to alsa that plays it on a loopback device that fmpeg can read
#ffmpeg creates 5 second snippets of the audio for processing
#		TODO!!!!
#noaa-apt (insert git link) processes these to a image slice that will be stiched together creating a live display.

#
rm -rf save_pid.txt

#enable alsa loopback
sudo modprobe snd-aloop

#create a loopback from udp to alsa loopback
nc -l -u 7355 | aplay -r 11025 -f S16_LE -t raw -c 1 -D hw:Loopback,0,1 &
echo $! >> save_pid.txt

#record the loopback via ffmpeg 
ffmpeg -ar 11025 -f alsa -ac 1 -i hw:Loopback,1,1 -vn -f segment -segment_time 5  "recording-%03d.wav" &
echo $! >> save_pid.txt

#start gnuradio script
./top_block.py &
echo $! >> save_pid.txt
