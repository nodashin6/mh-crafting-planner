"use client";

import React, { useState, useEffect } from 'react'
import { Box, Typography, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, Button, TextField, MenuItem } from "@mui/material"
import { DataGrid } from "@mui/x-data-grid";
import { createBackendClient } from '@/utils/backend/client';

interface Item {  // don't change this
  id: number;
  code: string;
  name: string;
  leadtime: number;
}

interface Shipment { // don't change this
  id: number;
  item_name: string;
  quantity: number;
  unit: string;
  shipmentType: string;
  time: string;
  date: string;
}

interface ItemRow {  // you can change this
  item: Item;
  dates: { date: string, quantity: number }[];
}

interface Cell {
  item: Item;
  date: string;
}

const fetchItems = async (setter) => {
  const response = await createBackendClient("api/v1/items").read()
  const items = await response.json();
  setter(items);
}

const ShipmentDialog = ({ open, handleSave, handleClose, cell }) => {
  const [quantity, setQuantity] = useState("");
  const [time, setTime] = useState('12:00');
  const [shipmentType, setShipmentType] = useState('FORECAST');
  const [unit, setUnit] = useState('KG');

  useEffect(() => {
    setQuantity("");
  }, [cell])

  const _handleClose = () => {
    handleClose();
  }

  const _handleSave = () => {
    // Save logic here
    const data = {
      quantity,
      time,
      shipmentType,
      unit,
    };
    handleSave(data);
    handleClose();
  };

  return (
    <Dialog open={open} onClose={_handleClose}>
      <DialogTitle>Shipment Management</DialogTitle>
      <DialogContent>
        <DialogContentText>
          Manage shipment for the selected item and date.
        </DialogContentText>
        <TextField
          margin="dense"
          label="Item"
          type="text"
          fullWidth
          value={cell?.item.name || ''}
          disabled
        />
        <TextField
          margin="dense"
          label="Date"
          type="text"
          fullWidth
          value={cell?.date || ''}
          disabled
        />
        <TextField
          margin="dense"
          label="Time"
          type="time"
          fullWidth
          value={time}
          onChange={(e) => setTime(e.target.value)}
        />
        <TextField
          margin="dense"
          label="Shipment Type"
          select
          fullWidth
          value={shipmentType}
          onChange={(e) => setShipmentType(e.target.value)}
        >
          <MenuItem value="FORECAST">FORECAST</MenuItem>
          <MenuItem value="ACTUAL">ACTUAL</MenuItem>
        </TextField>
        <TextField
          margin="dense"
          label="Quantity"
          type="number"
          fullWidth
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />
        <TextField
          margin="dense"
          label="Unit"
          type="text"
          fullWidth
          value={unit}
          onChange={(e) => setUnit(e.target.value)}
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={_handleClose}>Cancel</Button>
        <Button onClick={_handleSave}>Save</Button>
      </DialogActions>
    </Dialog>
  )
}

const ShipmentPage = () => {
  const [thisMonth, setThisMonth] = useState(new Date(2025, 1, 1));
  const [items, setItems] = useState<Item[]>([]);
  const [open, setOpen] = useState(false);
  const [selectedCell, setSelectedCell] = useState<Cell | null>(null);

  useEffect(() => {
    fetchItems(setItems);
  }, []);

  const handleCellClick = (params) => {
    const item = items.find(item => item.id === params.row.id);
    const date = params.field;
    if (item && date) {
      const newCell: Cell = { item, date };
      if (selectedCell === null) {
        setSelectedCell(newCell);
      } else if (newCell.item.name === selectedCell.item.name) {
        setOpen(true);
      } else {
        setSelectedCell(newCell);
      }
    }
  };

  const handleSave = (data) => {
    console.log("saved!!");
    console.log(data);
  };

  const handleClose = () => {
    setOpen(false);
  }

  const columns = [
    { field: 'item', headerName: 'Item', width: 150 },
    // Generate date columns dynamically
    ...Array.from({ length: 31 }, (_, i) => ({
      field: `day${i + 1}`,
      headerName: `${i + 1}`,
      width: 80,
      editable: false,
    })),
  ];

  const rows = items.map((item, index) => ({
    id: item.id,
    item: item.name,
  }));

  return (
    <Box sx={{ m: 2 }}>
      <Typography variant="h4">Shipment</Typography>
      <Typography variant="h6">{thisMonth.toLocaleString('default', { month: 'long' })}</Typography>
      <Box sx={{ mb: 2, minWidth: 600, maxHeight: 1600, overflowY: "scroll" }} >
        <DataGrid
          rows={rows}
          columns={columns}
          onCellClick={handleCellClick}
        />
      </Box>
      <ShipmentDialog
        open={open}
        handleSave={handleSave}
        handleClose={handleClose}
        cell={selectedCell}
      />
    </Box>
  )
}

export default ShipmentPage;