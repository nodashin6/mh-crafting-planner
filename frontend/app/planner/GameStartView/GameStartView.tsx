"use client";
import React, { useState, useEffect } from 'react';
import { 
  Box, Button, TextField, Typography,
  Stack, List, ListItem, ListItemButton, ListItemText,
} from '@mui/material';
import { 
  GameUser, GameState, Player, SetGameState, 
  getPlayer, createPlayer,
  getSavedataList, createSavedata,
  SetPlayer,  SetSavedataState, SetSavedataListState
} from '../GameCore';
import { createClient } from '@/utils/supabase/client';


import { CreatePlayerView  } from './CreatePlayerView';
import { SelectSavedataView } from './SelectSavedataView';
import { GameStartLoading } from './GameStartLoading';
import { GameWelcomeView } from './GameWelcomeView';


export interface GameStartViewProps {
  game_user: GameUser
  setGameState: SetGameState;
}


export const GameStartView = ({game_user, setGameState}: GameStartViewProps) => {
  const user = game_user;
  const supabase = createClient();
  const [phase, setPhase] = useState<number>(0);
  const [player, setPlayer] = useState<Player | null>(null);
  const [savedata, setSavedata] = useState<object | null>(null);

  const onGameStartButtonClick = () => {
    setPhase(1);
  }

  const stepNextPhase = () => {
    setTimeout(() => {
        setPhase(phase + 1);
    }, 1000); // msec
  }

  useEffect(() => {
    if (phase == 1){
      getPlayer(supabase, user, setPlayer);
      stepNextPhase();
    }

  }, [phase]);

  if ([1].includes(phase)) {
    return (
      <GameStartLoading />
    )
  }

  if (phase == 0) {
    return (
      <GameWelcomeView onGameStartButtonClick={onGameStartButtonClick}/>
    )
  }

  if (player == null) {
    return (
      <CreatePlayerView user={user} setPlayer={setPlayer} />
    )
  }
  
  if (savedata==null) {
    return (
      <SelectSavedataView user={user} setSavedata={setSavedata}/>
    )
  }

  return (
    <Typography>
      ゲームスタート
    </Typography>
  )
};
