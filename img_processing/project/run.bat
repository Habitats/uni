@echo off
matlab -nosplash -nodesktop -minimize -r image_processing('projectimages/sweetsA02.png') -logfile log.txt
echo Running image processing in matlab... 
echo Wait until execution is done, then press any key to continue the graphical simulation in Python (and OpenGL)
pause
python graphics_legcay.py