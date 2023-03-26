#!/bin/bash

current_version="0.1"

#colors ---------->
tail="\e[0m"
blue="\e[1;34m"
tblue="\e[0;34m"
green="\e[1;32m"
red="\e[1;31m"
#colors ---------/>

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
            5) echo -e "$red[~] Exiting..$tail" && sleep 1 && break;;
            *) echo -e "${red}Invalid input! $tail"
            
        esac


    done
}


banner_print () {
    echo ""
    echo -e "$blue██████╗  ██████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗"
    echo "██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝"
    echo "██████╔╝██║   ██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ "
    echo "██╔══██╗██║   ██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  "
    echo "██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   "
    echo "╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   "
    echo -e "$green Version:$tail $red$current_version $tail"
    echo "============================================================"
}

main_menu () {
    echo ""
    echo -e "$blue      MAIN MENU $tail"
    echo "[1] Reserved"
    echo "[2] Python test run"
    echo "[3] Database Management"
    echo "[4] Advanced Options"
    echo "[5] Exit"
    echo "======================="
}

adv_options_menu () {

    echo ""
    echo -e "${tblue}Main-Menu/Advanced-Options $tail"
    echo "[1] Setup Selenium"
    echo "[2] Back"
    echo "======================="

}
db_man_menu () {

    echo ""
    echo -e "${tblue}Main-Menu/Database-Management $tail"
    echo "[1] Setup database"
    echo "[2] Input options"
    echo "[3] Output options"
    echo "[4] Back"
    echo "======================="

}

input_options_menu () {

    echo ""
    echo -e "${tblue}Main-Menu/Database-Management/Input-Options $tail"
    echo "[1] Input manually"
    echo "[2] Input from CSV"
    echo "[3] Input from JSON"
    echo "[4] Back"
    echo "======================="

}

output_options_menu () {

    echo ""
    echo -e "${tblue}Main-Menu/Database-Management/Output-Options $tail"
    echo "[1] Output to terminal"
    echo "[2] Output to CSV"
    echo "[3] Output to JSON"
    echo "[4] Back"
    echo "======================="

}

output_options () {

    while :
    do
        output_options_menu
        read -r -p "Enter your option: " output_option

        case $output_option in 
            1) python3 term_output.py;;
            2) python3 csv_output.py;;
            3) python3 json_output.py;;
            4) break;;
            *) echo -e "${red}Invalid input! $tail"
        esac



    done
}

input_options () {

    while :
    do
        input_options_menu
        read -r -p "Enter your option: " input_option

        case $input_option in 
            1) python3 input.py;;
            2) python3 csv_input.py;;
            3) python3 json_input.py;;
            4) break;;
            *) echo -e "${red}Invalid input! $tail"
        esac



    done
}

db_man () {

    while :
    do
        db_man_menu
        read -r -p "Enter your option: " db_man_option

        case $db_man_option in
            1) python3 db_setup.py;;
            2) input_options;;
            3) output_options;;
            4) break;;
            *) echo -e "${red}Invalid input! $tail"
            
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
            *) echo -e "${red}Invalid input! $tail"
            
        esac

    done

}

mainfunc