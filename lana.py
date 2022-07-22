#!/usr/bin/bash

#warna
default="\033[00m"
merah="\033[31m"
hijau="\033[32m"
kuning="\033[33m"
biru="\033[34m"
birumuda="\033[35m"
ungu="\033[36m"
putih="\033[37m"


clear
echo
   echo -e ""  $merah "███╗   ██╗ ██████╗"  $merah "   ██╗     ██╗███╗   ███╗██╗████████╗"
   echo -e ""  $merah "████╗  ██║██╔═══██╗"  $merah "  ██║     ██║████╗ ████║██║╚══██╔══╝"
   echo -e ""  $merah "██╔██╗ ██║██║   ██║"  $merah "  ██║     ██║██╔████╔██║██║   ██║"      
   echo -e ""  $putih "██╔██╗ ██║██║   ██║"  $putih "  ██║     ██║██║╚██╔╝██║██║   ██║"
   echo -e ""  $putih "██║ ╚████║╚██████╔╝"  $putih "  ███████╗██║██║ ╚═╝ ██║██║   ██║"  
   echo -e ""  $putih "╚═╝  ╚═══╝ ╚═════╝"     $putih "  ╚══════╝╚═╝╚═╝     ╚═╝╚═╝   ╚═╝"  
 
   echo
   echo -e $kuning" ╔═══════════════════════════════════════════════╗"
   echo -e $kuning" ║"   "\033[34mAuther    : Lana                       "$kuning"    ║"
   echo -e $kuning" ║"   "\033[34mTeam      : Zexxy                   "$kuning"    ║"
   echo -e $kuning" ║"   "\033[32mWA : 088245059338                       "$hijau"    ║"
   echo -e $kuning" ║"   "\033[34mGithub    : https://github.com/AUTOSAFE     "$kuning"    ║"
   echo -e $kuning" ╚═══════════════════════════════════════════════╝"

   echo -e $putih
   echo -e $putih "╔════════════════════════╗"
   echo -e " ║ " "\033[1;31m By Lana Script" $putih "    ║"
   echo -e $putih "╚════════════════════════╝"


echo  $hijau"Welcome"
echo  $biru"[1] Script Bussid"
echo  $ungu"[2] Script Stumble"
echo  $birumuda"[3] Exit"


echo -e -n "pilih > ";read pil
if [ $pil = "1" ];then
  git clone https://github.com/KIPASGTS/Mass-cash-bussid &> /dev//null
  cd Mass-cash-bussid
  pip install requests
  python bussid.py
  echo "Selamat Datang di Script Bussid"
elif [ $pil = "2" ];then
  git clone https://github.com/AUTOSAFE/Lana.py &> /dev//null
  cd lana.py
  npm i
  node index
echo "selamat datang di Kontol Geming"
elif [ $pil = "3" ];then
exit
else
echo "input salah"
fi
