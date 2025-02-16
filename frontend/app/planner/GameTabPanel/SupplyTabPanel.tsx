import { Box, TextField, Button, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import { useState } from 'react';


const items = [
  { name: 'Item A', day: 1, price: 100 },
  { name: 'Item B', day: 4, price: 200 },
  { name: 'Item C', day: 5, price: 300 },
  { name: 'Item D', day: 6, price: 400 },
  { name: 'Item E', day: 7, price: 500 },
]

export const SupplyTabPanel = () => {
  const [quantities, setQuantities] = useState(Array(items.length).fill(0));
  const [currentDay, setCurrentDay] = useState(5);

  const handleQuantityChange = (index: number, value: number) => {
    if (typeof(value) !== 'number') {
      return
    }
    const newQuantities = [...quantities];
    newQuantities[index] = Math.max(value, 0);
    setQuantities(newQuantities);
  };

  const handlePurchase = () => {
    const totalAmount = items.reduce((acc, item, index) => acc + item.price * quantities[index], 0);
    alert(`Purchased items for a total of ${totalAmount} Gold`);
  };

  return (
    <Box className="supply-tab-panel text-white">
      <TableContainer component={Paper} sx={{ bgcolor: "#000" }}>
        <Table>
          <TableHead>
            <TableRow >
              <TableCell sx={{textAlign: "center", width: 60, color: "#FFF"}}>品目</TableCell>
              <TableCell sx={{textAlign: "center", width: 60, color: "#FFF"}}>配達日</TableCell>
              <TableCell sx={{textAlign: "center", width: 60, color: "#FFF"}}>単価</TableCell>
              <TableCell sx={{textAlign: "center", width: 60, color: "#FFF"}}>数量</TableCell>
              <TableCell sx={{textAlign: "center", width: 60, color: "#FFF"}}>金額</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {items.map((item, index) => (
              <TableRow key={item.name}>
                <TableCell sx={{px: 4, color: "#FFF"}}>{item.name}</TableCell>
                <TableCell sx={{textAlign: "center", color: "#FFF"}}>Day {currentDay + item.day}</TableCell>
                <TableCell sx={{px: 4, textAlign: "right", color: "#FFF"}}>{item.price}</TableCell>
                <TableCell
                  sx={{px: 4, textAlign: "right", color: "#FFF"}}
                >
                  <TextField
                    type="number"
                    fullWidth
                    value={quantities[index]}
                    onChange={(e) => handleQuantityChange(index, parseInt(e.target.value))}
                    sx={{
                      mx: 2,
                      width: '120px', 
                      color: "#FFF", 
                      bgcolor: "#333",
                      textAlign: "right",
                    }}
                    InputProps={{
                      inputProps: {
                        style: { 
                          margin: '8px 0',
                          padding: '8px 12px',
                          textAlign: 'right' 
                        }
                      }
                    }}
                  />
                </TableCell>
                <TableCell sx={{px: 4, textAlign: "right", color: "#FFF"}}>{item.price * quantities[index]} Gold</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      <Typography mt={2}>
        合計金額: {items.reduce((acc, item, index) => acc + item.price * quantities[index], 0)} Gold
      </Typography>
      <Button variant="contained" onClick={handlePurchase} sx={{ mt: 2 }}>
        『購入』
      </Button>
    </Box>
  )
}