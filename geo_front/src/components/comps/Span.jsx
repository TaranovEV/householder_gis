import React from "react";
import {Button, Typography} from "@mui/material";


const MySpan = (props) => {
    return (
        <React.Fragment>
            <Typography sx={{color: "#FF4C29", fontSize: 18}}>{props.text}</Typography>
        </React.Fragment>
    )
}

export default MySpan;
