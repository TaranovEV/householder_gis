import React from "react";
import {Button} from "@mui/material";


const CustomButton = (props) => {

    return (
        <React.Fragment>
            <Button sx={{bgcolor: "#2C394B", color: "#FF4C29", minWidth: "100%"}} disabled={props.disable} onClick={props.onClick} type="button">{props.label}</Button>
        </React.Fragment>
    )
}

export default CustomButton;
