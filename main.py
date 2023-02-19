#!/usr/bin/env python3
from database_management import db_main

def main():
    a = int(input("Izaberi opciju: "))

    if a == 1:
        db_main()

