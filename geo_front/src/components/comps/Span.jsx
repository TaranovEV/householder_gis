import React from "react";
import {Button, Typography} from "@mui/material";


const MySpan = (props) => {
    // const {veh_type} = props
    return (
        <React.Fragment>
            {/*<Button sx={{bgcolor: "#2C394B", color: "#FF4C29", minWidth: "100%"}}>{props.label} </Button>*/}
            <Typography sx={{color: "#FF4C29", fontSize: 18}}>{props.text}</Typography>
        </React.Fragment>
    )
}

export default MySpan;