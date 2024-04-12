import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';


export default function BasicSelect(props) {

    const listItems = props.items.map((item) => (
        <MenuItem value={(props.labelId==="timeLenLabel")? item.toString().match(/\d+/)[0] : item }>{item}</MenuItem>
    ));

  return (
    <Box sx={{ minWidth: "100%" }}>
      <FormControl fullWidth>
        <InputLabel id={props.id}></InputLabel>
        <Select
          labelId={props.labelId}
          id={props.id}
          key={props.id}
          value={props.it}
          onChange={props.onChangeItem}
          sx={{
            color: "#FF4C29",
            '.MuiOutlinedInput-notchedOutline': {
              borderColor: 'rgba(228, 219, 233, 0.25)',
            },
            '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
              borderColor: '#FF4C29',
            },
            '&:hover .MuiOutlinedInput-notchedOutline': {
              borderColor: '#FF4C29',
            },
          }}
        >
            {listItems}
        </Select>
      </FormControl>
    </Box>
  );
}
