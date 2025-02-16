import { Box, Button, TextField, Typography } from "@mui/material";
import { useState } from "react";
import { GameUser, createPlayer, SetPlayer } from "../GameCore";
import { createClient } from "@/utils/supabase/client";
import { StartViewStyle } from "./styles";

export interface CreatePlayerViewProps {
  user: GameUser;
  setPlayer: SetPlayer;
}

export const CreatePlayerView = ({user, setPlayer}: CreatePlayerViewProps) => {
  const supabase = createClient();
  const [playerName, setPlayerName] = useState<string>("");

  const onPlayerCreateButtonClick = async () => {
    if (playerName == "") {
      return;
    }
    await createPlayer(supabase, user, playerName, setPlayer);
  }

  return (
    <Box {...StartViewStyle}>
      <Box>
        <Typography sx={{my: 2, p: 2}}>
          名前の登録がありません
        </Typography>
        <Box display="flex" alignItems="center" sx={{m: 2}}>
          <TextField 
            label="プレイヤー名"
            value={playerName}
            onChange={(e) => setPlayerName(e.target.value)}
            sx={{
              mx: 2,
              width: '360px', 
              color: "#FFF", 
              bgcolor: "#333",
              textAlign: "right",
            }}
            InputProps={{
              inputProps: {
                style: { 
                  margin: '8px 0',
                  padding: '8px 12px',
                  textAlign: 'left',
                  color: "#FFF"
                }
              }
            }}
          />
          <Button 
            color="primary"
            variant="contained"
            onClick={onPlayerCreateButtonClick}
            sx={{
              m: 2, 
              p: 2
            }}
          >
            登録
          </Button>
        </Box>

      </Box>
    </Box>
  )
}
