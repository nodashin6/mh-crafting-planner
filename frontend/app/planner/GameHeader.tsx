import React from 'react';
import { Box, Typography, Button, Grid2 } from '@mui/material';


export interface GameHeaderProps {
  user_id: string;
  day: number;
  gold: number;
}

export const GameHeader = ({
  user_id,
}: GameHeaderProps) => {
  return (
    <Grid2 container sx={{py: 1, bgcolor: '#223', color: 'white'}}>
      <Grid2 size={5} sx={{px: 1, display: 'flex', alignItems: 'center'}}>
        <Typography variant='body1'>
          ユーザーID <br/>{user_id}
        </Typography>
      </Grid2>
      <Grid2 size={2} sx={{px: 1, display: 'flex', alignItems: 'center'}}>
        <Button>
          <Typography variant='body1'>
            Save As
          </Typography>
        </Button>
      </Grid2>
      <Grid2 size={2} sx={{px: 1, display: 'flex', alignItems: 'center'}}>
        <Button>
          <Typography variant='body1'>
            Load
          </Typography>
        </Button>
      </Grid2>
      <Grid2 size={2} sx={{px: 1, display: 'flex', alignItems: 'center'}}>
        <Button>
          <Typography variant='body1'>
            Exit
          </Typography>
        </Button>
      </Grid2>
    </Grid2>
  )
}