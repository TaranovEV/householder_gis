import React, {useState} from "react";
import {TextField} from "@mui/material";


const FormCalculate = (props) => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [emailError, setEmailError] = useState(false)
    const [passwordError, setPasswordError] = useState(false)

    return (
        <React.Fragment>
            <TextField></TextField>
        </React.Fragment>
    )
}

export default FormCalculate;