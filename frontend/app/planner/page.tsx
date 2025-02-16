import { Box, Typography, TextField, Button } from '@mui/material';
import { createClient } from "@/utils/supabase/server"; // Ensure this is the server-side client
import { redirect } from "next/navigation";
import GameOrchestrator, { GameUser, GameOrchestratorProps } from "./GameOrchestrator";
import { useState } from 'react';

const PlannerPage = async () => {
  const supabase = await createClient();

  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return redirect("/sign-in");
  }

  const game_user: GameUser = {
    id: user.id
  }

  return (
    <Box>
      <GameOrchestrator game_user={game_user}/>
    </Box>
  )
}

export default PlannerPage

