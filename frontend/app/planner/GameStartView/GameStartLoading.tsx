
import React from 'react';
import { Box, Typography } from '@mui/material';
import { StartViewStyle } from './styles';


export const GameStartLoading = ({}) => {
  return (
    <Box {...StartViewStyle}>
      <Typography>
        ロード中...
      </Typography>
    </Box>
  )
}