import React from "react";
import {Button} from "@mui/material";


const MyButton = (props) => {

    return (
        <React.Fragment>
            <Button sx={{bgcolor: "#2C394B", color: "#FF4C29", minWidth: "100%"}} onClick={props.onClick}>{props.label} </Button>
        </React.Fragment>
    )
}

export default MyButton;