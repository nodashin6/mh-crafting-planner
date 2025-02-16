"use client";
import React, { useState, useEffect } from 'react';
import { Box, List, ListItemButton, Grid2, Typography } from "@mui/material"
import { StartViewStyle } from "./styles"
import {
  Savedata,
  GameUser, SetSavedataState,
  createSavedata, getSavedataList
} from "../GameCore";
import { createClient } from "@/utils/supabase/client";

const SelectSavedataButtonStyle = {
  p: 2,
  sx: {
    width: "100%",
    height: 60,
    fontSize: 24,
    bgcolor: "#333", // Changed from bgColor to bgcolor
    textAlign: "right",
    '&:hover': {
      bgcolor: "#444"
    }
  }
}

const SavedataRowStyle = {
  p: 2,
  sx: {
    width: "100%",
    height: 60,
    fontSize: 18,
    bgcolor: "#333",
    textAlign: "right",
    '&:hover': {
      bgcolor: "#555"
    }
  }
}


export interface SelectSavedataViewProps {
  user: GameUser;
  setSavedata: SetSavedataState;
}


export const SelectSavedataView = ({user, setSavedata}: SelectSavedataViewProps) => {
  const supabase = createClient();
  const [clickedLoadButton, setClickedLoadButton] = useState<boolean>(false);
  const [savedataList, setSavedataList] = useState<Savedata[]>([]);

  useEffect(() => {
    getSavedataList(supabase, user, setSavedataList);
  }, []);

  const onNewdataButtonClick = () => {
    const numSavedata = savedataList.length + 1;
    createSavedata(supabase, user, `new savedata (${numSavedata})`, setSavedata);
  }

  const onLoadButtonClick = () => {
    setClickedLoadButton(!clickedLoadButton);
  }

  const onSelectSavedataClick = (savedata: Savedata, setSavedata: SetSavedataState) => {
    const _onSelectSavedataClick = () => {
      setSavedata(savedata);
    }
    return _onSelectSavedataClick;
  }

  const onOptionButtonClick = () => {
    //TODO
  }
  return (
    <Box {...StartViewStyle}>
      <Grid2 container width={"100%"} sx={{p: 4}}>
        <Grid2 size={6}>
          <Box height={600} width={"95%"} sx={{p: 0}}>
            <List sx={{p: 0}}>
              <ListItemButton {...SelectSavedataButtonStyle} onClick={onNewdataButtonClick}>
                新しくはじめる
              </ListItemButton>
              <ListItemButton {...SelectSavedataButtonStyle} onClick={onLoadButtonClick}>
                ロード
              </ListItemButton>
              <ListItemButton {...SelectSavedataButtonStyle}>
                オプション
              </ListItemButton>
            </List>
          </Box>

        </Grid2>
        <Grid2 size={6}>
          {
            clickedLoadButton && (
              <Box height={600} width={"95%"} sx={{p: 0, bgcolor: "#333", overflowY: "auto"}}>
              <List sx={{p: 0}}>
                <Typography textAlign={"center"} sx={{p: 2, color: "#FFF"}}>
                  セーブデータ一覧
                </Typography>
                {
                  savedataList.map((savedata) => {
                    return (
                      <ListItemButton key={savedata.name} {...SavedataRowStyle} onClick={onSelectSavedataClick(savedata, setSavedata)}>
                        {savedata.name}
                      </ListItemButton>
                    )
                  })
                }
              </List>
            </Box>
            )
          }
        </Grid2>
      </Grid2>
    </Box>
  )
}