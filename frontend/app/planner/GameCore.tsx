import { SupabaseClient } from '@supabase/supabase-js';

export type GameUser = {
  id: string;
}

export type GameState = {
  user_id: String;
  savedata_id: string;
}

export type Player = {
  id: string;
  name: string;
}

export type Savedata = {
  id: string;
  user_id: string;
  name: string;
}

export type SetPlayer = (player: Player) => void;
export type SetGameState = (gameState: GameState) => void;
export type SetSavedataState = (savedata: Savedata) => void;
export type SetSavedataListState = (savedataList: Savedata[]) => void;


export async function fetchPlayerData(supabase: SupabaseClient, user: GameUser) {

}

export const getPlayer = async (supabase: SupabaseClient, user: GameUser, setPlayer: SetPlayer) => {
  let {data: player, error} = await supabase.from('players').select("*").eq('id', user.id).single();
  setPlayer(player);
}


export const createPlayer = async (supabase: SupabaseClient, user: GameUser, name: string, setPlayer: SetPlayer) => {
  let {data: player, error} = await supabase.from('players').insert([{id: user.id, name: name}]).select().single();
  console.log(player);
  setPlayer(player);
}

export const getSavedataList = async (supabase: SupabaseClient, user: GameUser, setSavedataList: SetSavedataListState) => {
  let {data: savedataList, error} = await supabase.from('savedatas').select("*").eq('player_id', user.id);
  console.log(savedataList);
  if (error) console.error(error);
  if (typeof(savedataList) == 'array'){
    setSavedataList(savedataList);
  }
    
}

export const createSavedata = async (supabase: SupabaseClient, user: GameUser, name: string, setSavedata: SetSavedataState) => {
  let { data, create_error } = await supabase
  .rpc('create_savedata', {
    player_id: user.id, 
    savedata_name: name
  });
  if (create_error) console.error(create_error);
  else console.log(data);

  let {data: savedata, read_error} = await supabase
    .from('savedatas')
    .select("*")
    .eq('player_id', user.id)
    .eq('name', name)
    .single();
  if (read_error) console.error(read_error);
  else console.log(savedata);
  setSavedata(savedata);
}