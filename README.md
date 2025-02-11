# MH Crafting Planner

github copilotを試している。


## INSTALL SUPABASE CLI

```shell
curl -LO https://github.com/supabase/cli/releases/download/v2.12.0/supabase_2.12.0_linux_amd64.deb
sudo dpkg -i supabase_2.12.0_linux_amd64.deb

supabase init
cd supabase
supabase start
```


# network

docker network create app-network --subnet=172.24.1.0/24 --gateway=172.24.1.1


# port 

supabase: 8020
frontend: 3020
website: 3021

