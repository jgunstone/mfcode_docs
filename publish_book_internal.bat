call build_book.bat
call robocopy %~dp0\book\_build J:\J4321\DigitalDesignTeam\CodeDev\mfcode_docs\_build /MIR /FFT /Z /R:1 /W:5 /MT:32