
import React from 'react';
import { Box, Button } from '@mui/material';
import { StartViewStyle } from './styles';


export interface GameWelcomeViewProps {
    onGameStartButtonClick: () => void;
}


export const GameWelcomeView = ({onGameStartButtonClick}: GameWelcomeViewProps) => {
    return (
      <Box {...StartViewStyle}>
        <Button variant="contained" color="primary" onClick={onGameStartButtonClick}>
          ゲーム開始
        </Button>
      </Box>
    )
}