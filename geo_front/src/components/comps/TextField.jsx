import React from "react";
import {TextField} from "@mui/material";

const CustomTextField = (props) => {
    const {label, type, action, value, error} = props
    return (
        <React.Fragment>
          <TextField
            label={label}
            onChange={e => {
              const newValue = e.target.value
              action(newValue)}}
            required
            variant="outlined"
            color="warning"
            type={type}
            sx={{
              mb: 3,
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
            inputProps={{
              sx: {
                color: '#FF4C29',
              },
            }}
            InputLabelProps={{
              sx: {
                color: '#FF4C29',
                textTransform: 'capitalize',
              },
            }}
            fullWidth
            value={value}
            error={error} />
        </React.Fragment>
    )
}

export default CustomTextField;
