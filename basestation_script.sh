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
 

#look for noaa-apt, if not present, download
#https://github.com/martinber/noaa-apt/
if [ -f noaa-apt/noaa-apt ]; then
	echo "noaa-apt exists"
else
	mkdir audio
	mkdir img
	mkdir noaa-apt
	cd noaa-apt/
	wget https://github.com/martinber/noaa-apt/releases/download/v1.2.0/noaa-apt-1.2.0-x86_64-linux-gnu-nogui.zip
	unzip *.zip
	echo "noaa-apt fetched"
	rm -rf *.zip
	cd ../
fi

rm -rf audio/*

#enable alsa loopback
sudo modprobe snd-aloop

#create a loopback from udp to alsa loopback
nc -l -u 7355 | aplay -r 11025 -f S16_LE -t raw -c 1 -D hw:Loopback,0,1 &
echo $! >> save_pid.txt

#record the loopback via ffmpeg 
ffmpeg -ar 11025 -f alsa -ac 1 -i hw:Loopback,1,1 -vn -f segment -segment_time 35 -strftime 1  "audio/recording-%Y-%m-%d_%H-%M-%S.wav" &
echo $! >> save_pid.txt

#start gnuradio script
./top_block.py &
echo $! >> save_pid.txt

#starts a loop that checks for new files generated by ffmpeg
echo "init of inotify"
echo "init of inotify"

inotifywait -m -q -e create -r --format "%:e %w%f" audio/ | while read file

do
cdate=$(date +"%Y-%m-%d-%H:%M:%S")
echo $cdate
sleep 1
unset -v latest
for file in audio/*; do
  [[ $file -nt $latest ]] && latest=$file
done
echo $latest
./noaa-apt/noaa-apt $latest -o img/$cdate.png
rm -rf $latest
done
