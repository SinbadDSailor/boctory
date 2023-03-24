#!/bin/bash

current_version="0.1"

mainfunc () {
    sleep 1
    banner_print
    sleep 1
    while :
    do
        main_menu
        read -r -p "Enter your option: " main_option

        case $main_option in
            1) echo "Reserved";;
            2) python3 test.py | tee test.txt;;
            3) db_man;;
            4) adv_options;;
            5) echo "[~] Exiting.." && sleep 1 && break;;
            *) echo "Invalid input!"
            

        esac


    done
}


banner_print () {
    echo ""
    echo "██████╗  ██████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗"
    echo "██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝"
    echo "██████╔╝██║   ██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ "
    echo "██╔══██╗██║   ██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  "
    echo "██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   "
    echo "╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   "
    echo "Version: $current_version"
    echo "============================================================"
}

main_menu () {
    echo ""
    echo "    MAIN MENU"
    echo "[1] Reserved"
    echo "[2] Python test run"
    echo "[3] Database Management"
    echo "[4] Advanced Options"
    echo "[5] Exit"
    echo "======================="
}

adv_options_menu () {

    echo ""
    echo "Main-Menu/Advanced-Options"
    echo "[1] Setup Selenium"
    echo "[2] Back"
    echo "======================="

}
db_man_menu () {

    echo ""
    echo "Main-Menu/Database-Management"
    echo "[1] Setup database"
    echo "[2] Back"
    echo "======================="

}

db_man () {

    while :
    do
        db_man_menu
        read -r -p "Enter your option: " db_man_option

        case $db_man_option in
            1) python3 db_setup.py;;
            2) break;;
            *) echo "Invalid input!"
            
        esac

    done

}

adv_options () {

    while :
    do
        adv_options_menu
        read -r -p "Enter your option: " adv_opt_option

        case $adv_opt_option in
            1) source driver_setup.sh;;
            2) break;;
            *) echo "Invalid input!"
            
        esac

    done

}

mainfunc