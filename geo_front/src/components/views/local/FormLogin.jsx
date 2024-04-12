import React, {useState} from "react";
import {Link, useNavigate} from "react-router-dom";
import CustomTextField from "../../comps/TextField";
import CustomButton from "../../comps/Button";
import {Box} from "@mui/material";
import setBodyColor from "../../../logic/setBodyColor";
import {baseApiUrl} from "../../../constants";


const FormLogin = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [emailError, setEmailError] = useState(false)
    const [passwordError, setPasswordError] = useState(false)
    // const [, setToken] = useContext(UserContext)
    const navigate = useNavigate()

    setBodyColor({color: "#082032"})

    const submitLogin = async (values) => {
        const requestOptions = {
            method: "POST",
            headers: {"Content-Type": "application/json",
              },
            body: JSON.stringify(
              {username:email, password:password}
            )
        }
        const response = await fetch(`${baseApiUrl}/api/token/`, requestOptions)
        const data = await response.json()
        if (!response.ok){
            localStorage.setItem('accessToken', null)
            localStorage.setItem('refreshToken', null)
            alert(data.detail)
        } else {
            localStorage.setItem('accessToken', JSON.stringify(data.access))
            localStorage.setItem('refreshToken', JSON.stringify(data.refresh))
            navigate('/calculate/')
        }
        }

     const handleSub = (event) => {

        setEmailError(false)
        setPasswordError(false)

        if (email === '') {
            setEmailError(true)
        }
        if (password === '') {
            setPasswordError(true)
        }
        submitLogin()
     }

    return (
        <React.Fragment>
        <Box
            display="flex"
            justifyContent="center"
            alignItems="center"
            minHeight="100vh">
            <form autoComplete="off" onSubmit={handleSub}>
            <h2 align={"center"} style={{color: "#334756"}}>  </h2>
                <br/>
                <CustomTextField sx={{backgroundColor:'red'}} label={"Email"} type={"email"} action={setEmail} value={email} error={emailError}></CustomTextField>
                <br/>
                <CustomTextField label={"Password"} type={"password"} action={setPassword} value={password} error={passwordError}></CustomTextField>
                <br/>
                <CustomButton label={"LOGIN"} onClick={handleSub}></CustomButton>
                <br/>
            <small style={{color: "#FF4C29"}}>Нужна регистрация?<Link to={"/register/"}> Register</Link></small>
            </form>
            </Box>
        </React.Fragment>
    )
}

export default FormLogin;
