# MH Crafting Planner

github copilotを試している。


# network

docker network create app-network --subnet=172.24.1.0/24 --gateway=172.24.1.1
docker network create supabase-network --subnet=172.24.2.0/24 --gateway=172.24.2.1

# port 

supabase: 8020

frontend: 3020
website: 3021
backend/core: 8021
backend/planner: 8022
backend/inventory: 8023

