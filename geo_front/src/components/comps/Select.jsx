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

  const [selectItem, setSelectItem] = React.useState('');

  const handleChange = (event) => {
    setSelectItem(event.target.value);
  };

  return (
    <Box sx={{ minWidth: "100%" }}>
      <FormControl fullWidth>
        <InputLabel id={props.id} sx={{color:'#2C394B'}}></InputLabel>
        <Select
          labelId={props.labelId}
          id={props.id}
          value={selectItem}
          label={selectItem}
          onChange={handleChange}
          sx={{
            color: "xx",
            '.MuiOutlinedInput-notchedOutline': {
              borderColor: '#2C394B',
            },
            '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
              borderColor: '#FF4C29',
            },
            '&:hover .MuiOutlinedInput-notchedOutline': {
              borderColor: '#2C394B',
            },
            '.MuiSvgIcon-root ': {
              fill: "xx !important",
            }
          }}
        >
            {listItems}
        </Select>
      </FormControl>
    </Box>
  );
}