"use client";

import { Box, Typography, Button, Tabs, Tab, Grid2 } from '@mui/material';
import { useState } from 'react';
import { createClient } from "@/utils/supabase/client";

import { GameUser, GameState } from './GameCore';
import { GameStartView } from './GameStartView/GameStartView';
import { GameHeader, GameHeaderProps } from './GameHeader';
import { GameTabPanel, GameTabPanelProps } from './GameTabPanel/GameTabPanel';
import { TodayTabPanel } from './GameTabPanel/TodayTabPanel';
import { CraftTabPanel } from './GameTabPanel/CraftTabPanel';
import { SupplyTabPanel } from './GameTabPanel/SupplyTabPanel';


export interface GameOrchestratorProps {
  game_user: GameUser;
}

const boxStyle = {
  minHeight: 900,
  minWidth: 600,
  sx: {
    my: 4,
    bgcolor: "#112"
  }
}

const isDubug = false;
const defaltStarted = isDubug ? true : false;

const GameOrchestrator = ({game_user}:GameOrchestratorProps) => {
  const user = game_user;
  const [gameState, setGameState] = useState<GameState | null>(null);

  if (gameState === null) {
    return (
      <Box {...boxStyle}>
        <GameStartView game_user={user} setGameState={setGameState}/>
      </Box>
    )
  }


  return (
    <Box {...boxStyle}>
      <GameMainView user={user}/>
    </Box>
  )
}

export default GameOrchestrator




interface GameMainViewProps {
  user: GameUser;
}

const GameMainView = ({user}: GameMainViewProps) => {
  const [selectedTab, setSelectedTab] = useState(0);

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setSelectedTab(newValue);
  };

  return (
    <Box minHeight={900}>
      <GameHeader user_id={user.id} day={0} gold={0} />
      <Tabs value={selectedTab} onChange={handleTabChange} sx={{ bgcolor: '#332', color: 'white' }}>
        <Tab label="本日の調合" />
        <Tab label="調合計画" />
        <Tab label="原料調達" />
        <Tab label="財務状況" />
        <Tab label="資材一覧" />
        <Tab label="お知らせ" />
      </Tabs>
      <GameTabPanel value={selectedTab} index={0}>
        <TodayTabPanel />
      </GameTabPanel>
      <GameTabPanel value={selectedTab} index={1}>
        <CraftTabPanel />
      </GameTabPanel>
      <GameTabPanel value={selectedTab} index={2}>
        <SupplyTabPanel />
      </GameTabPanel>
      <GameTabPanel value={selectedTab} index={3}>
        {/* Content for 財務状況 */}
      </GameTabPanel>
      <GameTabPanel value={selectedTab} index={4}>
        {/* Content for アイテム一覧 */}
      </GameTabPanel>
      <GameTabPanel value={selectedTab} index={5}>
        {/* Content for お知らせ */}
      </GameTabPanel>
    </Box>
  )
}





