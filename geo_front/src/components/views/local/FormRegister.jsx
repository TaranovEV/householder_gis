import React, {useState, useContext} from "react";
import { Link } from "react-router-dom";
import TextField1 from "../../comps/TextField";
import Button1 from "../../comps/Button";
import {FormControl, Box, Stack} from "@mui/material";
import {UserContext} from "../../../context/UserContext";
import CustomButton from "../../comps/Button";


const FormRegister = () => {
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const [, setToken] = useContext(UserContext)

    const submitRegistration = async () => {
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({first_name: firstName, last_name: lastName, email: email, hashed_password: password}),
        };
        const response = await fetch("/api/register", requestOptions);
        const data = await response.json();

        if (!response.ok){
            setErrorMessage(data.detail)
        } else {
            setToken(data.access)
        }
    };
    const handleSubmit = (e) => {
        e.preventDefault();
        submitRegistration()
    }

    return (
        <React.Fragment>
            <Box
            display="flex"
            justifyContent="center"
            alignItems="center"
            minHeight="100vh"
            onSubmit={handleSubmit}>
                <form>
                    <h2 align={"center"} style={{color: "#334756"}}> REGISTER </h2>
                    <Stack spacing={2} direction="row" sx={{marginBottom: 4}}>
                        <TextField1 label={"First Name"} type={"text"} action={setFirstName} value={firstName}></TextField1>
                        <TextField1 label={"Last Name"} type={"text"} action={setLastName} value={lastName}></TextField1>
                    </Stack>
                        <TextField1 label={"Email"} type={"email"} action={setEmail} value={email} sx={{mb: 4}}></TextField1>
                        <TextField1 label={"Password"} type={"password"} action={setPassword} value={password} sx={{mb: 4}}></TextField1>
                        <CustomButton label={"REGISTER"} type='submit' onClick={handleSubmit}></CustomButton>
                    <br/>
                    <small style={{color: "#FF4C29"}}>Есть аккаунт?<Link to={"/"}> Login</Link></small>
                </form>
            </Box>
        </React.Fragment>
    )
}

export default FormRegister;
